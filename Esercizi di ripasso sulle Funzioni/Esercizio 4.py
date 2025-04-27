#Esercizio 4
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    voti1 = {}
    for i in voti:
        name = i["nome"]
        vote = i["voto"]

        if name in voti1:
            voti1[name].append(vote)
        else:
            voti1[name] = [vote]
                
            

            


                    
            

            
        


    return voti1
                
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
