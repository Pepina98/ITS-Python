#3C-007
i = 1
croce = 0
testa = 0

for i in range (8):
    moneta:str = str(input("Lancia una moneta. Se esce testa digita t o T mentre se esce croce digita c o C:"))

    match moneta:

        case moneta if moneta == "c" or moneta == "C":
            croce += 1
            i += 1

        case moneta if moneta == "t" or  moneta == "T":
            testa += 1
            i += 1

        case _:
            print("Puoi inserire solo testa o croce.")



    percentuale_testa:float = (testa / i) * 100
    percentuale_testa:float = (round(percentuale_testa, 2))
    print(f"La percentuale dei risultati testa totali è: {percentuale_testa}%")

    percentuale_croce:float = (croce / i) *100
    percentuale_croce:float = (round(percentuale_croce, 2))
    print(f"La percentuale dei risultati croce totali è: {percentuale_croce}%")

    


