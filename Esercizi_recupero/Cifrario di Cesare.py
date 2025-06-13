from string import ascii_lowercase
# se voglio aggiungere anche le lettere maiuscole basta aggiungere ascii_uppercase
# e poi fare degli if dopo il ciclo for 
# for carattere in frase:
#   if carattere in ascii_lowercase:   
#       mettere ciò che è scritto qui sotto
#   elif carattere in ascii_uppercase:
#       mettere ciò che è scritto qui sotto sostituendo ad ascii_lowercase con ascii_uppercase

def cifrario(frase:str, chiave: int) -> str:

    risultato: str = "" # stringa che conterrà il risultato

    for carattere in frase: # voglio codificare la frase quindi scorro carattere per carattere

        # devo trovare l'indice corrispondente al carattere corrente es carattere = "a" idx = 0
        # perchè ascii_lowercase = ["a", "b", "c", "d"... "z"]
        idx: int = ascii_lowercase.index(carattere) 

        idx = (idx + chiave) % len(ascii_lowercase)

        risultato += ascii_lowercase[idx]

    return risultato 


