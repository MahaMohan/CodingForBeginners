#PYTHON PRATICAL CHEATSHEET

#python is a case sensitive language
#Python runs programs from Top to Bottom

print("Hello World")
# Output of a String(Sequence of characters)


#VARIABLES
# variables to temporarily store data in memory
age = 20
# storing 20 as age variable in computer memory
print(age)
# Output prints value of age variable

Price = 19.95
#Variables can store numbers as Whole numbers(integers) or in Decimals (float)
First_name = "mahadhevha"
#underscore for easier readability for variable to store string value
is_online = False
#Boolean either True or False is Yes/No in computer language



#RECEIVING INPUT
#Input always get user value/data as string(sequence of characters)
#Built in function to get input from user
input("What is your name? ")
#A simple input function to get your name

name = input("What is your name")
#Getting the input from the user and assigning it to a variable
print("Hello" + name)
#String Concatenation: Combining both strings to form a sentance



#TYPE CONVERSION
#Functions used to convert value of variable from one type to another
#integer is a whole number in programming
#flaot is a number with decimal values
#string is a sequence of characters together

10 #whole number or integer
10.89 #number with decimals or float
"Mosh" #Strings
True #Booleans

int() #converting string to integer
float() #converting a string to a float
bool() #converting a string to a boolean value

#Input always get user value/data as string(sequence of characters)
birth_year = input("Enter your birth year: ")
h = 2020 - birth_year #ERROR
print(h)
#ERROR Caused by subtraction of String(user value) from integer(2020)
h = 2020 - int(birth_year)
print(h)
#converting uservalue from string to integer

birth_year = input('Birth year: ')
print(type(birth_year))
#type() gets us the variable type in this case it is <class 'str'> 
age = 2022 - int(birth_year)
print(type(age))
#type() prints age's type as <class 'int'>



#Srings
#You can use both single or double quotes to define a string
course = "Python's course for beginners"
course = 'Python for "beginners" '
#define string that uses multiple lines
course = ''' 
Hi Epicalable,
Here is our first email to you.

Thank you,
The support team
'''

#Getting specific character from string using index
course = 'Python for beginners'
        #0123456789
print(course[0])
#OUTPUT: P
#First character in string is indexed 0
course = 'Python for beginners'
print(course[-1])
#Last character of the string at the end

course = 'Python for beginners'
print(course[0:3])
#OUTPUT: Pyt
#Returns value from index 0 to index 3 but exclude index 3
print(course[0:])
#Prints the entire string varaible
another = course[:]
#Can be used to duplicate the string and store it in another variable


#Formatted Strings
#useful when you want to dynamically generate a text for your variable
first = 'John'
last = 'smith'
#Want to generate a text John [Smith] is a coder
message = first + ' [' + last + '] is a coder'
print(message)
#BUT IT IS NOT IDEAL SO WE USE FORMATED STRING

msg = (f'{first} [{last}] is a coder')
#Curly braces act as placeholders or holes in our string

#String Methods
course = 'Python for beginners'
print(len(course))
#Returns the number of characters in the string
course.upper()
#Converting string to uppercase
course.lower()
#Converting string to lowercase
course.find('P')
#Output is 0
#If character cannot be found output will be -1
course.replace('Beginners', 'Absolute Beginners')
#Replace part of string with another string
print('Python' in course)
#Search if string is present and Output will give a boolean value True



#ARITHMETIC OPERATIONS
10 #Integers are whole numbers
10.123 #Floats are numbers with decimal points

print(10+3) #Addition Operator
print(10-3) #Subtraction Operator
print(10*3) #Multipliaction Operator
print(10/3) #Division Operator
#OUTPUT is 3.333333333333(FLOAT)
print(10//3)
#OUTPUT is 3(INTEGER)
print(10%3) #Modulus/Remainder Operator
#Gives remainder of the division: 1
print(10 ** 3) #Exponent/Power Operator
#OUTPUT is 1000

#Argumented Increment
x = 10
x = x + 3
print(x) #Output is 13 since it gets incremented
x = 10
x += 3 #Argumented Assignment Operator
print(x) 

#Operator Precedence
x = 10 + 3 * 2 #Using B.O.D.M.A.S we get 16
x = 10 + 3 * 2 ** 2 #We get 22
#Paraenthesis takes priority
x = (10 + 3) * 2 ** 2 #We get 13*4

#Math Functions
x = 2.9
print(round(x)) #Built in function to round up numbers we get 3
print(abs(-2.9)) #Absolute always return a positive number we get 2.9

import math
from struct import calcsize #Module to access all maths functions
math.acos()
math.sin()
math.ceil(2.9) #We get 3
math.floor(2.9) #We get 2
#Search for "Python 3 Math Module and read the documentation to learn all the functions"



#IF STATEMENT

is_hot = True
if is_hot:  #If it is False only 'Enjoy your day' will be shown
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")

is_hot = False
if is_hot: #Only gets displayed if is_hot is True
    print("It's a hot day")
    print("Drink plenty of water")
else:    #Only gets displayed if is_hot is False
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

is_hot = False
is_cold = True
if is_hot:  # Only gets displayed if is_hot is True
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:  # Only gets displayed if is_hot is False
    print("It's a lovely day")
print("Enjoy your day")
#Since is_cold is True, elif statements will be shown



#LOGICAL OPERATORS
#situations when we have multiple conditions

#Logical And Operator
#If applicant has HIGH INCOME and GOOD CREDIT then ELigible for loan
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
#If any of the conditions is False then message will not be shown

#Logical OR Operator 
#If applicant has HIGH INCOME or GOOD CREDIT then ELigible for loan
has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for loan")
#Even if one of the conditions is false message will be shown

#Logical NOT Operator
#If applicant has GOOD CREDIT and no criminal record then ELigible for loan
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
#NOT operator changes False to True and message will be shown thanks to AND
#If has_criminal_record is True then NOT will be False and message won't be shown

#AND: BOTH SHOULD BE THROUGH
#OR: AT LEAST ONE SHOULD BE TRUE
#NOT: INVERSES THE VALUE EX. BOOLEAN TRUE TO FALSE



#COMPARISON OPERATOR
#Used to compare variable with value to give a boolean value

temperature = 35
if temperature > 30: #expression since it's a piece of code which gives boolean value
    print("It's a hot day")
else:
    print("It's not a hot day")
#OUTPUT: IT'S A HOT DAY

# > Greater than operator
# >= Grater than equal to Operator
# < Less than Operator
# <= Less than equal to Operator
# == Equality Operator
# != Not equl Operator
# = Assignment Operator to assign values or changing value



#WHILE LOOP
#To execute a block of code multiple times
# SYNTAX:-
# while condition:
#    .......
#If condtion is satisfied it will be executed repeatedly

i = 1
while i <= 5:
    print(i)
    i = i + 1 #If not added then I will be 1 forever and will end with a infinity loop
    break #Used to terminate the loop
print("Done")



#FOR LOOP
for item in 'Python':
    print(item) #Each character of string is printed on newline

# In python [] defines list
for item in ['mosh','john','sarah']:
    print(item)

for item in range(10):
    print(item)
#instead of typing out [1,2,3,4,5,6] we can do range(10) using the range function
#range creates a special object that it can iterate over
for item in range(5, 10):
    print(item)
#We get numbers starting with 5 and end with 9
for item in range(5, 10, 2):
    print(item)
#We get 5,7,9 as it increments by 2

#NESTED LOOPS
#Adding 1 loop inside another loop
for x in range(4):
    for y in range(3):
        print(f'({x} , {y})')
#OUTPUT: (0,0),(0,1),(0,2),(1,0),(1,1),(1,2),ETC.....
       


#LISTS
names = ['John', 'Bob', 'Mosh', 'Sarah', 'mary']
print(names[0]) #OUTPUT: John
print(names[2]) #OUTPUT: Mosh
print(names[-1]) #OUTPPUT: Mary
print(names[2:]) #OUTPUT is from Mosh to end of the list
print(names[2:4]) #OUTPUT: Mosh, Sarah
print(names[:]) #Gets all the items in the list

names = ['John', 'Bob', 'Mosh', 'Sarah', 'mary']
names[0] = 'Jon'  #REplaces John with Jon
print(names) 


#2D LISTS
#Based on mathematicsl concept of matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1]) #Output: 2
#Changing matrix value
matrix[0][1] = 20
print(matrix[0][1]) #Output: 20
#Using a loop to get all the values in a matrix
for row in matrix:
    for item in row:
        print(item)
#Output: 1 2 3 4 5 6 7 8 9


#LIST METHODS/FUNCTIONS
#operations to perform on a list
numbers = [5,2,1,7,4]
numbers.append(20)
print(numbers) #Output: [5,2,1,7,4,20]

numbers.insert(0,10) #Insert in a specific position
print(numbers) #Output: [10,5,2,1,7,4]

numbers.remove(5)
print(numbers) #Output: [2,1,7,4]

numbers.clear()
print(numbers) #Output: []

numbers.pop() #Removes the last number on the list
numbers.index(5) #Gets us the location of number here is 0

print(50 in numbers) #Output will be in a boolean value True or False if objest exists

numbers = [5,2,1,5,7,4]
print(numbers.count(5)) #print how many times 5 is repeated. Here is 2

numbers.sort() #Sort in asending order
numbers.reverse() #sort in desending order
numers2 = numbers.copy() #Creates a copy of the list in a new variable


#TUPLES
#Similar to lists but cannot be modified and is immune to changes
numbers = (1,2,3,4) #Use normal bracket to create a tuple
#Only can get info on tuple and values cannot changed
print(numbers[0]) #Gets number on index 0 here it is 1
#Best to be used in program to prevent accidental changes


#UNPACKING
coordinates = (1,2,3)
x = coordinates[0] 
y = coordinates[1]
z = coordinates[2]
answer = x*y*z
#Can follow the below method to get same answer with far less code

x, y, z = coordinates
#Python assigns the values to the variables acoordingly 
#Can be used in lists as well


#DICTIONARIES
#store info as key value pair
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"]) #Output: John Smith
print(customer.get("birthdate")) #Doesnt yell at us if wrong request
print(customer.get("birthdate", "Jan 1 1980")) #Added default value in case not in dictionary

customer["name"] = "Jack Smith" #Edited name of the dictionary
customer["birthdate"] = "Jan 1 1980"
print(customer["name"]) #Ability to add new or update key values in dictionaries


#FUNCTIONS
#As our project grows we need a better way to organise our code by breaking up into smaller reusable chunks
#It is a container with a few lines of code that performs a specific task
#print() ,input() are inbuilt functions that have a purpose 

def greet_user(): #colon is to tell python we are defining a block of code
    print('Hi there')
    print('welcome aboard') #We will need them in other programs
#Whenever greet_user funtion is called these 2 lines will appear

print("start")
greet_user()
print("finish")
#On running program we get 4 messages on the terminal Both print and function statements
#Order of code matters as calling function bafore it is defined gives an error


#PARAMETERS
#Passing infomation to your functions

def greet_user(name): #Function gets value from main code
    print(f'Hi {name}!') #Value is formatted and then sent to main code
    print('welcome aboard')

print("start")
greet_user("John") #Passing a value to the funcion
greet_user("Mary") #Reusing same function by passing it a different value
#If didn't have function we would need to rewrite entire code twice for John and Mary
print("finish")
#Running program replaces the line hi there with hi john and then hi mary

#If function has parameter we are obligated to pass a value for that parameter if not error will occur
#Argument in programming is the value that we supply to a function
#John, Mary are argument that we pass to the name parameter
#Parameters are holes or placeholders we define in our funtion for recieving info
#Arguments are the actual pieces of infomation that we supply to these functions

def greet_user(first_name, last_name):  # Function gets value from main code
    print(f'Hi {first_name} {last_name}!')  # Value is formatted and then sent to main code
    print('welcome aboard')

print("start")
greet_user("John", "Smith")  # Passing values to the funcion
print("finish")
#Passing 2 arguments to the parameters of the function


#KEYWORD ARGUMENTS
#Position of passing the arguments doesn't matter here
#Combination of parameter name followed by it's value is keyword argument
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('welcome aboard')

print("start")
greet_user(last_name="Smith", first_name= "John")  #Here we have 2 keyword arguments
#Now we dont have to worry about the order of the parameter
print("finish")
#It usually helps with the readability of the code sometimes than positional arguments
#Good to use when passing numerical values as we cant guess what those values represent:
#Example: calc_cost(total=50, shipping=5, discount=0.1) increase readability


#RETURN STATEMENT
#Create functions that return values
def square(number):
    return number*number #return value back to main code

result = square(3)
print(result) #Output: 9
#Or can be written as:
print(square(3)) #A Shorter code
#If return statement is removed we will get default value Output: None


#EXCEPTIONS
#How to handle errors in your program as a good programmer always anticipate 
#these kind of exceptions and handle them properly

age = int(input('age:'))
print(age)
#If value is other than integer we get an error invalid input
#Exit code 0 means good and 1 means it crashed
#Print a proper error message if program crashed
try:
    age = int(input('age:')) #Wrong input will lead to an excption
    print(age)
except ValueError: #Print proper error message if user input not integer
    print('Invalid value') #Message will be printed if there is an exception

try:
    age = int(input('age:'))  #Now user enters 0
    income = 20000
    risk = income/age  #No number can be divided by 0
    print(risk)  #We will get error zerodivisionerror
except ZeroDivisionError: #20000 cannot be divided by 0 and will be caught
    print('age cannot be zero')
except ValueError:   #0 is an integer and hence not caught by valueerror
    print('Invalid value') 


#COMMENTS
#Comments are used to add notes or comments to our program to help with readability

#This line is ignored and can serve as reminders or notes to communicate with other devs
#Bad comment is ex. print sky is blue as it is obvious next line will print this 
print("Sky is blue")
#Don't use useless and repeative comment as it will create more noise in the code for others when thwy read
#Use comments to explain hows or assumptions or can be used to remind yourself or others


#CLASSES
#Classes are used to define a new type to model real concepts
#basic types: numbers, strings, boolean and complex types: lists, dictionaries
class Point:  #Pascal naming convention used for class ex. EmailClient
    def move(self):
        print("move")

    def draw(self):
        print("Draw")
#A new type has been created with this class and now we can make new objects
#Object is an instance of an class
point1 = Point() #Store the object in a variable
point1.draw() #defined method is useable
#Output: Draw
point1.move() #defined method is useable
#Apart from methods these objects can also have attributes
