#Esercizio 2

#Primo caso ciclo for
massimo = input("Inserisci il primo numero che sarà il nostro massimo all'inizio:")
i = 0

for i in range(4):
    numeri:float = float(input("Inserisci un valore:"))
    i += 1

    if numeri > massimo:
        massimo = numeri

print(f"Il massimo è:{massimo}")

#Secondo caso ciclo while repeat
massimo = input("Inserisci il primo numero che sarà il nostro massimo all'inizio:")
i = 0

while True:
    if i == 4:
        break 
    else:
        numeri:float = float(input("Inserisci un valore:"))
        i += 1

        if numeri > massimo:
             massimo = numeri

print(f"Il massimo è:{massimo}")

#Terzo caso ciclo while
massimo = input("Inserisci il primo numero che sarà il nostro massimo all'inizio:")
i = 0

while i < 4:
    numeri:float = float(input("Inserisci un valore:"))
    i += 1

    if numeri > massimo:
        massimo = numeri

print(f"Il massimo è:{massimo}")







