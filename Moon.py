from abc import ABC, abstractmethod


class Moon(ABC):
    def __init__(self,attacks,geoPosition):
        self.attacks = attacks
        self.geoPosition = geoPosition

    @abstractmethod
    def attck(self):
        pass