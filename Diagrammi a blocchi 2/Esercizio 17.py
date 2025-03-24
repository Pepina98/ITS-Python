#Esercizio 17
media = 0
somma = 0
i = 1

temperatura = []

while i < 8:
    temp:float= float(input("Inserire la temperatura:"))
    giorno:int = int (input("Inserire il giorno:"))
    
    somma = temp + somma 
    media = somma / i

    temperatura.append(temp)

    massima = max(temperatura)
    minima = min(temperatura)

    i += 1

    if temp >= 10 and temp <= 30:
        print("Temperatura nella norma")
    
    elif temp >= 35 or temp < 5:
        print("Allerta temperatura")


print(f"La temperatura media è: {media :.1f}°C")
print(f"Si ha la temperatura massima di {massima}°C il giorno {giorno}")
print(f"Si ha la temperatura {minima}°C il giorno {giorno}")




