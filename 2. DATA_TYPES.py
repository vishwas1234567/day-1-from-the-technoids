# Strings
str1 = 'Hello world'
str2 = "My name is Akshay"
str3 = '''This is an example for intialization of strings'''
type(str1)
print(str1)
print(str2)
print(str3)

# Accessing Strings
print(str1[6])
print(str2[-1])

#immutable
str2[3] = 'h'

#Slicing
print(str1[:-1])
print(str1[:])
print(str2[3:])
print(str3[::2])
print(str1[::-1]) # reverse a string

# concatenation
new_str = str1+' '+str2
print(new_str)
print(new_str*2)

#built in functions in string
lower_string = new_str.lower()
print(lower_string)
lower_string.count('m')

# Lists
ls1 = [10,-4,25,13]
print(ls1)
ls2 = ["tiger","lion", "cheetah"]
print(ls2)
mixed_list = [3.5,"tiger",10,[3,4]]
print(mixed_list)
type(mixed_list)
ls3 = list("hello")
print(ls3)

#Accessing list
ls = [1,2,3,4,5]
print(ls[3])
mixed_list = [1,2,3,[4,5],[6,7]]
print(mixed_list[3][1])
print(mixed_list[-1])
3 in mixed_list
4 in mixed_list
[4,5] in mixed_list

#Mutable
ls = [1,2,3,[4,5],[6,7,8]]
ls[0] = 99
ls[3][1] = 100
print(ls)

# list concatenation
ls1=[1,2,3]
ls2=[4,5,6]
ls3=ls1+ls2
print(ls3)

#mutliplying the list with a number
ls = [1,2,3,4]
print(ls*2)

#List Slices
ls=[3,'hi',[2,3],2.3,-3]
print(ls[:])
print(ls[1:])
print(ls[:3])
print(ls[-1])
print(ls[1:4])

#Append
ls=['hi','how','are']
ls.append('u?')
print(ls)

#Extend
ls1=[1,2,3]
ls2=[5,6,7]
ls1.extend(ls2)
print(ls1)

#Sorting
ls=[18,12,56,13,61]
ls.sort()
print(ls)

ls.sort(reverse=True)
print(ls)

#Insert
ls=[1,2,4]
ls.insert(2,3)
print(ls)

#clear
ls=[1,2,3,4]
print(ls)
ls.clear()
print(ls)

#Deleting
ls=[53,27,71,19,36]
x=ls.pop()
print(ls)
print(x)

y=ls.pop(2)
print(ls)
print(y)

ls.remove(53)
print(ls)

del ls[1]
print (ls)

#list functions
ls=[23,25,57,18,22]
max(ls)
min(ls)
sum(ls)
len(ls)

#split and join
str='How you doing'
ls=str.split()
print(ls) 

str='1576/4345/2221'
ls=str.split('/')
print(ls)

ls=['How','are','you?']
d=' '
d.join(ls)


#Dictionaries
legends={'Cricket':'Sachin','Football':'Pele','Basketball':'Jordan'}
print(legends)
print(legends.keys())
print(legends.values())
print(legends.items())

# in operator in dictionaries
'Cricket' in legends
"Sachin" in legends
"Sachin" in legends.values()

# get() in dictionaries
print(legends.get("Cricket",0))
print(legends.get("Snooker","N/A"))

# accessing dictionary elements
legends["Cricket"] = "M.S. Dhoni"
print(legends)

# to find frequency of characters in a sentence
text = input("Enter a sentence: ")
text = text.lower()
text = list(text)
dic = {}
for char in text:
    dic[char] = dic.get(char,0) + 1
print(dic)