class Animal:
    def sound(self):
        print("Animal makes a sound") 
    def color(self):
        print("my color is black")

class Dog(Animal): 
    def voice(self):
        print("Dog barks")

animal = Animal()
animal.sound()
dog=Dog()
dog.voice()
dog.sound()
dog.color()