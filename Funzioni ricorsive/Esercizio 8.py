#Esercizio 8
def vowelsCounter(s:str)-> int:

    if not s:
        return 0
    
    if s[0].lower() in ["a","e","i","o","u"]:
        return 1 + vowelsCounter(s[1:])
    
    else:
        return 0 + vowelsCounter(s[1:])
    
print(f'La stringa \"\" contiene {vowelsCounter(" ")} vocali')
print(f'La stringa \"\" contiene {vowelsCounter("ciao")} vocali')
