#Esercizio 9
pi:float = 0
i:int = 1
count:int = 0

while True:
    if round(pi, 2) == 3.14:
        print(f"E' stato raggiunto il valore di 3.14, i termini necessari per raggiungere ciò sono stati: {count}")
        break
    else:
        pi = pi + (4/i)
        count += 1
        i += 2
        pi = pi - (4/i)
        count += 1
        i += 2

while True:
    if round(pi, 3) == 3.141:
        print(f"E' stato raggiunto il valore di 3.141, i termini necessari per raggiungere ciò sono stati: {count}")
        break
    else:
        pi = pi + (4/i)
        count += 1
        i += 2
        pi = pi - (4/i)
        count += 1
        i += 2

while True:
    if round(pi, 4) == 3.1415:
        print(f"E' stato raggiunto il valore di 3.1415, i termini necessari per raggiungere ciò sono stati: {count}")
        break
    else:
        pi = pi + (4/i)
        count += 1
        i += 2
        pi = pi - (4/i)
        count += 1
        i += 2

while True:
    if round(pi, 5) == 3.14159:
        print(f"E' stato raggiunto il valore di 3.14159, i termini necessari per raggiungere ciò stati {count}")
        break
    else:
        pi = pi + (4/i)
        count += 1
        i += 2
        pi = pi - (4/i)
