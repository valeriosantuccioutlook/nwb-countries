import requests
from requests import Response
from starlette import status
from typing_extensions import Self

from app.config import settings
from app.v1.core.datamodels.modelcountries import BaseCountry
from app.v1.utils import ExtCache


class Country:
    """
    Handle the requests logic against https://restcountries.com services.
    """

    # Private
    __URL: str = settings.URL

    def __new__(cls, *args, **kwargs) -> Self:
        instance = super().__new__(cls)
        return instance

    def __init__(self, name: str) -> None:
        self.name = name
        self.cacher = ExtCache(name)
        self.url = self.__URL.format(name=self.name)

    async def retrieve_country(self) -> BaseCountry | None:
        """
        Retrieve country info.
        To respect a limit of requests, the country info for a given
        name is cached for a limited period of time.

        Returns:
            BaseCountry | None: country model response, if country info found.
            None otherwise.
        """
        cached = self.cacher.get()
        if cached is not None:
            return BaseCountry(**cached)
        req: Response = requests.get(self.url)
        if req.status_code == status.HTTP_404_NOT_FOUND:
            return None
        _data = req.json()
        self.cacher.set(_data[0])
        return BaseCountry(**_data[0])
