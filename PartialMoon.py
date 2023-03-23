from Moon import Moon
from Attack import Attack

class PartialMoon(Moon):
    def __init__(self,geoPossition):
        super().__init__(self.createAttacks(), geoPossition)

    def createAttacks(self):
        return [Attack1(),Attack2()]

    def attck(self):
        pass