#Esercizio 6
def hypotenuse (cateto1: float, cateto2: float) -> float:
    if cateto1 > 0 and cateto2 > 0:
        ipotenusa  = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5
        return ipotenusa

print(hypotenuse(3.0, 4.0))