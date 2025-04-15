#La tartaruga e la lepre
import random
tarta = 1
lep = 0

def tartaruga ():
    
    x = random.randint(1,10)
    print(x)

    if x >= 1 and x<= 5:
        tarta += 3 
    
    if x >=6 and x <= 7:
        tarta -= 6

    if x >= 8 and x >= 10:
        tarta += 1 

    

    

def lepre ():

    y = random.randint(1,10)
    print(y)

    if y >= 1 and y<= 2:
        lep += 0

    if y >= 3 and y <= 4:
        lep += 9

    if y == 5:
        lep -= 12

    if y >= 6 and y <= 8:
        lep += 1

    if y >= 9 and y <= 10:
        lep -= 2

    







