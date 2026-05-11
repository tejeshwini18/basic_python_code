class Student:

    def __init__(self):
        self._marks = 0

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value >= 0:
            self._marks = value
        else:
            print("Marks cannot be negative")


s = Student()

s.marks = 85
print(s.marks)