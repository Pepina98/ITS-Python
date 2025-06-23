message:list = ["ciao", "come", "stai"]
def show_message() -> str:
    print(*message, sep= "\n")

show_message()
