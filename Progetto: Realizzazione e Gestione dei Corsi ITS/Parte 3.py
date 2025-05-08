#Parte 3 
class Room:

    def __init__(self, id:str, floor:int, seats:int):
        self.id = id 
        self.floor = floor
        self.seats = seats
        self.area = seats * 2

    def get_id(self) -> str:
        return self.id
    
    def get_floor(self) ->int:
        return self.floor
    
    def get_seats(self) ->int:
        return self.seats
    
    def get_area(self) ->float:
        return self.area 

class Building:

    def __init__(self,name:str, address:str, floors: tuple):
        self.name = name
        self.address = address
        self.floors = floors 
        self.rooms = []

    def get_floors(self) -> int:
        return self.floors
    
    def get_rooms(self) -> int:
        return self.rooms

    def add_room(self, room: Room):
         
        if  room.get_floor() in self.floors and room not in self.rooms:
            self.rooms.append(room)

    def area(self) -> float:
        a = 0
        for i in self.rooms:
            a += i.get_area()
        
        return a 


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


class Course:

    def __init__(self, name:str):
        
        self.name = name
        self.groups = []

    def register(self, student: Student):
        
        for i in self.groups:
            if i.get_limit() > len(i.get_students):
                i.add_student(student)
                break 

    def get_groups(self):
        return self.groups
    
    def add_group(self, group : Group):
        self.groups.append(group)