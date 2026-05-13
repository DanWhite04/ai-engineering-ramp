import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hi I'm {self.name}")
    
    def describe(self):
        print(f"{self.name} is {self.age} years old")
        
        

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def greet(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def greet(self):
        print(f"{self.name} says Meow!")

def main():
    rex = Dog("Rex", 4, "Labrador")
    mala = Cat("Mala", 10, True)
    rex.describe()
    rex.greet()
    mala.describe()
    mala.greet()



if __name__ == "__main__":
    main()
