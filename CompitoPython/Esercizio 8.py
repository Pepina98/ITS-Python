#Esercizio 8
lista_numeri:list = []
i = 0

while i < 5:
    n:int = int(input("Inserire un numero intero compreso tra 1 e 30 (max 5 numeri):"))
    if n >= 1 and n <= 30:
        lista_numeri.append(n)
        i += 1
    else:
        print("Digitare un numero compreso tra 1 e 30")
    
for num in lista_numeri:
    print("*" * num)