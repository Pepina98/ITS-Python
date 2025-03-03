#Esercizio 3-6
names:list[str] = ["Rebecca", "Ilaria", "Camilla"]

names.insert(0, "Matteo")
names.insert(2, "Danilo")
names.append("Lorenzo")

print("I found a bigger dinner table")
print(f"{names[0]},would you want come to dinner?\n{names[1]},would you want come to dinner?\n{names[2]},would you want come to dinner?\n{names[3]},would you want come to dinner?\n{names[4]},would you want come to dinner?\n{names[5]},would you want come to dinner?")