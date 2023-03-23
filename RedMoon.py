from Moon import Moon

class RedMoon(Moon):
    def __init__(self,geoPosition):
        super().__init__(self.createAttacks(),geoPosition)

    def createAttacks(self):
        attack1 = A1()
        attack1.setRecoveryTime(0.8)
        return [attack1]