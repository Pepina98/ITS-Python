from custom_types import *
from progetto import *
from impiegato import *
from typing import Any

class Coinvolto:

    def __init__(self, impiegato: Impiegato, progetto: Progetto):
        self._impiegato: Impiegato = impiegato
        self._progetto: Progetto = progetto 

    def impiegato(self) -> Impiegato:
        return self._impiegato
    
    def progetto(self) -> Progetto:
        return self._progetto
    
    def __hash__(self) -> int:
        return hash((self.impiegato(), self.progetto()))
    
    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False
        
        return (self.impiegato(), self.progetto()) == (other.impiegato(), other.progetto())
