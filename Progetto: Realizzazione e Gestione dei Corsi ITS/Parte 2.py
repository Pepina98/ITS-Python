#Parte 2
class Person:
    def __init__(self, cf:str, name:str, surname:str, age:int):

        self.cf = cf
        self.name = name
        self.surname = surname 
        self.age = age


class Student(Person):
    def __init__(self, cf, name, surname, age):
        self.group = None
        super().__init__(cf, name, surname, age)

    def set_group(self, group):
        self.group = group


class Lecturer(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)


class Group:
    def __init__(self, name:str,limit:int):
        
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []

    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):
        limite_prof = 1
        if len(self.students) > 10:
            limite_prof = len(self.students) // 10 
        return limite_prof
    
    def add_student(self, student: Student):
        if self.limit > len(self.students):
            self.students.append(student)

    def add_lecturer(self,lecture: Lecturer):
        if self.get_limit_lecturers() > len(self.lecturers):
            self.lecturers.append(lecture)

    
