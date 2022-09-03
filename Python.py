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
message = first + ' [' + last + '} is a coder'
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

import math #Module to access all maths functions
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

