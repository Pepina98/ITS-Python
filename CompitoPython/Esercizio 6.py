#Esercizio 6
n1:int = int(input("Inserire il primo numero:"))
n2:int = int(input("Inserire il secondo numero:"))

prodotto1:int = 1
prodotto2:int = 1

if n1 < n2:
    for i in range(n1, n2 + 1):
        prodotto1 *= i
    print(f"Il prodotto è: {prodotto1}")

else:
    for i in range (n2, n1 +1):
        prodotto2 *= i
    print(f"Il prodotto è: {prodotto2}")