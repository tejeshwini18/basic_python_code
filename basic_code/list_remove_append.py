"""
Let's imagine a situation: you went to the market and filled your baskets (basket1 and basket2) with fruits. You wanted to have one of each kind but realized that some fruits were put in both baskets.

Task 1. Your first task is to remove everything from basket2 that is already present in basket1.
Task 2. After the removal it is reasonable to anticipate that one of the baskets might weigh more compared to the another (all fruit kinds weight the same). Therefore, the second task is to transfer some fruits from a heavier basket to the lighter one to get approximately the same weight/amount of fruits.
"""


# Remove fruits from basket2 that are present in basket1
basket1 = ['apple', 'banana','orange','grapes','water melon','papaya']
basket2 = ['apple', 'banana','orange','ananas','custurd apple']

#TASK 1
for item in basket1:
    if item in basket2:
       basket2.remove(item)
print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))

#TASK 2
for item in basket1:
  if len(basket1)>len(basket2):
    basket2.append(item)
    basket1.remove(item)

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))