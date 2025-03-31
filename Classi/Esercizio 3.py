#Eercizio 3
class Animal:
    def __init__(self, name:str, razza:str, zampe:int):
        self.name = name 
        self.razza = razza
        self.zampe = zampe

    def printInfo(self):
        print(f"{self.name}, {self.razza}, numero zampe {self.zampe}")

    def setLegs (cls, zampe:int):
        cls.zampe = zampe 

    def getLegs (cls):
        return cls.zampe 


        

ragno = Animal("Ragno","Violino", 6)
tasso = Animal("Tasso","Miele", 3)

ragno.setLegs(8)
tasso.setLegs(4)

ragno.printInfo()
tasso.printInfo()




