#Esercizio 3
posti:int = 100
nome_corso:str = str(input("Inserire il nome del corso:"))

print(f'Le seguenti opzioni che si possono inserire sono: "iscrivi", "annulla", "visualizza", "elimina" ed "esci"')

while True:
    opzione:str = str(input("Inserire un'opzione tra quelle elencate:"))

    match opzione:

        case "iscrivi":
            if posti > 0:
                posti -= 1
            else:
                print("Non ci sono posti disponibili")

        case "annulla" :
            if posti < 100:
                posti += 1
            else:
                print("Tutti i posti sono già disponibili")

        case "visualizza":
            print(f"Il numero di posti disponibili è {posti}")
            print(f"Il numero di posti occupati è {100 - posti}")

        case "elimina":
            nome_corso:str = str(input("Inserire il nome del corso:"))

        case "esci":
            break

        case _:
            print("Opzione non valida")





