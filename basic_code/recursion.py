#recursion for fibonaccy series
def fib(n):
    if (n==0):
        return 0
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
n = 10
print("Fibonacci series of 10 numbers is :",fib(10))
# for loop to print the fibonacci series.
for i in range(n+1): 
    print(fib(i),end=" ")

print('\n')
#Recussion for factorial calculation
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * fact(n - 1)
print('factorial of 5 is : ',fact(5))
print('\n')
for i in range(5):
    print(f'factorial of {i} is:',fact(i))

print('\n')
#Recurssion to reverse list
def reverseList(lst):
    if not lst:
        return []
    return [lst[-1]] + reverseList(lst[:-1])
print('Reversed list: ',reverseList([1, 2, 3, 4, 5]))

def perfect_number(n,i=1):
    if n<0:
        return False
    if i*i == n:
        print(f"{n} is a perfect number and {i} is its square root")
        return True
    elif i*i > n:
        print(f"{n} is not a perfect number")
        return False
    else:
        return perfect_number(n,i+1)        
perfect_number(10)