#Esercizio 4
tutor:int = 10
studente_attesa:int = 0

while True:
    studente:str = str(input("Inserire il nome dello studente che necessita di un tutor:"))

    if tutor > 0:
        tutor -= 1
        print("Tutor assegnato con successo")

    else:
        studente_attesa += 1
        print("Studente in attesa")

    if tutor == 0 and studente_attesa > 50:
        break
    
    else:
        continue 

    
