#Esercizio 2
def transform(x: int) -> int:
    if x % 2 == 0:
        x = x / 2 
        return x
    
    else:
        x = (x * 3) - 1
        return x


