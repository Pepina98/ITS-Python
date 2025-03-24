#Esercizio 18

somma = 0
i = 1
media = 0
somma_pari = 0
somma_dispari = 0

while True:
    n:int = int(input("Inserire un numero intero:"))
    frase:str = str(input("Vuoi continuare a inserire numeri?"))

    somma += n
    media = somma / i 
    

    if frase == "si":
       continue
    
    elif frase == "no":
        break

    else:
        print("La risposta non è valida")

    
    if n % 2 == 0 and n > media:
        somma_pari += n

    i += 1






print(somma_pari)
