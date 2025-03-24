#Esercizio 16
positivi = 0
negativi = 0
pari = 0
dispari = 0
i = 0

while i < 3:
    n:int = int(input("Inserire 10 numeri interi:"))
    i += 1
    match n:
        case n if  n > 0:
            positivi += 1
            match n:
                case n if n % 2 == 0 and n > 20:
                    pari += 1 
        
        case n if  n < 0:
            negativi += 1
            match n:
                case n if n % 2 != 0 and n < -10:
                    dispari += 1

        case _:
            
            print("Errore")
    
print(f"I numeri positivi sono: {positivi}")
print(f"I numeri negativi sono: {negativi}")
print(f"I numeri positivi, pari e maggiori di 20 sono: {pari}")
print(f"I numeri negativi, dispari e minori di -10 sono: {dispari}")

        
