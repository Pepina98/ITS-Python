#ESercizio 2
class Student:
    
    def __init__(self, name:str, studyProgram: str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"{self.name}, {self.studyProgram}, {self.age}, {self.gender}")

rachele = Student("Rachele", "Cyber Security", 27, "Cornetto alla nutella")
edoardo = Student("Edoardo", "Cyber Security", 6, "Papà Pig")
claudio = Student("Claudio", "Cyber Security", 19, "Motosega" )

rachele.printInfo()
edoardo.printInfo()
claudio.printInfo()

