from typing import Annotated, Any, Dict, List

from fastapi import APIRouter, Path, Query
from fastapi_versioning import version
from pydantic import StrictStr
from starlette import status

from app.config import V
from app.v1.core.datamodels.modelcountries import BaseCountry, Comparable
from app.v1.corefuncs import countriesfuncs
from app.v1.decorators import manage_transaction

router = APIRouter(prefix="/countries")


@router.get(
    "/{name}/info",
    status_code=status.HTTP_200_OK,
)
@version(V)
@manage_transaction
async def get_country_infop(
    name: Annotated[StrictStr, Path(..., description="country name")],
) -> BaseCountry:
    """
    Get country information.
    Country is retrieved by full name.

    Args:
        `name` (Annotated[StrictStr, Path]): the name of the country.

    Returns:
        `BaseCountry`: country model response.
    """
    return await countriesfuncs.get_country_by_name(name)


@router.get(
    "/compare",
    status_code=status.HTTP_200_OK,
)
@version(V)
@manage_transaction
async def compare_countries_info(
    countries_names: Annotated[List[StrictStr], Query(..., description="countries names", max_length=2, min_length=2)],
    compare: Annotated[
        List[Comparable],
        Query(
            ...,
            description="list of keys identifying the fields to compare",
        ),
    ],
) -> List[Dict[StrictStr, Any]]:
    """
    Compare two countries: comparison can be made on one of the fields available or on all of them.

    Args:
        `countries_names` (Annotated[List[StrictStr], Query]): name of the countries to compare.
        `compare` (Annotated[ List[Comparable], Query]): ist of keys identifying the fields to compare.

    Returns:
        List[Dict[StrictStr, Any]]: fields comparison between two countries.
    """
    return await countriesfuncs.compare_countries(countries_names, compare)
