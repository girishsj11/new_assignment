from abc import ABC,abstractmethod

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

'''
##ouput

Abstract class called !!
The German Scheford dog Pinky called automatically !
Pinky
The dog Pinky eats lot of food.
The dog Pinky Barks so aggressivly #

Process finished with exit code 0
'''
