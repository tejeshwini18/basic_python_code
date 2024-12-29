n = int(input("Enter the number of rows: "))  
for i in range(0, n):  
    for j in range(i, n):  
        print("* ", end="")         
    print()  

print('\n')
for i in range(0, n):  
    for j in range(0, i + 1): 
        if i>=j: 
            print("* ", end="")         
    print()  



