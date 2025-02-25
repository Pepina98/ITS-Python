#Esercizio 10
lista_numeri:list = []
lista_pari:list = []
lista_dispari:list = []
numeri_massima_frequenza:list =[]
frequenza_numero:dict = {}
massima_frequenza = 0

i= 0
count = 0
somma_pari = 0
somma_dispari = 0
media_dispari = 0

while True:
    n:int = int(input("Inserisci un numero intero, per terminare il loop inserire 0:"))
    
    if n != 0 and n % 1 == 0:
        lista_numeri.append(n)
        i += 1 
        
    else:
        break
print(f"La lista dei numeri è: {lista_numeri}")

for num in lista_numeri:
    if num % 2 ==0:
        lista_pari.append(num)
    else:
        lista_dispari.append(num)
        count += 1
        
    if num in frequenza_numero:
        frequenza_numero[num] += 1 
    else:
        frequenza_numero[num] = 1 

for key, value in frequenza_numero.items():
    if value > massima_frequenza:
        massima_frequenza = value
        numeri_massima_frequenza = [key]
    
    elif value == massima_frequenza:
        numeri_massima_frequenza.append(key)
    

print(f"La somma dei numeri pari è: {sum(lista_pari)}")

somma_dispari = sum(lista_dispari)
media_dispari = somma_dispari / count
print(f"La media dei numeri dispari è: {media_dispari}")

print(f"Il numero con maggiore frequenza nella lista è: {numeri_massima_frequenza} che si ripete per {massima_frequenza} volte")
