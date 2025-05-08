#Esercizio 6
def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    return{"profile" : name, "email": email, "telefono": telefono}


def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    dictionary["profile"] = name
    if telefono != None:
        dictionary["telefono"] = telefono 
    if email != None:
        dictionary["email"] = email 

    return dictionary


contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))