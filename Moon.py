from abc import ABC, abstractmethod

class Moon(ABC):
    def __init__(self,name,attacks,geoPossition):
        self.name = name
        self.attacks = attacks
        self.geoPossition = geoPossition

    @abstractmethod
    def createAttacks(self):
        pass

    @abstractmethod
    def attck(self):
        pass