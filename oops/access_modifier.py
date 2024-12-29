class MyClass: 
    def __init__(self, public_value, protected_value, private_value): 
        self.public_value = public_value # Public attribute 
        self._protected_value = protected_value # Protected attribute 
        self.__private_value = private_value # Private attribute 
        
    def get_private_value(self): 
        return self.__private_value        
        
    def display_values(self): 
        print("Public: {}".format(self.public_value)) 
        print("Protected: {}".format(self._protected_value)) 
        print("Private: {}".format(self.__private_value)) 
            
            
# Creating an object of MyClass 
obj = MyClass("public", "protected", "private") # Accessing public attribute 
# obj.display_values()
print("Accessing public attribute directly:", obj.public_value) 
print("Accessing protected attribute directly:", obj._protected_value) 
# Accessing private attribute via getter method 
print("Accessing private attribute via getter:", obj.get_private_value()) # Modifying private attribute via setter method 
# This will fail 
print(obj.__private_value) 
