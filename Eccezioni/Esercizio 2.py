#Esercizio 2
def validate_password(password:str):
    count= 0
    j= 0
    for i in password:
        if i.isupper():
            count += 1
        elif i.isalnum():
            j += 1

    if len(password) >= 20 and count >= 3 and j >= 4:
        return print(True)
    else:
        raise Exception("Password errata")
    

validate_password("fj!o_fHbsdjiefledkoe?Osji?A")
    



