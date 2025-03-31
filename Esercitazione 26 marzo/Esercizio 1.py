#Esercizio 1 

def check_access (username:str, password:int, is_active: bool) -> str :
    
    if username == "admin" and password == 12345 and is_active == True:
        a = "Accesso consentito"
        return a

    else:
        b = "Accesso negato"
        return b
    
    
print(check_access("admin", 12345, True))

    


    
