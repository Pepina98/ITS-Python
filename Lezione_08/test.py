from persona import Persona
from studente import Studente

# creo un oggetto p della classe Persona
p: Persona = Persona("Rachele", "Corsi", 27)

# visualizzare le informazioni dell'oggetto p
print(p)

# creare un oggetto studente1 della classe Studente
studente1: Studente = Studente("Mario", "Rossi", 20 ,"0123456")

# visualizzare le informazioni relative all'oggetto studente1
print(studente1)

# controllare se studente1 è istanza della classe Studente
# isinstance(obj, class) -> controlla se l'oggetto obj sia istanza della classe Class
# in caso affermativo -> True
# in caso negativo -> False
if isinstance(studente1, Studente):
    print("\nstudente1 è istanza della classe Studente")

# controllo se studente1 sia anche un'istanza della classe Persona 
if isinstance(studente1, Persona):
    print("\nstudente1 è un oggetto della classe Studente ma è anche un oggetto della classe Persona")

# controllo se l'oggetto p sia istanza della classe Persona
if isinstance(p, Persona):
    print("\np è un oggetto della classe Persona")

# controllo se l'oggetto p sia anche un'istanza della classe Studente
if isinstance(p, Studente):
    print("\np è un oggetto della classe Persona ma anche un oggetto della classe Studente")
else:
    print("\np è un oggetto della classe Persona ma non è un oggetto della classe Studente")


# come controllare se una classe è sottoclasse di un'altra
# controllo che la classe Studente sia sottoclasse della classe Persona
# issubclass(Class1, Class2) -> controlla se la classe Class1 è sottoclasse della classe Class2
# in caso affermativo -> True
# in caso negativo -> False

if issubclass(Studente, Persona):
    print("\nla classe Studente è sottoclasse della classe Persona")


