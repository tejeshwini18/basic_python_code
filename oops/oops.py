#Method Overloading
class MathOperations:
    def add(self,x,y):
        return x+y
    
    def add(self, x,y,z):
      return x+y+z 

#Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound") 
class Dog: 
    def sound(self):
        print("Dog barks")

# Creating objects 
math_ops = MathOperations()
# print(math_ops.add(3,5))
print(math_ops.add(3,5,4))

animal = Animal()
animal.sound()
dog=Dog()
dog.sound()
