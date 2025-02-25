#Esercizio 1
print("Inserire una parola, se si vuole uscire dal loop digitare la parola fine")
while True:
	parola = str(input("Inserisci una parola:"))
	
	if parola == "fine" :
		break 
	
	elif parola [0] == parola [-1] :
		print ("Il primo e l'ultimo carattere sono uguali")
		
	else:
		print("Il primo e l'ultimo carattere non sono uguali")
		continue 