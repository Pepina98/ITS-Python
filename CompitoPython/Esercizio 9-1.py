#Esercizio 9

def cambio_segno(target:str = "3.14"):
    pi:float = 0
    denominatore:int = 1
    segno: int = 1
    i = 0

    while True:

        pi += segno * (4/denominatore)
        segno *= -1
        denominatore += 2

        i += 1
    
        if str(pi)[:len(target)] == target:
            print(f"Il valore è stato raggiunto con {i} termini")
            break
  
cambio_segno(target = "3.14")
cambio_segno(target="3.141")
cambio_segno(target="3.1415")
cambio_segno(target="3.14159")