def sandwiches(*args):
    for panino in args:
        for i, ingrediente in enumerate(panino, start=1): #permette di ottenere sia l'indice che il valore mentre si fa un ciclo for"
            print(f"{i} {ingrediente}")

print("Il primo panino è composto da:")
panino1:list = ["pomodoro", "mozzarella", "tonno"]
sandwiches(panino1)

print("Il secondo panino è composto da:")
panino2:list = ["prosciutto", "formaggio"]
sandwiches(panino2)

print("Il terzo panino è composto da:")
panino3:list = ["pollo", "insalata", "maionese"]
sandwiches(panino3)    


