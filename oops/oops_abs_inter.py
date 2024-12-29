from abc import ABCMeta, abstractmethod

class Animal(ABCMeta): 
    def __init__(self, name): 
        self.name = name 
    
    @abstractmethod 
    def speak(self): 
        pass 
        
class Dog(Animal): 
    def __init__(self, name, breed): 
        super().__init__(name) 
        self.breed = breed 
    def speak(self): 
        print("My name is {}".format(self.name))
        return 0

class Cat(Animal): 
    def __init__(self, name, color): 
        super().__init__(name) 
        self.color = color 
    def speak(self): 
        print("I says meow : {} ".format(self.name))
        return 0 
            
# Trying to instantiate Animal will raise an error 
# This will raise a TypeError 
animal = Animal("Unknown") 
    
# Creating objects 
dog = Dog("Buddy", "Golden Retriever") 
print(dog.speak()) 

cat = Cat("Whiskers", "Gray")
print(cat.speak())