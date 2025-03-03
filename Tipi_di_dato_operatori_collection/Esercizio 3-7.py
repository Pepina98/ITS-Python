#Esercizio 3-7
names:list[str] = ["Matteo", "Rebecca", "Danilo", "Ilaria", "Camilla", "Lorenzo"]

print("I'm sorry, I just found out that the table dinner won't arrive in time so I can invite only two people")

guest1 = names.pop(0)
guest2 = names.pop(2)
guest3 = names.pop(2)
guest4 = names.pop(2)

print(f"I'm sorry {guest1}, I can't invite you to dinner\nI'm sorry {guest2}, I can't invite you to dinner\nI'm sorry {guest3}, I can't invite you to dinner\nI'm sorry {guest4}, I can't invite you to dinner")

print(f"{names[0]},you are still on my list so you are still invited\n{names[1]},you are still on my list so you are still invited")

del names [0]
del names [0]

print(names)