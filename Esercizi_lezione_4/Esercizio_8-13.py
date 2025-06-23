def build_profile(name:str, lastname:str,age:int, eyes:str, weight:str) -> str:
    return f'{name} {lastname}, age {age}, eyes {eyes}, weight {weight}'

print(build_profile("Rachele", "Corsi", 27, "brown", "1,65m"))
