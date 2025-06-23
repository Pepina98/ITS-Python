def make_album() ->dict:
    album:dict = {}

    while True:
        utente:str = str(input("Digitare si per aggiungere e no per terminare: "))

        if utente == "no":
            break
        elif utente == "si":
            artist:str = str(input("Inserire il nome dell'artista: "))
            title:str = str(input("Inserire il titolo dell'album: "))

            album[artist] = title
            print(album)
            
        else:
            print("La risposta inserita non è valida")
            continue
        
    

make_album()