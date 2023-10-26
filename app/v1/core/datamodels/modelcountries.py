from enum import Enum
from typing import Any, Dict, List, Union

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

from app.v1.core.datamodels.enums import CarSide, WeekDays


class CountryName(BaseModel):
    common: StrictStr = Field(None)
    official: StrictStr = Field(None)
    native_name: Any = Field(None, alias="nativeName")


class CountryIdd(BaseModel):
    root: StrictStr = Field(None)
    suffixes: List[StrictStr] = Field(None)


class CountryDemonym(BaseModel):
    f: StrictStr = Field(None)
    m: StrictStr = Field(None)


class CountryMap(BaseModel):
    google_maps: StrictStr = Field(None, aias="googleMaps")
    open_street_maps: StrictStr = Field(None, alias="openStreetMaps")


class CountryCar(BaseModel):
    side: CarSide = Field(None)
    signs: List[StrictStr] = Field(None)


class CountryPngSvg(BaseModel):
    png: StrictStr = Field(None)
    svg: StrictStr = Field(None)


class CountryFlag(CountryPngSvg):
    alt: StrictStr = Field(None)


class CountryPostalCode(BaseModel):
    format: StrictStr = Field(None)
    regex: StrictStr = Field(None)


class BaseCountry(BaseModel):
    name: CountryName = Field(None)
    tld: List[StrictStr] = Field(None)
    cca2: StrictStr = Field(None)
    ccn3: StrictStr = Field(None)
    cca3: StrictStr = Field(None)
    cioc: StrictStr = Field(None)
    independent: StrictBool = Field(None)
    currencies: Any = Field(None)
    idd: CountryIdd = Field(None)
    capital: List[StrictStr] = Field(None)
    alt_spellings: List[StrictStr] = Field(None, alias="altSpellings")
    region: StrictStr = Field(None)
    subregion: StrictStr = Field(None)
    languages: Dict[StrictStr, StrictStr] = Field(None)
    translations: Any = Field(None)
    latlng: List[Union[StrictFloat, StrictInt]] = Field(None)
    landlocked: StrictBool = Field(None)
    borders: List[StrictStr] = Field(None)
    area: Union[StrictInt, StrictFloat] = Field(None)
    demonyms: Any = Field(None)
    flag: Any = Field(None)
    maps: CountryMap = Field(None)
    population: Union[StrictInt, StrictFloat] = Field(None)
    gini: Dict[StrictStr, Union[StrictInt, StrictFloat]] = Field(None)
    fifa: StrictStr = Field(None)
    car: CountryCar = Field(None)
    timezones: List[StrictStr] = Field(None)
    continents: List[StrictStr] = Field(None)
    flags: CountryFlag = Field(None)
    coat_of_arms: CountryPngSvg = Field(None, alias="coatOfArms")
    start_of_week: WeekDays = Field(None, alias="startOfWeek")
    capital_info: Any = Field(None, alias="capitalInfo")
    postal_code: CountryPostalCode = Field(None, alias="postalCode")


class CountryCompare(BaseModel):
    countries: List[BaseCountry] = Field(list())


# OpenAPI

Comparable = Enum("Comparable", {str(k).upper(): str(k).lower() for k in list(BaseCountry.__annotations__.keys())})
