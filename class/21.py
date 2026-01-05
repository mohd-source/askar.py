from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        return "Moving"



class Dog(Animal):
    @property
    def make_sound(self):
        return "bhow"
    

class Cat(Animal):
    @property
    def make_sound(self):
        return "meow"
        

dog = Dog()
cat = Cat()


print(cat.make_sound)