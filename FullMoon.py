from Moon import Moon
from Attack import Attack

class FullMoon(Moon):
    def __init__(self,geoPosition):
        super().__init__(self.createAttacks(),geoPosition)

    def createAttacks(self):
        return [Attack1(),Attack2(),Attack3()]

    def attck(self):
        pass