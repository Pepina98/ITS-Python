#ESercizio 10
reddito:float = float(input("Inserire il reddito familiare:"))
media:float = float(input("Inserire la media dei voti:"))

if reddito < 20000 and media > 27:
    print("Borsa di studio approvata")

else:
    print("Borsa di studio rifiuttata. Motivo: reddito o media insufficiente")
