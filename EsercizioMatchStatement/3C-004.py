#3C-004
animale:str = str(input("Inserire un animale:"))

match animale:

    case animlae if animale in ["cane", "gatto", "cavalo", "elefante", "leone"]:
        print(f"{animale} appartiene alla categoria dei Mammiferi!")

    case animale if animale in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
        print(f"{animale} appartiene alla categoria dei Rettili!")

    case animale if animale in ["aquila", "pappagallo", "gufo", "falco"]:
        print (f"{animale} appartiene alla categoria dei Uccelli!!")

    case animale if animale in ["squalo", "trota", "salmone", "carpa"]:
        print(f"{animale} appartiene alla categoria dei Pesci!")

    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")