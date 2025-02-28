#3C-010
giorno:int = int(input("Inserire il giorno:"))
mese:str = str(input("Inserire il mese:"))

data = (giorno, mese)

match data:

    case data if giorno == 1 and mese == "Gennaio":
        print("Capodanno")

    case data  if giorno == 14 and mese == "Febbraio":
        print("San Valentino")

    case data if giorno == 2 and mese == "Giugno":
        print("Festa della Repubblica")

    case data if giorno == 15 and mese == "Ferragosto":
        print("Ferragosto")

    case data if giorno == 31 and mese == "Ottobre":
        print("Halloween")

    case data if giorno == 25 and mese == "Dicembre":
        print("Natale")
    
    case _:
        print("Nessuna festività importante in questa data")

    
