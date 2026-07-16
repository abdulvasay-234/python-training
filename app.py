#Print statement
print("Does it show error?")
print("This is an error code")
print("Lets try if this prints or not")

# Variables
fruit = 'Apple'
yelloColorFruit = 'u'

print(yelloColorFruit)
print(fruit)

# Write a student detail which has the following
#Name, Phone No., Clg & then print all this

# arthematic operators
# + , - , * , /


a = 9.87
b = 8
c = 90
d = 98
e = a*b
print(e)

# print the addition
# a value to be 9.87
# b value to be 8
# f value to be 90
# answer to be 8

# float - Decimal 9.8
# Integer - Numbers 98
# String - Alphabet
# Boolean - True / Faulse (1 / 0)

# Case Sensitivity

name1 = "Afnan"
name2 = "Vasay"
name3 = "Vasay"
name3= "Abdul"


Phone_Numbe = "892732348"
phone_number = "892732348"
print (phone_number)


#Create the following (Practice Question)
# Name as [your name]
# name as [your friend name]
# Phone as [your friend name]
# add any 2 numbers which gives the sum as 45
# - Print the answer
# Only after all this this exactly to be
# Printed "This is my Phone No. 99887755"

# Type formating

apple = 95 #Integer
total = ("The apple cost is" , apple , "Rupees") #Type Convertion
print (total)

a = 10 #Integer
b = "20" #String / Alpha Numerical
e = 40 #Integer
c = int(b) + a #B is converting to Integer
# d = b+e 
print (d)


# Create values for
# a, b, c, d, e, f,
# where values of a, e, f are alpha numeric
# & rest of the values are integers
# Now based on the above values you defined
# print a + e + f //output
# Print b - c + d // Output
# Print a + b + f // Output
# Also provide you marks of maths where you,
# write the complete code & the output should be
# ('My marks in maths is' 79)


# Data Types
Student_Name = "Vasay" #Str
Student_Maths = 9 # Int
Student_Physics = 8.5 #FLoat
Student_Chemistry = 9
Student_Enrollment = False #Boolean

print (Student_Enrollment)

# Understanding types -> Type is a built in function
Student_Name = "Vasay" #Str
Student_Maths = 9 # Int
Student_Physics = 8.5 #FLoat
Student_Chemistry = 9
Student_Enrollment = False #Boolean

print(type(Student_Name))
print(type(Student_Maths))
print(type(Student_Physics))
print(type(Student_Enrollment))

# Reassigning of the variables
a = 10
# print (a) #O/p - 10

a = a + 20
print (a) #o/p - 30

a = a + 50
print (a) #O/p - 80



a = 80
b = "name"
c = False

print(type(b))
print(type(a))

# arthematic operators
# + - Addition
# - Subtraction
# * Multiplication
# / Division #Float
# // Floor division #Integer
# % Reminder / modulo
# ** Power

print("This is the solution")
a = 2
b = 2
c = a + b   # 4
d = a * b   # 4
e = a / b   # 1
print(a // b) # 0
# print(a % b)    # 0
print(a ** b)   # 4

print (e)

# / division but gives in float number
# // Integer 

# Comparator Operators
# < Less than
# > Greater than
# == Equal
# != Not equal
# <= Less equal
# >= Greater equal

marks = 75
print(marks == 75)   # T
print(marks != 100)  # T
print(marks > 80)    # F
print(marks >= 75)   # T
print(marks < 50)   # F


# Assement
a = 100
a += 50 #O/p - 150
a -= 30 #O/p - 120
a += 100 #O/P - 220
print(a)

# 3) Create two variables x = 10 and y = 20. Swap their values so 
# that x becomes 20 and y becomes 10. Print them after swapping. 
# Try doing it without a third variable.
x = 10
y = 20
x,y = y,x
# print(x,y)

# Input Function (I/p)
# input("What is Your Name?")
# name = input("What is Your Name?")
# Phone = input("what is phone: ")
# print(Phone)
# print(name)

# a = input(int("Write 1st No."))
# b = input("Write 2st No.")
# c = a + b
# print (c)

# take input of Name, Phone Number, & College & then
# Print all of the above fields

# Write a program to calculate the Year of Birth of a person
# by asking / taking their age 

# name = str(input("What is Your Name"))
#age = int(input("what is your age"))


# O/p 
# Hello ---, we both are of same birth year that is ---

# F strings | Functions
name = "Faiz"
age = 24
maths_marks = 96.1233 #Float

print(f"Name: {name}, Age:{age}")
print(f"Marks: {maths_marks:.2f}%") 

# Ask user to type the input

# List - Mutable - it can be changed
fruits = ["apple" ,  "Mango" , "pineapple", "carrot", "tomato", "raddish"]
vegitables = ["carrot", "tomato", "raddish"]
print(fruits)
print(vegitables)
print(fruits[-2])

# Slicing
print(fruits[0:5])
print(fruits[:3]) #First 3 values will be printed
print(fruits[::2]) #Step slicing

# add values
a = ["car", "bike", "truck"]
a.append("buss")
print(a)
# Append addes value at the last of the list

# Insert
a.insert(2, "auto")
print(a)

# change the values
p =[1,2,3,4,5] # change index 3 value with 40
p[1] = 20
p[3] = 40
print(p)

#extend
p.extend([6,7,8,9,10])
print(p)

# Remove
g = [11, 12, 13, 14, 15]
g.remove(12)
print(g)

#pop
g.pop(1)
print(g)

# delete
del g[2]
print(g)

#clear
g.clear()
print(g)

#List length
lst = [1,32,73,74,65,99]
print(len(lst))

# checking elements
b = ["Apple", "Mango", "Pineapple", "jackfruit"]
print("orange" in b)

#sorting list
q = [66, 98, 45, 20, 10]
q.sort()
print(q) #Assending order

# Decending Order
q.sort(reverse=True)
print(q)

# reverse
q.reverse()
print(q)

# copying list
num = [1, 2, 3, 4, 5]
num1 = num.copy()
print(num1)

#count
e = [5, 6, 5, 9, 5, 9]
print(e.count(9))

#finding index
print(e.index(9))

# If Else

marks = 20

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else: grade = "F"

print(f"Marks: {marks} Grade: {grade}")

# Nested if
age = 10
has_id = True

if age >= 18: #1st condition
    if has_id: #2nd Condition
        print("Access Granted")
    else:
        print("ID required")

else:
    print("Denied Access")
    
# Operators and & or not
temp = 20
is_sunny = True

#and - both conditions must be true
if temp >= 30 and is_sunny:
    print("Hot & Sunny day")
    
# or - at least one condtion need to satisfy / be true
if temp > 40 or not is_sunny:
    print("conditions are extreme high")

else: 
    print ("Condition is fine")
    
    
# One line if / else
mark = 55

# same code in 1 line
result = "pass" if mark >= 50 else "Fail"
print(result)

#For Loops
# scores = [88, 72, 95, 61, 83]
# for result in scores:
#    print(result)
    
# Range()
for i in range(1,6):
    print(f"Student {i}")
    
# Multiplication of 3 table
for o in range(1,11):
    print(f"3 x {o} = {3 * o}")
    
# Step in Range()
for i in range(1,6,3):
    print(f"Student {i}")
    
# Accumulator patter
scores = [88, 72, 95, 61, 83]
total = 0
higest = 0
passing = 0

for score in scores:
    total += score
    if score > higest:
        higest = score
    if score >= 50:
        passing +=1
        
average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average: .1f}")
print(f"Higest: {higest}")
print(f"Passing: {passing} out of {len(scores)}")

# enumerate() attaching the index values
m_students = ["Arav" , "sneha" , "Rohan" , "abhi"]

for i, name in enumerate(m_students, start=1):
    print(f"{i} . {name}")
    
#zip()
names = ["Arav" , "sneha" , "Rohan" , "abhi"]
marks_maths = [88, 98, 45, 87]

for name, score in zip(names, marks_maths):
    grade = "A" if score >=90 else "B" if score >= 75 else "c"
    print(f"{name} {score} Grade: {grade}")

#While Loop + Break + Continue
data = [10, 5, 0, 22, 3, 15, 99]
index = 0

while index < len(data): # Length = 6
    value = data[index] # 
    index +=1
    if value < 0:
        continue
    if value > 35:
        break
    print(f"Processing: {value}")


#enumerate() loop
phy_students = ["Vasay" , "SNeha" , "Abdul"]
for i, name in enumerate(phy_students, start=1):
    print(f"{i}. {name}")
    
# Functions
# It is a reusable block of code
# adv - less code, predefine by user

# Get avg of students marks by taking 5 subjects
# Step-1 : Int() subject -1
# Step-2-4 : Int() subject -2 to 5
# step-5: add all the marks (+) // arthemetic operations
# Step-6: total_marks / total subject

#Functions def()
#def function_name():
    #Function Body
    
def greet():  #def is the keyword used to create the function | gree() is the function name
    print("Welcome to Python!")
greet() #calls the function (executes)

def greet(name):
    print("Hello", name)
greet("Afnan")

# Multiple parameters
def add(a,b):
    print(a+b)
add(10,20)

#Return Statement
def ad(a,b):
    return a+b
result = ad(10,20)
sub
print(result)
