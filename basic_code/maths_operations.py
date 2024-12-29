# n =int(input("enter value of n: "))

def armstrong(n):
    m=n
    digits=[]
    no_digit=0
    while n!=0:
        digits.append(n%10)
        no_digit +=1
        n=n//10
    num=0    
    for i in digits:
        num +=i**(no_digit)
    if m==num:
        print('{} is a armstrong number'.format(m))
    else:
        print('{} is not a armstrong number'.format(m))
    return 0


def fact(n):
    fact_list = []
    for i in range(1,n+1):
        fact=1
        for j in range (1,i+1):
            fact = fact*j
        fact_list.append(fact)    
    return fact_list  


def fib(n):
    fib_list=[0,1]
    for i in range(2,n+1):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list


def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            print("{} is not a prime number".format(n))
            break
        elif n%i!=0 and i==(n//2):
            print("{} is a prime number".format(n))



# Extract the last digit using n % 10 and store it in rem.
# Build the reversed number: The rev_num is updated by multiplying the current value by 10 and adding the last digit (rem).
# Remove the last digit from n by performing integer division n //= 10
def palindrome(n):
    rev_num = 0
    num = n
    while n>0:
        rem = n%10
        rev_num = rev_num * 10 + rem
        n //=10
    if num == rev_num:
        print(f'{num} is a palindrome number')
    else:
        print(f'{num} is not a palindrome number')


def perfect_square(n):
    for i in range(n//2):
        if i*i == n:
            print(f"{n} is a perfect number and {i} is its square root")
            break
        elif i*i > n:
            print(f"{n} is not a perfect number")
            break

def pair_sum(arr,target):
    pair_dict = {}
    for val in arr:
        if val in pair_dict.values():
            return val,target-val
        else:
            pair_dict[val] = target-val
    return None

if __name__=='__main__':
    n =int(input("enter value of n: "))
    armstrong(n)
    fact_num=fact(n)
    # print(fact_num)
    fibo_list=fib(n)
    print(fibo_list)
    prime(n)
    palindrome(n)
    perfect_square(n)
    for i in range(1,n):
        j=i
        while i!=0:
            if i%10==4:
                print('Number {} consist 4 as a digit'.format(j))
                break
            i=i//10
    val1,val2=pair_sum([4,3,5,6],10)
    print(val1,val2)
