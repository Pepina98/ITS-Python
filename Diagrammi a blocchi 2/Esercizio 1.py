#Esercizio 1
posti:int = int(input("Inserire un numero massimo di posti:"))

liberi = posti

while True:
    opzione:str = input("Inserire un opzione:")

    match opzione:

        case "ingresso":
            if liberi > 0:
                liberi -= 1

            else:
                print("Non ci sono posti disponibili")

        case "uscita":
            if liberi < posti:
                liberi += 1

            else:
                print("Tutti i posti sono disponibili")

        case "stato":
            print(f"I posti liberi sono {liberi}")
            print(f"I posti occupati sono {posti - liberi}")

        case "esci":
            break

        case _:
            print("L'opzione inserita non è valida")