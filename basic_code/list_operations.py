
class ListOperations:
    def __init__(self,a):
        self.a = a

    def addelement(self,n):
        self.a.append(n)
        return self.a
    
    def insertelement(self,n):
        self.a.insert(4,n)
        return self.a
    
    def extendelement(self):
        self.a.extend([14, 15, 16])
        return self.a

    def popelement(self):
        self.a.pop()
        return self.a
    
    def removeelement(self,n):
        self.a.remove(n)
        return self.a

    def findlength(self):
        len = 0 
        for _ in self.a:
            len += 1
        return len

    def listcomp(self):
        new_list = [i for i in (self.a) if i%2==0]
        return new_list

    def sortlist(self):
        for i in range(len(self.a)):
            for j in range(i+1,(len(self.a))):
                if self.a[i]>self.a[j]:
                    self.a[i],self.a[j]=self.a[j],self.a[i]
        return self.a

    def findminmax(self):        
        print("min value is ", self.a[0])
        print("max value is ", self.a[-1])


    def findelement(self,n):
        for i in range(len(self.a)):
            if self.a[i]==n:
                print(f"{n} : element found")
                break
            elif self.a[i]!=n and i==len(self.a)-1:
                print(f"{n} : element not found")

    def reverselist(self,a):
        if not a:
            return []
        else:
            return [a[-1]] + (self.reverselist(a[:-1]))


def removeDuplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums


a=[8,5,10,9,4,2]
print('Initial list: ',a)
list_op = ListOperations(a)

added_list = list_op.addelement(3)
print('added_list: ',added_list)

inserted_list = list_op.insertelement(7)
print('inserted_list: ',inserted_list)

extended_list = list_op.extendelement()
print('extended_list: ',extended_list)

popped_list = list_op.popelement()
print('popped_list: ',popped_list)

removed_list = list_op.removeelement(7)
print('removed_list: ',removed_list)

length = list_op.findlength()
print('Length of the list: ' ,length)

new_list = list_op.listcomp()
print('comprehented list: ',new_list)

sort_list = list_op.sortlist()
print('Sorted list: ',sort_list)

list_op.findminmax()
list_op.findelement(5)
list_op.findelement(1)

reversed_list = list_op.reverselist(a)
print('reversed_list: ',reversed_list)

unique_list=removeDuplicates([1,7,8,4,5,9,8,1,4])
print(unique_list)