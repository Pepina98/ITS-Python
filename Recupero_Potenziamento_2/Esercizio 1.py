def isDNA(s:str) -> bool:
    DNA = 'AGCT'
    is_dna: bool = True

    for i in s:
        if i in DNA:
            continue
        else:
            is_dna = False

    return is_dna

def molecoledna(s1: str, s2:str) -> None:
    s1 = s1.upper()
    s2 = s2.upper()
