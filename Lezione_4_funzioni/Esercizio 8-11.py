#Esercizio 8-11
mylist:list[str] = ["ciao", "hola", "hello", "halo", "hallo"]
sent_message:list[str] = []

def send_message(list, list2):
    for i in list:
        print(i)
        list2.append(i)
   

send_message(mylist, sent_message)
print(sent_message)
print(mylist)
