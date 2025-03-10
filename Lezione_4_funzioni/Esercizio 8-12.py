#Esercizio 8-12

def sandwiches (*args):
    for i in args:
        print(*i, sep = "\n")

print("Il primo panino è composto da:")
panino1:list = ["pomodoro", "mozzarella", "tonno"]
sandwiches(panino1)

print("Il secondo panino è composto da:")
panino2:list = ["prosciutto", "formaggio"]
sandwiches(panino2)

print("Il terzo panino è composto da:")
panino3:list = ["pollo", "insalata", "maionese"]
sandwiches(panino3)

 







             



        
