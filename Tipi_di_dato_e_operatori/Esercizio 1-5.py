#Esercizio 1-5

gradiFahrenheit:float = float(input("Inserire la temperatura in gradi Fahrenheit:"))

gradiCelsius:float = 5*(gradiFahrenheit - 32) / 9
gradiCelsius = round(gradiCelsius, 1)

print(f"{gradiFahrenheit} gradi Fahrenheit corrispondono a {gradiCelsius} gradi")