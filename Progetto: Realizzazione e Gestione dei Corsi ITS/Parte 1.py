#Parte 1
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




    



