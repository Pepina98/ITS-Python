#Esercizio 6
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True or conditionB == True and conditionC == True:
        
        a = "Operazione permessa"
        return a
    
    else:
        b = "Operazione negata"
        return b
    