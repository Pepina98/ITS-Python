#Esercizio 19
somma = 0
prodotto = 1
i = 0
j = 0

while True: 
    n:int = int(input("Inserire un numero intero:"))
    frase:str= str(input("Vuoi continuare a inserire numeri?"))

    if frase == "si":
        continue

    elif frase == "no":
        break

    else:
        print("Risposta non valida")
