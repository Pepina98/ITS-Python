#Esercizi 1-6
itsBakeryMenu:dict = {"pizza": 9.00, "pasta":10.50, "zuppa":7.00, "hamburger":15.50, "cotoletta":10.00, "salmone":20.20, "patatine fritte": 5.50, "patate al forno":5.50, "verdura del giorno":7.00, "cheesecake":6.00, "tiramisù":6.00, "focaccia con nutella": 6.00, "coca cola":3.50, "acqua":1.50, "vino": 5.00}

ordine:dict = {}

ordine["pasta"] = 10.50
ordine["salmone"] =  20.20
ordine["verdura del giorno"] =  7.00
ordine["tiramisù"] = 6.00
ordine["acqua"] = 1.50

print(ordine)

print(ordine.values())

totale:float = sum (ordine.values())
print(f"Il conto totale è : {totale} euro")
