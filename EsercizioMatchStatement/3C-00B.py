#3C-00B
nome:str = str(input("Inserisci il nome:"))
genere:str = str(input("Inserisci il genere f per femmina e m per maschio:"))

match genere:

    case genere if genere == "f":
        print(nome)
        print("Femmina")

    case genere if genere == "m":
        print(nome)
        print("Maschio")

    case _:
        print("Errore, non è possibile generare un documento d'identità")