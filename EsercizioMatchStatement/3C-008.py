#3C-008
frase:str = str(input("Inserire una frase di una riga:"))

match frase:

    case frase if frase[-1] == "?" and len(frase) %2 == 0:
        print("Sì")

    case frase if frase[-1] == "!" and len(frase) %2 != 0:
        print("No")

    case frase if frase[-1] == "!":
        print("Wow!")

    case _:
        print(f'Tu dici "{frase}"')

