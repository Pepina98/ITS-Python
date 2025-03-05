#Esercizio 8-7
def make_album(artist:str, album:str, song:int=None):
    music:dict[str, int] = {}
    music["artist"] = artist    
    music["album"] = album
    if song != None:
        music["songs"] = song

    return music

print(make_album("pokemon", "HeartGold"))
print(make_album("pokemon", "Platino"))
print(make_album("pokemon", "Smeraldo"))
print(make_album("pokemon", "HeartGold", 3))

