#3C-005
user:dict = {"nome": input("Digitare il nome dell'utente:"), "ruolo": input("Digitare il ruolo dell'utente:"), "età": int(input("Digitare l'età dell'utente:"))}

match user:

    case {"nome": name, "ruolo": "Admin", "età": età}:
        print("Accesso completo a tutte le funzionalità")

    case {"nome": name, "ruolo": "Moderatore", "età": età}:
        print("Può gestire i contenuti ma non modificare le impostazioni")

    case {"nome": name, "ruolo": "Utente", "età": età} if user["età"] >= 18:
        print("Accesso standard a tutti i servizi")

    case {"nome": name, "ruolo": "Utente", "età": età} if user["età"] < 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate")

    case {"nome": name, "ruolo": "Ospite", "età": età}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti")

    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!") 
