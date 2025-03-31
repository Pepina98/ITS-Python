#Esercizio 2
def countdown(n:int) -> int:
    while n > 0:
        print(n)
        n -=1
    
    return n

print(countdown(5))