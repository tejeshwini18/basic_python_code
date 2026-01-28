

import string

# Base class
class BaseProcessor:
    def __init__(self):
        pass

    # Method to remove punctuation from a string
    def remove_punctuation(self, input_string):
        punc_list = ['.','!','?',',',';',':','-','=','""']
        res_string = ''
        for char in input_string:
          if char not in punc_list:
            res_string += char
        return res_string

# Inherited class
class AdvancedProcessor(BaseProcessor):
    def __init__(self):
        ### Complete the initialisation of base class
        pass

    # Method to check if a number is prime
    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Method to filter prime numbers from a list
    def filter_primes(self, num_list):
        list_prime_num = []
        for num in num_list:
          prime_num = self.is_prime(num)
          if prime_num:
            list_prime_num.append(num)
        return list_prime_num


processor = AdvancedProcessor()

#Task 1: Instantiate Base class init method from processor object.
processor.__init__()

#Task 2: Test remove_punctuation method
test_string = "Hello, World! This is a test-string."
print("Original String:", test_string)
print("Without Punctuation:", processor.remove_punctuation(test_string))


#Task 3: Test Filter method : Call is_prime method from filter_primes
test_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Original List:", test_list)
print("Prime Numbers:", processor.filter_primes(test_list))