from enum import Enum
from FullMoon import FullMoon
from PartialMoon import PartialMoon
from RedMoon import RedMoon
import logging

class MoonEnum(Enum):
    FULL_MOON = "Full moon"
    PARTIAL_MOON = "Partial Moon"
    RED_MOON = "Red Moon"

class MoonFactory:
    def serialize(self, moonsName,geoPossition, moonType):
        match moonType:
            case MoonEnum.FULL_MOON.value:
                return FullMoon(moonsName,geoPossition)
            case MoonEnum.PARTIAL_MOON.value:
                return PartialMoon(moonsName,geoPossition)
            case MoonEnum.RED_MOON.value:
                return RedMoon(moonsName,geoPossition)
            case _:
                logging.error(f"Tried to create a false moon named: {moonType}")
                raise ValueError(moonType)

def main():
    moonFactory = MoonFactory()
    moon = moonFactory.serialize("Ynon","x","Full moon")
    print(type(moon))

if __name__ == "__main__":
    main()