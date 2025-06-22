from custom_types import *
from impiegato import *

class Progetto:

    def __init__ (self, nome:str, budget: RealGEZ, impiegati: set[Impiegato]| None=None):
        
        self.set_nome(nome)
        self.set_budget(budget)
        self._set_impiegati: set[Impiegato] = ()
        if impiegati:
            for i in impiegati:
                self.add_impiegato(i)

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def set_budget(self, budget:RealGEZ) -> None:
        self._budget = budget

    def nome(self) -> str:
        return self._nome
    
    def budget(self) -> RealGEZ:
        return self._budget
    
    def add_impiegato(self, impiegato:Impiegato) -> None:
        self._set_impiegati.add(impiegato)

    def remove_impiegato(self, impiegato:Impiegato) -> None:
        self._set_impiegati.remove(impiegato)

    def impiegati(self) -> frozenset[Impiegato]:
        return frozenset(self._set_impiegati)

    



