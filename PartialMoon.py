from Moon import Moon
#from Attack import Attack

class PartialMoon(Moon):
    def __init__(self,name,geoPossition):
        super().__init__(name,self.createAttacks(), geoPossition)

    def createAttacks(self):
        return "yes"
        #return [Attack1(),Attack2()]

    def attck(self):
        pass