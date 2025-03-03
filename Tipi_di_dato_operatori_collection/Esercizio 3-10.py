#Esercizio 3-10
Ilike:list[str]= ["Books", "Nature", "Animals", "Astronomy", "Juventus", "Fortine", "Sunflower", "Travel"]

Ilike.insert(3, "Food")
print(Ilike)

Ilike.append("Marvel")
print(Ilike)

Ilike.pop(3)
print(Ilike)

del Ilike[5]
print(Ilike)

print(sorted(Ilike))

print(sorted(Ilike)[::-1])

Ilike.reverse()
print(Ilike)

Ilike.sort()
print(Ilike)

Ilike.sort()
print(Ilike[::-1])