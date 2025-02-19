#Esercizio 4-10

numbers = [x**3 for x in range(1, 11)]
print(f"\nLa lista iniziale è {numbers}")

numbers[:3] # slicing: dall'elemento all'indice 0 (incluso) all'elemento all'indice 3 (escluso)
print(f"The first three items in the list are:{numbers[:3]}")

x = len(numbers)//2 
numbers[x-1:x+2]
print(f"The middle three items in the list are:{numbers[x-1:x+2]}")

numbers[-3:]
print(f"The last three items in the list are:{numbers[-3:]}")







 
