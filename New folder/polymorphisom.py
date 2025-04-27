# Polymorphisom ka matlb hota hai ki ek same function hai but uska behaviour alag alag hai 
# Jaise ki ek ladka hai ghar par wo beta hai, School me wo student hai, dosto ke saath unka buddie hai

class Dog:
    def speak(self):
        return "Bark!"

class cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
Cat = cat()

# animal_sound(dog)
# animal_sound(Cat)

class Car:
    def move(self):
        print("Csr is driving on the road.")

class Airplan:
    def move(self):
        print("Airplane is flying in the sky.")

class Boat:
    def move(self):
        print("Boat is ssailing on the water.")

def start_moving(vehivle):
    vehivle.move()

car = Car()
boat = Boat()
airplan = Airplan()

start_moving(car)
start_moving(boat)
start_moving(airplan)