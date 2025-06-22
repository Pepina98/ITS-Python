from custom_types import *
from dipartimento import *
from impiegato import *
from typing import Any
from datetime import datetime

class Afferenza:

    def __init__(self, impiegato:Impiegato, dipartimento: Dipartimento, data_afferenza:datetime):
        self._impiegato: Impiegato = impiegato
        self._dipartimento: Dipartimento = dipartimento 
        self._data_afferenza: datetime = data_afferenza

    def data_afferenza(self) -> datetime:
        return self._data_afferenza
    
    def impiegato(self) -> Impiegato:
        return self._impiegato 
    
    def dipartimento(self) -> Dipartimento:
        return self._dipartimento
    
    def __hash__(self) -> int:
        return hash((self.impiegato(), self.dipartimento(), self.data_afferenza()))
    
    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False
        
        return (self.impiegato(), self.dipartimento(), self.data_afferenza()) == (other.impiegato(), other.progetto(), other.data_afferenza())


