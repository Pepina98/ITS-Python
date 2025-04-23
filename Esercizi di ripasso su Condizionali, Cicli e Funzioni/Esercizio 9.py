#Esercizio 9 
def rimbalzo() -> None:
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    
    while True:
        
        print(f"Tempo: {tempo} Altezza: {altezza}")
        altezza = altezza + velocita 
        velocita = velocita - 96
        tempo += 1

        if altezza < 0:
            altezza = altezza * -0.5
            velocita = velocita * -0.5
            rimbalzi += 1
            print(f"Tempo: {tempo} Rimbalzo!")
            tempo += 1
        
        if rimbalzi == 5:
            break

print(rimbalzo())
        