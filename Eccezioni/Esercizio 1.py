#Esercizio 1
def safe_sqrt(number:int):
    import math
    x = math.sqrt(number)

    return print(x) 

x = -2
if x < 0:
    raise Exception(f"The number should not negative.")

safe_sqrt(x)



