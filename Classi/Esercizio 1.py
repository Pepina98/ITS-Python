#Esercizio 1
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age 

bob = Person("Bob", 30) 
alice = Person ("Alice", 45)
edoardo = Person("Edoardo", 34)
claudio = Person("Claudio", 19)
rebecca = Person("Rebecca", 23)

people = [bob, alice, edoardo, claudio, rebecca]

if bob.age < alice.age:
    print(alice.name)
else:
    print(bob.name)

youngest = people[0]

for person in people:
    if person.age < youngest.age:
        youngest = person

print(youngest.name)
