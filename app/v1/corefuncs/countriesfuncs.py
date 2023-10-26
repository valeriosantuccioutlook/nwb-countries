import asyncio
from concurrent.futures import ProcessPoolExecutor as ppe
from typing import Any, Dict, List

from fastapi.exceptions import HTTPException
from pydantic import StrictStr
from starlette import status

from app.v1.core.apis.apicountries import Country
from app.v1.core.datamodels.modelcountries import BaseCountry, Comparable


async def get_country_by_name(name: StrictStr) -> BaseCountry:
    """
    Find country by `name`.

    Args:
        :name (StrictStr): name of the country.

    Returns:
        BaseCountry: country response model.
    """
    country = Country(name.lower())
    data: BaseCountry = await country.retrieve_country()
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"msg": f"Country with name `{name}` not found"}
        )
    return data


async def compare_countries(
    countries_names: List[StrictStr], comparable: List[Comparable]
) -> List[Dict[StrictStr, Any]]:
    """
    Make a comparison between two existing countries on
    a given list of existing fields.

    Args:
        :countries_names (List[StrictStr]): list of names of countries.
        :comparable (List[Comparable]): list of fields to compare.

    Raises:
        HTTPException: if one or both countries could not be found.

    Returns:
        List[Dict[StrictStr, Any]]: list of comparable fields.
    """
    with ppe():
        countries: List[BaseCountry] = list()
        tasks = list()
        loop = asyncio.get_event_loop()

        for name in countries_names:
            tasks.append(loop.create_task(get_country_by_name(name)))

        countries = await asyncio.gather(*tasks, return_exceptions=True)
        if not all(isinstance(c, BaseCountry) for c in countries):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "One or both countries could not be found"}
            )

        comparison = list()
        tasks = list()
        for country in countries:
            tasks.append(loop.create_task(_extract_fields(country, comparable)))
        comparison = await asyncio.gather(*tasks)
        return comparison


async def _extract_fields(country: BaseCountry, comparable: List[Comparable]) -> Dict[StrictStr, Any]:
    """
    Extract the requested fields from the response model.

    Args:
        :country (BaseCountry): country rsponse model.
        :comparable (List[Comparable]): list of comparable fields.

    Returns:
        Dict[StrictStr, Any]: filtered comparable fields.
    """
    NAME: str = "name"
    _fields = dict()
    _fields[NAME] = country.name.common

    for c in comparable:
        _fields[c.value] = getattr(country, c.value)
    return _fields
