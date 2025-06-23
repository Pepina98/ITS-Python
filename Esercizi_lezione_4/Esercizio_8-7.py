def make_album(artist:str, title:str, song:int=None) ->dict:
    album:dict = {}

    album["artist"] = artist
    album["title"] = title
    if song != None:
        album["song"] = song
    return album


print(make_album("Pepina", "Chihuahua", 3))