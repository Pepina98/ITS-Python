#3C-006
animale:str = str(input("Inserire un animale:"))
habitat:str = str(input("Inserire un habitat:"))

match animale:

    case animale if animale in ["cane", "gatto", "cavalo", "elefante", "leone", "balena", "delfino"]:
        print(f"{animale} appartiene alla categoria dei Mammiferi!")
        animal_type = "Mammifero"

    case animale if animale in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
        print(f"{animale} appartiene alla categoria dei Rettili!")
        animal_type = "Rettile"

    case animale if animale in ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]:
        print (f"{animale} appartiene alla categoria dei Uccelli!!")
        animal_type = "Uccello"

    case animale if animale in ["squalo", "trota", "salmone", "carpa"]:
        print(f"{animale} appartiene alla categoria dei Pesci!")
        animal_type = "Pesce"

    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")
        animal_type = "Unknown"

animale_inf:dict = {}

animale_inf["animale"] = animale
animale_inf["categoria"] = animal_type
animale_inf["habitat"] = habitat 

match animale_inf:

    case animale_inf if animale_inf["animale"] in ["cane", "gatto", "cavalo", "elefante", "leone"]:
        match animale_inf:
            case animale_inf if animale_inf["habitat"] == "terra":
                print(f"L'animale {animale} è uno dei mammiferi che può vivere sulla terra")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere in {habitat}")
    
    case animale_inf if animale_inf["animale"] in ["balena", "delfino"]:
        match animale_inf:
            case animale_inf if animale_inf["habitat"] == "acqua":
                print(f"L'animale {animale} è uno dei mammiferi che può vivere nell'acqua")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere in {habitat}")

    case animale_inf if animale_inf["animale"] in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
        match animale_inf:
            case animale_inf if animale_inf["habitat"] == "terra" and animale_inf["animale"] in ["serpente", "tartaruga", "coccodrillo"] and animale_inf["habitat"] == "acqua":
                print(f"L'animale {animale} è uno dei rettili che può vivere nella terra e nell'acqua")
            case animale_inf if animale_inf["habitat"] == "terra":
                print(f"L'animale {animale} è uno dei rettili che può vivere sulla terra")

    case dict_animale if dict_animale["animale"] in ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]:
        match dict_animale:
            case dict_animale if dict_animale["animale"] in ["anatra", "cigno"] and dict_animale["habitat"] in ["aria", "terra", "acqua"]:
                print(f"{animale} è un {animal_type} che vive in acqua, cielo e terra")
            case dict_animale if dict_animale["animale"] in ["gallina", "tacchino"] and dict_animale["habitat"] == "terra":
                print(f"{animale} è un {animal_type} che vive su terra")
            case dict_animale if dict_animale["animale"] in ["aquila", "pappagallo", "gufo", "falco"] and dict_animale["habitat"] == "aria":
                print(f"{animale} è un {animal_type} che vive in aria")
            case _:
                print(f"non ho mai visto un {animale} in {habitat}")
    case dict_animale if dict_animale["animale"] in ["squalo", "trota", "salmone" ,"carpa"]:
        match dict_animale:
            case dict_animale if dict_animale["habitat"] == "acqua":
                print(f"{animale} è un {animal_type} che vive in acqua")
            case _:
                print(f"non ho mai visto un {animale} in {habitat}")
    case _:
        print("Errore. Dati non validi")






