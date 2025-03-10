#Esercizio 2
soglia:int = int(input("Inserire valore di soglia:"))
nord_sud:int = int(input("Inserire il numero di veicoli nella direzione nord e sud:"))
est_ovest:int = int(input("Inserire il numero di veicoli nella direzione est ed ovest:"))


if soglia < nord_sud and soglia < est_ovest:
    print("Il tempo minimo garantito per il verde per la direzione nord-sud è 50%") 
    print("Il tempo minimo garantito per il verde per la direzione est-ovest è 50%")

elif soglia < nord_sud:
    print("Il tempo minimo garantito per il verde per la direzione nord-sud è 60%")
    print("Il tempo minimo garantito per il verde per la direzione est-ovest è 40%")

elif soglia < est_ovest:
    print("Il tempo minimo garantito per il verde per la direzione nord-sud è 40%")
    print("Il tempo minimo garantito per il verde per la direzione est-ovest è 60%")

elif soglia > nord_sud and soglia > est_ovest:
    print(f"Il tempo minimo garantito per il verde per la direzione nord-sud è {((nord_sud / (nord_sud + est_ovest)) * 100):.1f}%")
    print(f"Il tempo minimo garantito per il verde per la direzione est_ovest è {((est_ovest / (nord_sud + est_ovest)) * 100):.1f}%")

else:
    print("Opzione non valida")
