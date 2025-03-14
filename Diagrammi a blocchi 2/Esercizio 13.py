#Esercizio 13


while True:
    x:int = int(input("Inserire un valore per x che sia intero e positivo:"))
    y:int = int(input("Inserire un valore per y che sia intero e positivo:"))
    z:int = int(input("Inserire un valore per z che sia intero e positivo:"))

    if x > 0 and x % 1 == 0:
        if y > 0 and y % 1 == 0:
            if z > 0 and z % 1 == 0:
                    break
            
            else:
                print("z deve essere intero e positivo")
        else:
            print("y deve essere intero e positivo") 
    else:
        print("x deve essere intero e positivo")

if (x + y + z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
     print("Regole rispettate")

else:
     print("Regole non rispettate")


    