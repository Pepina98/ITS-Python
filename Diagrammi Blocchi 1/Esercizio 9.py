#Esercizio 9
nome:str = str(input("Inserisci un nome:"))
vendite:int = int(input("Inserisci il numero di vendite:"))

massimo:int = vendite
minimo:int = vendite
max_name = nome
min_name = nome

for i in range(20):
    new_name:str = str(input("Inserisci un nome:"))
    new_vendite:int = int(input("Inserisci il numero di vendite:"))

    if new_vendite > massimo:
        max_name = new_name
        massimo = new_vendite

    elif new_vendite < minimo:
        min_name = new_name
        minimo = new_vendite

print(f"{max_name} è il venditore con il numero di vendite maggiori pari a {massimo}")
print(f"{min_name} è il venditore con il numero di vendite minori pari a {minimo}")
