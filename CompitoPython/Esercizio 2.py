#Esercizio 2
frase:str = str(input("Inserisci una frase:"))

count:int = 0

for lettere in frase:
	
	if lettere ==" ":
		
		count += 1
		
print(f"Il numero degli spazi bianchi è: {count}")