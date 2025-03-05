#Esercizio 8-8
def make_album():
    music:dict[str, int] = {} 
    while True:
        utente:str = str(input("Inserisci si per aggiungere o no per terminare:"))
        if utente == "no":
            break
        elif utente == "si":
            artist:str = str(input("Inseriscci il nome dell'artista:"))
            album:str = str(input("Inserisci il nome dell'album:"))
            music[artist] = album

        else:
            print("Risposta non valida")
            
            continue

    return print(music)
    
make_album()



