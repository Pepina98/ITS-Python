#3C-00C
voto:int = int(input("Inserire un voto da 1 a 10:"))

match voto:

    case 10:
        print("Eccellente")

    case 9 | 8:
        print("Molto buono")

    case 7 | 6:
        print("Sufficiente")

    case 5 | 4:
        print("Insufficiente")

    case 3 | 2 | 1:
        print("Gravemente insufficiente")

    case _:
        print("Voto non valido")