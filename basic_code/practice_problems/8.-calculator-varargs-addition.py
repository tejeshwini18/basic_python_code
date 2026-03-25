"""Calculator class that adds variable number of arguments."""


class Calculator:
    def __init__(self):
        self.sum = 0

    def add(self, *args):
        for num in args:
            self.sum += num
        return self.sum


result = Calculator()
print(result.add(3, 5))
print(result.add(2, 5, 6))
