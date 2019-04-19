# Program for finding the frequency of words in a text file 
#and number of lines and number of characters
import string
fhand = open("ML_algo.txt","r")
char_count = 0
line_count = 0
dic = {}
for line in fhand:
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    line_count += 1
    char_count += len(line)
    for words in line.split():
        dic[words] = dic.get(words,0)+1
fhand.close()
print("Number of lines in the file = ",line_count)
print("Number of characters in the file = ",char_count)
print("The words with their frequency")
print(dic)

#Program to print the first 10 lines and last 10 lines of a file
file1 = open("Elon_Musk.txt","r")
text = file1.read().split('\n')
print('The first 10 lines are ' )
for lines in text[:10]:
    print(lines)
print('\n\n')
print('The last 10 lines are ' )
for lines in text[-10:]:
    print(lines)





#To find the prime numbers in the specified range
a,b = int(input("Enter the starting limit: ")), int(input("Enter the ending limit: "))
ls = []
for i in range(a,b+1):
    fact = 0
    for j in range (1,i+1):
        if i%j ==0:
            fact +=1
    if fact == 2:
        ls.append(i)
print("The prime numbers in the given range {} , {} are: ".format(a,b))
print(ls)





#Function to rotate the given list n number of times based on user input
def rotatelist (n,ls):
    for i in range (n):
        x = ls.pop()
        ls = [x]+ls
    return ls
lis = [1,2,3,4]
rot_lis = rotatelist(5,lis)
print(rot_lis)
    





#Function to return True when the list is in ascending order else return False
def isAscending (ls):
    for i in range(len(ls)-1):
        if ls[i]>ls[i+1]:
            return False
    return True
res1 = isAscending([1,2,3,4])
res2 = isAscending([2,1,5,3,7])
print(res1)
print(res2)