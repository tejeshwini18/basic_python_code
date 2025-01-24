# Print 1-50 - Make a list
# If divisible by 3, 5, 15
# 3 - foo
# 5 - bar
# 15 - hello
results = []
for i in range(1,51):
    if i%3==0 and i%5==0:
        results.append('hello')
    elif i%3==0:
        results.append('foo')
    elif i%5==0:
        results.append('bar')
    else:
        results.append(i)
print(results)

# “I like to learn new things”
# Create dict of individual words as keys with their lengths as values
# {“I”:1, “like”:4, “to”:2, “learn”:5, “new”:3, “things”:6}
str1 = "I like to learn new things"
str_list = str1.split()
len_dict ={}
for word in str_list:
    len_dict[word]=len(word)
print(len_dict)


def decorator_func(func):
    def wrapper_func():
        print("wrapper_func worked")
        return func()
    print("decorator_func worked")
    return wrapper_func
def show():
    print("show worked")
decorator_show = decorator_func(show)
decorator_show()

# AAAABBBBCCCAAADDDDEEF
# A4B4C3A3D4E2F
def compress_string(input_str):
    if not input_str:
        return ""   
    compressed = []
    count = 1
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            compressed.append(f"{input_str[i - 1]}{count}")
            count = 1
    # Add the last character and its count
    compressed.append(f"{input_str[-1]}{count}")    
    return ''.join(compressed)
result_str = compress_string('AAAABBBBCCCAAADDDDEEF')
print(result_str)

# Program to flatten the list
# Input: l1 = [1,[2,3, [4, 5]]]
# Output: l1 = [1,2,3,4,5]
def flatten_list(a):
    out_list = []
    for i in a:
        if isinstance(i,list):
            out_list.extend(flatten_list(i))
        else:
            out_list.append(i)
    return out_list
input_list = [1,[2,3, [4, 5]]]
output_list = flatten_list(input_list)
print(output_list)

# sentence = "Python programming is amazing for data analysis"
# Longest even length word from sentence
sentence = "Python programming is amazing for data analysis"
word_list = sentence.split()
len_dict={}
for word in word_list:
    if len(word)%2==0:
        len_dict[word] = len(word)
print(len_dict)
longest_word = max(len_dict,key=len_dict.get)
print(longest_word)

# 111 --> 1
# 1231 --> 123
# 1112 --> 12
# 1261 --> 126
def remove_duplicate(a):
    unique_a = ''
    for char in a:
        if char not in unique_a:
            unique_a += char
    return unique_a
in_a = '1231'
out_a = remove_duplicate(in_a)
print(out_a)

# case1: add(3,5)
# sum = 8
# case 2: add(2,5,6)
# sum = 21
class Calculator:
    def __init__(self):
        self.sum = 0
    def add(self,*args):
        for num in args:
            self.sum += num
        return self.sum
result = Calculator()
print(result.add(3,5))
print(result.add(2,5,6))

even_numbers = ['even' if i%2==0 else 'odd' for i in range(11)]
print(even_numbers)

'''We have a table called BookAuthor. 
It has two columns Book and Author, Book being unique column. 
Write a query to find the names of the authors who have written more than 10 books.
"select author from BookAuthor GROUP BY author having COUNT(book)>10"
'''

'''Django ORM Queries
Model - BookAuthor
BookAuthor.objects.all()
BookAuthor.objects.filter(author='')
BookAuthor.objects.get(book='')
BookAuthor.objects.get(book='').delete()
up_data = BookAuthor.objects.get(book='')
up_data.author = ''
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.p1 = None  
        self.p2 = None  
        self.children = []  

    def set_parent(self, p1):
        self.p1 = p1
        if p1.p2 is None:
            p1.p2 = self
        else:
            current = p1.p2
            while current.p2 is not None:
                current = current.p2
            current.p2 = self

        p1.children.append(self)


def print_node_without_parent_sibling(root_node):
    if root_node is None:
        return []

    visited = [root_node]  
    
    while visited:
        current_node = visited.pop()

        has_no_children = len(current_node.children) == 0
        has_no_siblings = (current_node.p1 is None) or (current_node.p1.p2 == current_node)

        if has_no_children and has_no_siblings:
            print(current_node.value)

        for child in current_node.children:
            visited.append(child)

# Create nodes
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")
j = Node("J")
k = Node("K")
l = Node("L")
m = Node("M")
n = Node("N")
o = Node("O")
p = Node("P")

# Set parent-child relationships
b.set_parent(a)
c.set_parent(b)
d.set_parent(c)
e.set_parent(d)
f.set_parent(b)
g.set_parent(f)
h.set_parent(c)
k.set_parent(h)
i.set_parent(d)
j.set_parent(e)
l.set_parent(j)
m.set_parent(l)
n.set_parent(m)
o.set_parent(l)
p.set_parent(o)

print_node_without_parent_sibling(a)
