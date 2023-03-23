from Moon import Moon
from Attack import Attack

class FullMoon(Moon):
    def __init__(self,name,geoPossition):
        super().__init__(name,self.createAttacks(),geoPossition)

    def createAttacks(self):
        return [Attack1(),Attack2(),Attack3()]

    def attck(self):
        pass