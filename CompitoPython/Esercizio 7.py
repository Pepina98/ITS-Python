#Esercizio 7
a:list = [1, 2, 3, 4, 5]
b:list = [6, 7, 8, 9, 10]
c:list = []

somma1 = (a[0] + b[1])
c.append(somma1)

somma2 = (a[1] + b[2])
c.append(somma2)

somma3 = (a[2] + b[3])
c.append(somma3)

somma4 = (a[3] + b[4])
c.append(somma4)

somma5 = (a[4] + b[0])
c.append(somma5)

print(c)
