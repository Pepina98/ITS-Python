import random
from typing import Any

class Creatura:
    def __init__(self, nome:str):
        self.setNome(nome)

    def setNome(self, nome:str) -> None:
        
        if isinstance(nome, str):
            self.__nome = nome

        else:
            self.__nome = "Creatura Generica"

    def getNome(self) -> str:
        return self.__nome 
    
    def __str__(self) -> str:
        return f'Creatura: {self.getNome()}'
    
class Alieno(Creatura):
    def __init__(self, nome:str):
        super().__init__(nome)
        self.__setMatricola()
        self.__setMunizioni()

        if nome == "Robot-"+str(self.getMatricola()):
            self.setNome(nome)
        else:
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            self.setNome("Robot-"+str(self.getMatricola()))
    
    def __setMatricola(self) -> None:
        self.__matricola = random.randint(10000, 90000)

    def __setMunizioni(self) -> None:
        self.__munizioni = list(x**2 for x in range(0, 16))

    def getMatricola(self) -> int:
        return self.__matricola
    
    def getMunizioni(self) -> list[int]:
        return self.__munizioni 
    
    def __str__(self) -> str:
        return f'Alieno: {self.getNome()}'
    
class Mostro(Creatura):
    def __init__(self, nome:str, urlo_vittoria:str, gemito_sconfitta:str):
        super().__init__(nome)
        self.__setAssalto()
        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(gemito_sconfitta)

    def __setAssalto(self) -> None:
        self.__assalto = list(random.randint(1, 100) for y in range(15))

    def __setVittoria(self, vittoria:str) -> None:
        if isinstance(vittoria, str):
            self.__urlo_vittoria = vittoria
        else:
            self.__urlo_vittoria = "GRAAAHHH"

    def __setSconfitta(self, sconfitta:str) -> None:
        if isinstance(sconfitta, str):
            self.__gemito_sconfitta = sconfitta
        else:
            self.__gemito_sconfitta = "Uuurghhh"

    def getAssalto(self) -> list[int]:
        return self.__assalto
    
    def getVittoria(self) -> str:
        return self.__urlo_vittoria
    
    def getSconfitta(self) -> str:
        return self.__gemito_sconfitta

    def __str__(self) -> str:
        nome_str = self.getNome().lower()
        for i in range(1, len(nome_str), 2):
            nome_str[i] = nome_str[i].upper()
        return f'Mostro: {nome_str}'


def pariUguali(a:list[int], b:list[int]) -> list[int]:
    c:list = []

    for i in range(len(a)):
        if a[i] %2 == 0 and b[i] %2 == 0:
            c.append(1)
        else:
            c.append(0)
    return c 

def combattimento(a:Alieno, m:Mostro) -> Any:
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Combattimento terminato")
        return None
    
    c = pariUguali(a.getMunizioni(),m.getAssalto())
    uno = 0
    for i in c:
        if i == 1:
            uno += 1 

    if uno >= 4:
        for urlo in range(3):
            print(m.getVittoria)
            return m
    else:
        print(m.getSconfitta)
        return a 
    
def proclamaVincitore(c:Creatura) ->None:
    print(c.getNome())

if __name__ == '__main__':
    a:Alieno = Alieno("Robot-")
    m:Mostro = Mostro('Godzilla', 1, 2 )
    c = combattimento(a,m)
    proclamaVincitore(c)







    










    
        

    


        
    





    

