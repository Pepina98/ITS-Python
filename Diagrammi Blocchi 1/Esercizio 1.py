#Esercizio 1
cateto_uno:float = float(input("Inserisci il valore del primo cateto:"))
ipotenusa:float = float(input("Inserisci il valore dell'ipotenusa:"))

if ipotenusa > cateto_uno:
    cateto_due:float = (ipotenusa ** 2 - cateto_uno ** 2)**(1/2)

    print(f"Il valore del secondo cateto è:{cateto_due}")
    

