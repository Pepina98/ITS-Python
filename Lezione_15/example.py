'''
PATH: str = "Lezione_15/example.txt"
mode: str = "w"
encoding: str = "utf-8"

file = open(PATH, mode)

print(file)

message: str = "Hello, world!\n"
output: str = file.write(message)
print(message)
file.close()

'''

with open("Lezione_15/example.txt", "r") as file:
    print(file.read())

print("Hello, world!")

with open("Lezione_15/example.txt", "w") as file:
    print(file.write("Qualcosa"))


