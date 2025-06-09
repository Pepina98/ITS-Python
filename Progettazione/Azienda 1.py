from enum import *
from typing import Any
import re

class Indirizzo:
    def __init__(self, via:str, civ:str, cap:str) -> None:
        if not isinstance(via, str) or not isinstance(civ, str) or not (isinstance(cap, str) and len(cap) == 5 and cap.isdigit()):
            raise ValueError("I dati inseriti non sono corretti")
        
        self._via = via
        self._civ = civ 
        self._cap = cap
    
    def get_via(self) -> str:
        return self._via
    
    def get_civ(self) -> str:
        return self._civ
    
    def get_cap(self) -> str:
        return self._cap
    
    def __hash__(self) -> int:
        return hash((self._via(), self._civ(), self._cap()))
    
    def __eq__(self, other:Any) -> bool:
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return(self._via(), self._civ(), self._cap()) == (other._via(), other._civ(), other._cap())
    

class Telefono:
    def __init__(self, telefono:str) -> None:
        if telefono != re('^\d{10}$'):
            raise TypeError("Numero non valido")
        self._telefono = telefono

    def get_telefono(self) -> str:
        return self._telefono 

    def __hash__(self) -> int:
        return hash((self._telefono()))
    
    def __eq__(self, other:Any) -> bool:
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return(self._telefono()) == (other._telefono())


class Stipendio:
    def __init__(self, stipendio:float) -> None:
        if stipendio > 0:
            raise TypeError ("Valore non valido")
        self._stipendio = stipendio

    def get_stipendio(self) -> float:
        return self._stipendio
    
    def __hash__(self) -> int:
        return hash((self._stipendio()))
    
    def __eq__(self, other:Any) -> bool:
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return(self._stipendio()) == (other._stipendio())
    
class Budget:
    def __init__(self, budget:float) -> None:
        if budget > 0:
            raise TypeError ("Valore non valido")
        self._budget = budget

    def get_stipendio(self) -> float:
        return self._budget
    
    def __hash__(self) -> int:
        return hash((self._budget()))
    
    def __eq__(self, other:Any) -> bool:
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return(self._budget()) == (other._budget())
    b


        
    



