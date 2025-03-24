#Esercizio 4.1
def recursiveSumInRange (a:int, b:int) -> int:
    if a > b:
        
        i:int = a
        a = b
        b = i

    if b == a:
        
        return int(a)
    
    else:
        
        return int(b + recursiveSumInRange(a, b-1))
    
print(recursiveSumInRange(10, 5))
print(recursiveSumInRange(5, 10))
