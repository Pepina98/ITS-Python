#Esercizio 2
def compoundInterest(m:float, t:int ) -> float:
    
    if t == 0:
        return m
    
    else:
        return float(1.005 * (compoundInterest(m, t -1)))
    
print(compoundInterest(9000,9))

#m * (1 + 1.005)**t