#Esercizio 10
def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000
    
    for i in files:
        file_compresso:float = (i * 80) / 100 
        blocchi_usati = round(file_compresso /512)
        spazio_totale_blocchi = spazio_totale_blocchi -  blocchi_usati
        

        if blocchi_usati <= spazio_totale_blocchi:
            print(f"File di {i} byte compresso in {file_compresso} byte e memorizzato. Blocchi usati: {blocchi_usati}. Blocchi rimanenti: {spazio_totale_blocchi}.")
        
        else:
            print(f"Non è possibile memorizzare il file di {i} byte. Spazio insufficiente.")
            break
    
         
        
        
memorizza_file([1100, 20000, 1048576 ])







