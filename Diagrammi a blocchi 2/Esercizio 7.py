#Esercizio 7
media:float = 0
somma = 0
i = 0

while True:
    scelta:str = str(input("Vuoi inserire un voto?"))
    if scelta == "si":
        voto:int = int(input("Inserire un voto:"))
        if voto > 0 :
            somma += voto
            i += 1

        else:
            print("Errore, il voto deve essere positivo")

    elif scelta == "no":
        if i > 0 :
            media = somma / i
            print(f"La media è {round(media, 1)}")
        
        else:
            print("Nessun voto inserito")

    else:
        print("La risposta inserita non è valida")



