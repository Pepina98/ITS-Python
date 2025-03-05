#Esercizio 8-9
mylist = ["ciao", "hola", "hello", "halo", "hallo"]

def show_messages():
    print(*mylist, sep = "\n")

show_messages()