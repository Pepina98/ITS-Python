#Esercizio 12
n:int = int(input("Quante volte vuoi inserire x e y?"))

somma = 0
prodotto = 1

for i in range(n):
    x:int = int(input("Assegna valori a x:"))
    y:int = int(input("Assegna valori a y:"))

    if x > 0 and y > 0 :
        prodotto = x * y

    elif x < 0 or y < 0 :
        somma = x + y

    else:
        print("Errore")

print(f"Il prodotto tra x e y è: {prodotto}")
print(f"La somma tra x e y è: {somma}")