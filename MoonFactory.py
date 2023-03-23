from enum import Enum
from FullMoon import FullMoon
from PartialMoon import PartialMoon
from RedMoon import RedMoon

class MoonEnum(Enum):
    FULL_MOON = "Full moon"
    PARTIAL_MOON = "Partial Moon"
    RED_MOON = "Red Moon"

class MoonFactory:
    def serialize(self, moonsName,geoPossition, moonType):
        match moonType:
            case MoonEnum.FULL_MOON:
                return FullMoon(moonsName, geoPossition)
            case MoonEnum.PARTIAL_MOON:
                return PartialMoon(moonsName, geoPossition)
            case MoonEnum.RED_MOON:
                return RedMoon(moonsName, geoPossition)
            case _:
                raise ValueError(moonType)