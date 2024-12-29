import random

rand_variable = random.randrange(0,101)

upper_bound = rand_variable // 10 * 10 + 10
lower_bound = rand_variable // 10 * 10
# print(rand_variable)
# print(upper_bound)
# print(lower_bound)
def check_random_number(user_input):
    if rand_variable == user_input:
        return True
    else:
        return False
        
user_input = int(input("enter your number: "))
a = check_random_number(user_input)
if a:
    print("your guess is correct!!")
else:    
    for i in range(2):
        if 0 <= rand_variable < 100:
            if i==0:
                print("here is a hint for you")
                print(f"actual number belongs to this range {rand_variable // 10 * 10} to {rand_variable // 10 * 10 + 10}")
            user_input = int(input("You can again enter your number: "))
            a=check_random_number(user_input)
            if a:
                print("your guess is correct!!")
                break
            else:
                print("incorrect guess")