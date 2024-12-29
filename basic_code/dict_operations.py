#creation of dictionary using two lists
keys = ['name', 'age', 'gender']
values = ['John', 25, 'Male']
my_dict = dict(zip(keys, values))
print(my_dict)


# Iterate over keys
for key in my_dict:
    print(key)  

# Iterate over values
for value in my_dict.values():
    print(value)  

# Iterate over key-value pairs
for key, value in my_dict.items():
    print(key, value)  

print('Sorted')
sorted_dict={key:val for key,val in sorted(my_dict.items())}
print(sorted_dict)

# copying a dictionary
shallow_copy_dict = my_dict.copy()
deep_copy_dict = my_dict
print('shallow_copy_dict: ',shallow_copy_dict)
print('deep_copy_dict: ',deep_copy_dict)
my_dict['city'] = 'Pune'
print('my_dict: ',my_dict)
print('shallow_copy_dict: ',shallow_copy_dict)
print('deep_copy_dict: ',deep_copy_dict)


#merging two dictionaries
second_dict =  {'surname': 'Jackson', 'company': 'IBM', 'gender': 'Female'}
my_dict.update(second_dict)
print('Merged Dictionary: ',my_dict)
# merged_dict = {**my_dict, **second_dict}

dupl_dictionary =  {'name': 'John', 'age': 25, 'gender': 'Female', 'city': 'Pune', 'name': 'Jolly', 'city': 'Bengluru'}
print('Duplicate Dictionary: ',dupl_dictionary)


#dict comprehension
input_dict = {'product1':{'price':1,'quantity':20},
              'product2':{'price':2,'quantity':15},
              'product3':{'price':3,'quantity':20}}
output_dict = {key:val['price']*val['quantity'] for key,val in input_dict.items()}
print('output_dict: ',output_dict)


#finding max and min keys
max_key = max(output_dict, key=output_dict.get)
min_key = min(output_dict, key=output_dict.get)
print("max key: ",max_key)
print("min key: ",min_key)


#deletion
del my_dict['city']
print('my_dict_after_del: ',my_dict)

my_dict.pop('age')
print('my_dict_after_pop: ',my_dict)

my_dict.clear()
print('my_dict_after_clear: ',my_dict)
