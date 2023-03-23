from Moon import Moon
from Attack import Attack

class RedMoon(Moon):
    def __init__(self,name,geoPossition):
        super().__init__(name,self.createAttacks(),geoPossition)

    def createAttacks(self):
        return [Attack1()]

    def attck(self):
        pass