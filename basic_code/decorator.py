def decorator_func(func):
	def wrapper_func():
		print("wrapper_func Worked")
		return func()
	print("decorator_func worked")
	return wrapper_func

def show():
	print("Show Worked")

decorator_show = decorator_func(show)
decorator_show()


def sqr(n):
    for i in range(1, n+1):
        yield i*i 
a = sqr(3)  
print(next(a))
print(next(a))
print(next(a))


# list comprehension
odd_nums = [ i for i in range(10) if i%2]
print(odd_nums)
even_nums = [ i for i in range(10) if i%2==0]
print(even_nums)


#dict comprehension
sqr_dict = {n:n*n for n in range(1,10)}
print(sqr_dict)


# to get all dict keys
d = {'A': 1, 'B': 2, 'C': 3}
k = d. keys()
print([x for x in k])
for key in d:
    print(key)

# lambda function
square = lambda x : x * x
square(5) 


#nested for loop in list comprehension
one_square_cube = [i**j for i in range(1,4) for j in range(1,4)]
print(one_square_cube)