import random


text = '''Hello! How are you doing?
I am doing great!
Who are you?
My name is Kaustubh
Student of RNSIT
Cool!'''


file1 = open('my_file.txt', 'r')
print(file1.read())
file1.close()

file2 = open('FileText1.txt', 'w')
file2.write('This is the first line' + '\n\n')
file2.write(text)
file2.write('\n\n' + 'This is the last line \n\n')
file2.close()

for i in range(100):
    file3 = open('FileText1.txt', 'a')
    file3.write(str(i)+'\n')
    file3.close()

file3 = open('FileText2.txt', 'w')
file3.write('\n\n')
file3.close()

for i in range(100):
    with open('FileText2.txt', 'a') as file4:
        file4.write(str(i*10)+'\n')

# Random Module
random_numbers_1 = [random.random() for i in range(5)]
print("Random Numbers Set 1:", random_numbers_1)
random_numbers_2 = [random.random() for i in range(5)]
print("Random Numbers Set 1:", random_numbers_2)

random.seed(10)
new_random_numbers_1 = [random.random() for i in range(5)]
print("Random Numbers Set 1:", new_random_numbers_1)
random.seed(10)
new_random_numbers_2 = [random.random() for i in range(5)]
print("Random Numbers Set 2:", new_random_numbers_2)

names = [ 'Akhilesh', 'Animikh', 'Akshay', 'Akshata', 'Ipsita', 'Ksuhal', 'Vishwas']
# Completely Random
for i in range(10):
    print(random.choice(names))
print()

# Random but same series every time
random.seed(10)
for i in range(10):
    print(random.choice(names))
print()

# Same name every time
for i in range(10):
    random.seed(10)
    print(random.choice(names))
print()



