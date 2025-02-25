#Esercizio 3C-00A

numero_nati = int(input("Inserisci un numero:"))

match numero_nati:

    case 1:
        print("Congratulazioni!")
        
    case 2:
        print("Wow! Gemelli!")
    
    case 3:
        print("Wow! Tre!")

    case 4:
        print("Mamma mia quattro! Wow!")
    
    case 5:
        print("Incredibile! Cinque!")
    
    case _:
        print(f"Non ci credo! {numero_nati} bambini!")

    

    

