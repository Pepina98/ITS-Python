#3C-002C
voto:int = int(input("Inserire voto di laurea compreso tra 66 e 110:"))

match voto:

    case voto if voto <= 110 and voto >= 106:
        print("4.0")

    case voto if voto <= 105 and voto >= 101:
        print("3.7")
    
    case voto if voto <= 100 and voto >= 96:
        print("3.3")

    case voto if voto <= 95 and voto >= 91:
        print("3.0")

    case voto if voto <= 90 and voto >= 86:
        print("2.7")

    case voto if voto <= 85 and voto >= 81:
        print("2.3")

    case voto if voto <= 80 and voto >= 76:
        print("2.0")

    case voto if voto <= 75 and voto >= 70:
        print("1.7")

    case voto if voto <= 69 and voto >= 66:
        print("1.0")

    case _:
        print("Voto non valido")


    
