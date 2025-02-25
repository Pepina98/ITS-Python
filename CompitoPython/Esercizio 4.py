#Esercizio 4
print("Inserire un numero reale e positivo, per uscire dal loop inserire un numero negativo.")

i:int = 0
somma:int = 0
media:float = 0
lista_numeri = []

while True:
    numeri = float(input("Inserire un numero:"))

    if numeri < 0:
        break
    
    else:
        if numeri.is_integer() == True:
            somma += numeri
            i += 1 
            media = somma / i
        
    lista_numeri.append(numeri)

media = somma / i

print (f"La media dei numeri interi e positivi è: {media}")
print(f"Il minimo è: {min(lista_numeri)}")
print(f"Il massimo è: {max(lista_numeri)}")