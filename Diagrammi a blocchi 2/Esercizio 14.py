#Esercizio 14
punteggio = 0

while True:
    d1:int = int(input("Inserisci il numero che ti è uscito del primo dado:"))
    d2:int = int(input("Inserisci il numero che ti è uscito del secondo dado:"))

    if d1 > 0 and d1 <= 6 and d2 > 0 and d2 <= 6:
        somma = d1 + d2

        if d1 % 2 == 0 and d2 % 2 == 0 and somma > 8:
            punteggio = 100
            print(f"Hai vinto!\nIl tuo punteggio è:{punteggio}")
            break

        elif d1 == 6 or d2 == 6 or somma == 7:
            punteggio += 10
            if punteggio >= 100:
                print(f"Hai vinto\nIl tuo punteggio è:{punteggio} ")
                break

        else:
            punteggio = 0
            print(f"Hai perso!\nIl tuo punteggio è:{punteggio}")
            break
    else:
        d1:int = int(input("Inserisci il numero che ti è uscito del primo dado:"))
        d2:int = int(input("Inserisci il numero che ti è uscito del secondo dado:"))


    