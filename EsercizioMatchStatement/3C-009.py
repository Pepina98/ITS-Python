#3C-009
x:int = int(input("Inserire la coordinata x:"))
y:int = int(input("Inserire la coordinata y:"))

punto = (x, y)

match punto:

    case (0, 0):
        print("Il punto si trova nell'origine")

    case (x, 0):
        print("Il punto si trova sull'asse x")

    case (0, y):
        print("Il punto si trova sull'asse y")

    case (x, y) if x>0 and y>0:
        print("Il punto si trova sul primo quadrante")

    case (x, y) if x<0 and y>0:
        print("Il punto si trova nel secondo quadrante")

    case (x, y) if x<0 and y<0:
        print("Il punto si trova nel terzo quadrante")

    case (x, y) if x>0 and y<0:
        print("Il punto si trova nel quarto quadrante")

    case _:
        print("coordinate non trovate")


