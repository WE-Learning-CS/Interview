class Vehicle():
    name = '운송수단'
    def move(self):
        print("움직임")
        
    
class Car(Vehicle):
    def move(self):
        print("차가 달림")
        
class Ship(Vehicle):
    def move(self):
        print("배가 움직임")
        


vehicle = Ship()
print(vehicle.name)
vehicle.move()