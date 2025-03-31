#Esercizio 3
def rounded_average(numbers: list[int]) -> int:
    media = 0
    somma = 0

    for i in numbers:
        somma = somma + i 

    media = somma / len(numbers)
    

    return round(media)


numbers = [1, 2, 3, 4, 5]
print(rounded_average(numbers))



