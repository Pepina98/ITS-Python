class ContactManager:

    def __init__ (self):
        self.contacts:dict[str, list[str]] = {}

    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
        new_contacts:dict = {}
        new_contacts[name] = phone_numbers 

        if name not in self.contacts.keys():
            self.contacts[name] = phone_numbers
        
        else:
            raise ValueError("Errore: il contatto esiste già.")
        

        return new_contacts


    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        new_phone_number :dict ={}
        
        if contact_name not in self.contacts.keys():
            raise ValueError("Errore: il contatto non esiste.")
        
        elif phone_number in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono esiste già.")
        
        else:
            self.contacts[contact_name].append(phone_number)
            new_phone_number[contact_name] = self.contacts[contact_name]
            return new_phone_number
    
    
    def remove_phone_number(self, contact_name: str, phone_number:str) -> dict[str, list[str]]:

        if contact_name not in self.contacts.keys():
            raise ValueError("Errore: il contatto non esiste.")
        
        elif phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono non è presente.")
        
        else:
            self.contacts[contact_name].remove(phone_number)
            new_remove_phone_number:dict = {}
            new_remove_phone_number[contact_name] = self.contacts[contact_name]
            return new_remove_phone_number
        
    def update_phone_number(self, contact_name:str, old_phone_number: str, new_phone_number:str) -> dict[str, list[str]]:

        if contact_name not in self.contacts.keys():
            raise ValueError("Errore: il contatto non esiste.")
        
        elif old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono non è presente.")
        
        else:
            self.contacts[contact_name].remove(old_phone_number)
            self.contacts[contact_name].append(new_phone_number)
            new_update_phone_number:dict = {}
            new_update_phone_number[contact_name] = self.contacts[contact_name]
            return new_update_phone_number
        
    
    def list_contact(self) -> list:
        new_list_contact:list = []
        for key in  self.contacts.keys():
            new_list_contact.append(key)
        
        return new_list_contact
    
    def list_phone_numbers(self, contact_name:str) -> list:
        new_list_phone_numbers:list = []

        if contact_name not in self.contacts.keys():
            raise ValueError("Errore: il contatto non esiste.")
        
        else:
            for value in self.contacts[contact_name]:
                new_list_phone_numbers.append(value)
            
            return new_list_phone_numbers
        
    def search_contact_by_phone(self, phone_number: str) -> list:
        new_search_contact_by_phone : list = []

        for key, phone_number in self.contacts.items():
            if phone_number in self.contacts[key]:
                new_search_contact_by_phone.append(key)

            else:
                raise ValueError("Nessun contatto trovato con questo numero di telefono.")

        return new_search_contact_by_phone



