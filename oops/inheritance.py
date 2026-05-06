class Animal:
    def sound(self):
        print("Animal makes a sound") 
    def color(self):
        print("my color is black")

class Dog(Animal): 
    def voice(self):
        print("Dog barks")



#multilevel inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound") 
    def color(self):
        print("my color is black")

#multiple inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound") 
    def color(self):
        print("my color is black")

class Dog(Animal): 
    def voice(self):
        print("Dog barks")

#hierarchical inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound") 
    def color(self):
        print("my color is black")

class Dog(Animal): 
    def voice(self):
        print("Dog barks")

class Cat(Animal): 
    def voice(self):
        print("Cat meows")

class Bird(Animal): 
    def voice(self):
        print("Bird sings")


animal = Animal()
animal.sound()
dog=Dog()
dog.voice()
dog.sound()
dog.color()
cat=Cat()
cat.voice()
cat.sound()
cat.color()
bird=Bird()
bird.voice()
bird.sound()
bird.color()
