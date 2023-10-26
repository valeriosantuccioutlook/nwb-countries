from enum import Enum


class CarSide(Enum):
    R: str = "right"
    L: str = "left"


class WeekDays(Enum):
    MO: str = "monday"
    TU: str = "tuesday"
    WE: str = "wednesday"
    TH: str = "thursday"
    FR: str = "friday"
    ST: str = "saturday"
    SN: str = "sunday"
