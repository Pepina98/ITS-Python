#Studente
from persona import Persona 

class Studente(Persona):

    '''
    Attributi della classe Persona in quanto Studente eredita da Persona
    self.name: str
    self.lastname: str
    self.age: int

    Attributi della classe Studente
    self.metricola: str

    '''

    def __init__(self, name: str, lastname: str, age: int, matricola: str):
        # Inizializzo la classe Persona richiamando il metodo __init__ della superclasse
        super().__init__(name, lastname, age)

        # Istruzioni che inizializzanoun oggetto della classe Studente
        self.setMatricola(matricola)

        # metodi setter

        #metodo che imposta il valore dell'attributo self.matricola
    def setMatricola(self, matricola: str) -> None:
        if matricola:
            self.matricola = matricola 

        else:
            print("Error, la stringa matricola non può essere vuota")

    # metodo getter 

    # metodo che ritorna il valore dell'attributo self.matricola
    def getMatricola(self) -> str:
        return self.matricola 
    
    # ridefinire il metodo __str__(overiding)
    def __str__(self) -> str:
        return f"\nNome: {self.name}\nCognome: {self.getLastname()}\nMatricola: {self.getMatricola()}"

