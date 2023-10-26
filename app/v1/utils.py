from typing import Any, Union

from app.config import cache
from app.v1.core.datamodels.modelcountries import BaseCountry


class ExtCache:
    def __init__(self, name: str) -> None:
        self.name = name
        _cached = cache.get(name)
        if _cached is not None:
            _cached = BaseCountry(**_cached)
        self.cached: Union[BaseCountry, None] = _cached

    def set(self, value: Any) -> None:
        """
        Set cache value into the file system.

        Args:
            :value (Any): valu to cache.
        """
        cache.set(self.name, value)

    def get(self) -> dict | None:
        """
        Get cached value from the file system.

        Returns:
            dict | None: cached value. None if not found.
        """
        return cache.get(self.name)
