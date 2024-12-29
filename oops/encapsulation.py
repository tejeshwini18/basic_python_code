# Encapsulation and Abstraction 
class Introduction: 
    def __init__(self, name, gender): 
        self._name = name # Encapsulated attribute 
        self._gender = gender # Encapsulated attribute 
    def get_details(self): 
        # Abstraction through method 
        print("{} is a {}".format(self._name,self._gender))
        return 0

intro = Introduction("Devesh","Male")
intro.get_details()
