from Moon import Moon
from Attack import Attack

class RedMoon(Moon):
    def __init__(self,geoPosition):
        super().__init__(self.createAttacks(),geoPosition)

    def createAttacks(self):
        return [Attack1()]

    def attck(self):
        pass