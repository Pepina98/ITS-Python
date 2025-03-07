#Esercizio 11
liberi = 20

while True:
    opzione:str = str(input("Inserisci un opzione:"))

    match opzione:

        case "prenota":
            if liberi > 0:
                liberi -= 1

            else:
                print("Non ci sono posti disponibili")

        case "libera":
            if liberi < 20:
                liberi += 1

            else:
                print("Tutti i posti sono già disponibili")

        case "visualizza":
            print(f"I posti liberi sono {liberi}")
            print(f"I posti occupati sono {20 - liberi}")

        case "esci":
            break 

        case _:
            print("L'opzione inserita non è valida")



