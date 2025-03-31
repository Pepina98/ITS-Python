#Esercizio 9
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    return original_set - set(elements_to_remove)