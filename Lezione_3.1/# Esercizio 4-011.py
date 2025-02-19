# Esercizio 4-11

my_pizzas = ["Margherita", "Diavola", "Capricciosa"]

friends_pizzas = ["Quattro formaggi", "Marinara", "Boscaiola"]

my_pizzas.append ("Bianca")
print(my_pizzas)

friends_pizzas.append ("Verdure")
print(friends_pizzas)

if my_pizzas == friends_pizzas:
    print("Le liste sono uguali")
else:
    print("Le liste sono diverse")

print("My fav pizzas are:")
for pizza in my_pizzas:
    print(pizza)
    
print("My friend's fav pizzas are:")
for pizza in friends_pizzas:
    print(pizza)