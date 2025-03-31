#Esercizio 5
def sum_above_threshold(numbers: list[int], threshold: int) ->int:
    somma = 0

    for i in numbers:
        if i > threshold:
            somma = somma + i 

    return somma 

numbers = [1, 2, 3, 4, 5]
print(sum_above_threshold(numbers, 2))

