#Esercizio 6
x:int = int(input("Inserire un numero positivo:"))
i = 0
somma = 0

if x > 0:
    while True:
        if i < 10:
            n:int = int(input("Inserire 10 numeri sia positivi che negativi:"))
            if x %2 == 0 and n> x/2:
                somma = somma + n
                print(f"La somma dei numeri che sono maggiori della metà di x è {somma}")

            elif x %2 != 0 and n < x:
                somma = somma + n
                print(f"La somma dei numeri che sono minori di x è {somma}")

            i += 1

        else:
            i += 1

else:
    print("Errore, il numero deve essere positivo")




