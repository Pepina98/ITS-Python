#Esercizio 10
eta:int = int(input("Inserisci la tua età:"))

match eta:

    case eta if eta >= 18 and eta <= 65 :
        print("L'utente può partecipare all'attività")

    case eta if eta < 18 :
        print("L'utente non può partecipare perchè non ha raggiunto l'età minima")

    case _:
        print("L'utente non può partecipare perchè ha superato l'età massima")