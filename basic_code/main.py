# count the number of occurances of character in given text
text = 'ython'
character = 'p'
count_dict = {}
for i in text:
    if i==character:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
print(count_dict)

def decorateor_func(func):
    def wrapper_func():
        print("wrapper_func worked")
        return func()
    print("decorator_func worked")
    return wrapper_func

@decorateor_func()
def show():
    print("show worked")

decorateor_show = decorateor_func(show)
decorateor_show()