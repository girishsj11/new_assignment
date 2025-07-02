from abc import ABC,abstractmethod
'''
class Dog(ABC):
    def __init__(self):
        print("Abstract class called !!")

    @abstractmethod
    def bark(self):
        print("The Dogs Barks normally !")


class German_Scheford(Dog):
    def __init__(self,name):
        super().__init__()
        self.name = name
        print(f"The German Scheford dog {self.name} called automatically !")

    def bark(self):
        print(f"The dog {self.name} Barks so aggressivly #")

    def eat(self):
        print(f"The dog {self.name} eats lot of food.")

Dog1 = German_Scheford("Pinky")
print(Dog1.name)
Dog1.eat()
Dog1.bark()


##ouput

Abstract class called !!
The German Scheford dog Pinky called automatically !
Pinky
The dog Pinky eats lot of food.
The dog Pinky Barks so aggressivly #

Process finished with exit code 0
'''

class Vehicle(ABC):
    def __init__(self):
        print("Vehicle class called ")

    @classmethod
    @abstractmethod
    def wheels(cls):
        print("Depends on the vehicle type , the wheel allignment & number differs")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("Car class called ")

    def wheels(self):
        super().wheels()
        print("Car has 4 wheels in it")

class TataCurve(Car):
    def __init__(self):
        super().__init__()
        print("Tata car class called ")

    def wheels(self):
        super().wheels()
        print("Tata car 4 wheels with 1 extra wheel at the bumper side ")

    def display(self):
        print("In Tata curve car the display runs smoother")

tata1 = TataCurve()
tata1.wheels()
tata1.display()

'''
#output - 
/usr/bin/python3.10 /home/giri/Desktop/Programs/new_assignment/abstract.py 
Vehicle class called 
Car class called 
Tata car class called 
Depends on the vehicle type , the wheel allignment & number differs
Car has 4 wheels in it
Tata car 4 wheels with 1 extra wheel at the bumper side 
In Tata curve car the display runs smoother

Process finished with exit code 0
'''

