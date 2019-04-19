# A Python program to demonstrate that we can store
# large numbers in Python
# Range of int -32768 to 32767
x = 10000000000000000000000000000000000000000000
x = x + 1
print(x)
print(type(x))
print(100 ** 100)

# User Input
print('Hey! Enter some text: ')
x = input()
print('Text entered is: ', x)
print('Type:', type(x))

# print and user Input
print("Hello!")
x = input("Hi! Tell me your name: ")
print("Hi, nice to meet you,", x)
y = input("What is your email? :")
print("Oh! Your email ID is:", y)
z = input("What is your Phone Number? :")
print("Oh! Your Phone Number is:", z)

# Important Concepts
print("A\nB\nC\nD")
print("A\tB\tD")
print("WXY\bZE")

# Single double and tripe Quotes
print('This is in Single Quotes, It is taken as string')
print('Application for single quotes is when we have a Double quote inside the String: ')
print("This is in Double Quotes, It is also taken as a string")
print("Application for double quotes is when we have a single quote inside the String: That's awesome!")
print('''This is a triple quotes
This prints Multi-line Statements together
This is working pretty well!''')

# ADD integers
print('Enter integer 1: ')
x = input()
print('Enter integer 2: ')
y = input()
num1 = int(x)
num2 = int(y)
print(num1, '+', num2, '=', num1+num2)

# Shorter way of the same program
x, y = int(input("Num1: ")), int(input("Num2: "))
print(x, '+', y, '=', x+y)
# Different operators in python
print(x, '-', y, '=', x-y)
print(x, '*', y, '=', x*y)
print(x, '/', y, '=', x/y)
print(x, '//', y, '=', x//y) #It will return the integer as quotient
print(x, '%', y, '=', x%y)
print(x, '^', y, '=', x**y)

# Assigning values to variables
x = 100
v = ' \n'
y = 300
c = 'I am happy'
print('x+y:', x+y)
print(v+c)

# Multiple Assignment
x = y = z = 100
print(x)
print(y)
print(z)
a, b, c = 100, 200, '\nI love RNSIT'
print(a, b, c)


# Exchange 2 Variables
print("This is the Beauty of Python!")
a = 2
b = 3
print("Before Exchange: ", end="")
print("a =", a, "| b =", b)
b, a = a, b
print("After Exchange: ", end="")
print("a =", a, "| b =", b)


# Increment and Decrement Operator
# There is no Increment and Decrement operator in Python
# i++ and i-- or ++i and --i does NOT work in Python
i = 10
print('Initial Value:', i)
print('Incrementing i')
i += 1
print('After Increment:', i)
i -= 2
print('After Decrement:', i)

# .format()
print("My name is {name} and my USN is {USN}".format(name = "Akshay",USN = "1RN15EC013"))
print("My name is {} and my USN is {}".format("Akshay","1RN15EC013"))






