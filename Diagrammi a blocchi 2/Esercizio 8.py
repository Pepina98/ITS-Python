#Esercizio 8

a:int = int(input("Inserire il primo numero intero positivoe A:"))
b:int = int(input("Inserire il secondo numero intero positivo B:"))

i = a
somma = 0

if a < b:
    if a >0 and b > 0 :
        if a % 1 == 0 and b % 1 == 0 :
            while i <= b:
                somma = somma + i
                i += 1
            print(f"La somma è {somma}")

        else:
            print("A e B devono essere interi")
    else:
        print("A e B devono essere positivi")

else:
    print("A deve essere minore di B")


