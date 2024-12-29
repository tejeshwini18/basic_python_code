from collections import Counter
import re
import string
from itertools import permutations


class Practice:

    def even_odd_length_word(self,s):
        self.s = s
        str_1=s.split()
        for word in str_1:
            if len(word)%2==0:
                print("even length word : ", word)    
            else:  
                print("odd length word : ", word)  

    def second_half_capital(self,s):
        self.s = s
        mid = len(s)//2
        first_str=s[:mid]
        second_str=s[mid:].upper()
        result_str=first_str+second_str
        print(result_str)               

    def first_last_capital(self,s):
        self.s=s
        str_1=s.split()
        l=[]
        for word in str_1:
            start=0
            end=len(word)-1
            if start==end:
                word_1 = word[start].upper()
            else:
                word_1 = word[start].upper()+word[1:end]+word[end].upper()
            l.append(word_1)
        print(l)   

    def avoid_space(self,s):
        # # Python3 code to demonstrate working of Avoid Spaces in Characters Frequency
        self.s = s
        print("The original s is : " + str(s))
        test_str=s.replace(' ','')
        res=len(test_str) 
        # printing result
        print("s after avoiding spaces : " , test_str)
        print("The Characters Frequency avoiding spaces : " + str(res))

    def remove_char_spec_pos(self,s):
        self.s=s
        # Removing char at pos 3 using slice + concatenation
        new_str = s[:2] + s[3:]
        print ("The s after removal of i'th character : " + new_str)

    def vowel_count(self, s):
        # Function to count vowels
        self.s = s
        count = 0
        # Creating a set of vowels
        vowel = set("aeiouAEIOU")

        # Loop to traverse the alphabet in the given s
        for alphabet in s:
            if alphabet in vowel:
                count = count + 1
        print("Number of vowels: ", count)

    def check_string(self,s):
        #checking special characters
        for c in s:
            if c in string.punctuation:
                print("string is not accepted")
                return
        print("string is accepted")

    def find_min_freq_char(self,s):
        self.s = s
        res = Counter(s)
        print(res)
        res = min(res, key = res.get) 
        # printing result 
        print ("The minimum of all characters in GeeksforGeeks is : " + str(res))
    
    def check(self,s):
        #accept the s only if all vowels are present
        self.s = s
        test_str = s.replace(' ', '')
        s_1 = test_str.lower()
        vowel = [s_1.count('a'), s_1.count('e'), s_1.count('i'), s_1.count('o'), s_1.count('u')]
    	# If 0 is present int vowel count array
        if vowel.count(0) > 0:
            print('not accepted')
        else:
            print('accepted')

    def commonfun(self,first_str,second_str):
        # Find the number of common characters between two ss.
        # First, convert both ss to sets and then find common characters.
        self.first_str = first_str
        self.second_str = second_str
        print('common words are : ',((set(first_str)).intersection(set(second_str))))
        print(len((set(first_str)).intersection(set(second_str))))
      
    def count_numbers(self,s):
        # Frequency of numbers in s
        self.s=s
        res=0
        for num in s:
            if(num.isdigit()):
                res+=1
        # printing result
        print("Count of numerics in s : " + str(res))

    def UncommonWords(self, A, B):
        # Python3 program to find a list of uncommon words
        self.A=A
        self.B=B
        A=A.split()
        B=B.split()
        x=[]
        for i in A:
            if i not in B:
                x.append(i)
        for i in B:
            if i not in A:
                x.append(i)
        x=list(set(x))
        print('uncommon words are :' ,x)

    # Python code to replace, with . and vice-versa
    def Replace(self,str1):
        arr = []        
        for i in str1:
            if (i == '.'):
                arr.append(', ')
            elif (i == ','):
                arr.append('.')
                continue
            elif (i == ' '):
                continue
            else:
                arr.append(i)
        str2 = ''.join(arr)
        print('result string:',str2)

    def allPermutations(self,str):        
        # Get all permutations of string 'ABC'
        permList = permutations(str)
        # print all permutations
        for perm in list(permList):
            print (''.join(perm))
	
    # Python code to find the URL from an input string
    def Find(self,s):
        x=s.split()
        res=[]
        for i in x:
            if i.startswith("https:") or i.startswith("http:"):
                res.append(i)
        print(res)

    def countfrequency(self,s):
        count_dict = {}
        for char in s:
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
        print(count_dict)

    def reversestring(self,s):
        my_str_list = s.split()
        rev_str = ''
        for word in my_str_list:
            for char in word:
                rev_str = char + rev_str 
        print('reversed string: ', rev_str)

    def isanagram(self,s1,s2):
        #anagram:when 2 strings contain same characters but in different order
        if sorted(s1)==sorted(s2):
            print('strings are anagram')
        else:
            print('strins are not anagram')


if __name__=='__main__':
    s = "I am working as a software engineer in TCS since 2021"
    p=Practice()
    p.even_odd_length_word(s)
    print('\n')
    p.second_half_capital(s)
    print('\n')
    p.avoid_space(s)
    print('\n')
    p.remove_char_spec_pos(s)
    print('\n')
    p.vowel_count(s)
    print('\n')
    p.first_last_capital(s)
    print('\n')
    p.find_min_freq_char(s)
    print('\n')
    p.check(s)
    print('\n')
    p.commonfun('TEJESHWINI','VIJYALAXMI')
    print('\n')
    p.count_numbers(s)
    print('\n')
    p.check_string('Geeks$For$Geeks')
    print('\n')
    p.UncommonWords('my name is Tejeshwini','Devesh is my brother')
    print('\n')
    p.Replace('You are beautiful, intelligent and awesome.So,I love the way you are.')
    print('\n')
    p.allPermutations('AB')
    print('\n')
    p.Find('My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/')
    print('\n')
    p.countfrequency('aaaabbbbbuuuuurrrrrhhhhtylwwwrro')
    print('\n')
    p.reversestring('I am a software engineer')
    print('\n')
    p.isanagram('heart','earth')
    print('\n')
    p.isanagram('me','mine')