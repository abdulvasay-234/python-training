print("Hello World") # Print Statement

# Variables
# To store a value
name = "afnan"
print(name)
phone = 123456789 #Integer / number
email = "lords@lords.com"
print (phone)
print (email)
print("Hello This is a python class")

# Python is case sensitive -> it dosent understand alphabets & numbers particular about how we write the code

Name = "vasay"
print(name)

#Case Sensitive
#12hello = "world" #Show error, you cannot start with number
hello12 = "this works" # This will run
#-error = "this try" #cant start with special characters
hello_world = "this is something new"
phone_Number_1 =123456
phone_Number_2 = 258856
# phone number = 123456856 #Cant have space in variables

# Python excuete the code from line to line from top to bottom.

# strings -> Alphbets 
# integers -> Numbers. 3689
# Float -> Decimal numbers 25.36
# Boolean values -> TRUE / FALUSE

# Arthematic Operators -> Doing Maths
# + - Addition
# - Subtraction
# * Multiplication
# / Division #Float Decimal. 4.6
# // Floor division #Integer. 5 round off the value
# % Reminder / modulo
# ** Power

a = 56 #variable / value 1
b = 78 #variable / value 2
c = a + b #storing the values in the 3rd variable to  do the calculattion
d = c - 12
e = a * b
print(d) # calling our statement by printing

# Inputt Function
# name_inp = input("What is your name? ")
# print(name_inp)
#pho = input("phone: ")
#print(pho)

#Joining 2 statements
#student_name = input("Whats is Your Name")
#print("Hello " , student_name , " Welcome!")
#social = input("Social")
#print("Social Marks: " , social)

# Type casting

# string -> integer
b = 23 #integer
k = "78" #string
r = b + int(k) # addition & converting from strg to integer
print(r)

#Float -> Float
h = 80
u = 2.36
v = h + int(u)
print(v)

# Integer -> string
age = 25
message = "Hey" , str(age) , " is your age"
print(message)

# string -> Float
price = "99.05" # string
price = float(price)

print (price)

# Input
# By default the python understand it as string even if it is integer
# float or anything
# age = input("Enter You age ")
# print(type(age))

# calculation
age = int(input("Enter your age "))
print (age + 1)

# int("25") # can be changed
# int("25.78") # error Strng & float
# float("25.89") It can be changed
# int("hello") #cannot be changed

# Comparator Operators
#  < less than
#  > Greater than
#  == Equal
# != Not equal
# <= Less Than equal
# >= Greater Than equal

marks = 75
print(marks ==75) # True
print(marks != 100) #True
print(marks > 80) #Faluse
print(marks >= 75) #True
print(marks < 50) #Faluse
print(marks >75) #Faluse

a = 100
a += 50 #o/p 150
a -= 30 #o/p 120
a += 100 #o/p 
print(a) #o/p 220

# Create two variables x= 10 & y = 20. swap their values so that
# X become 20 & y becomes 10. Print them after swapping.
# Try doing it without third variable
x = 10
y = 20
x,y = y,x
print(x,y)

# F strings - Function
name_last = "faiz"
age_f = 24
marks_total = 96.5678

print(f"Name: {name_last}, Age: {age_f}")
print(f"Marks: {marks_total:.1f}%")


# List - store lot values
fruits = ["apple" , "Mango" , "Banana" , "Pineapple"]
phone_numbers = ["871210", "456789" , "34569876" , "56789"]

#Indexing / Index values start from 0
print(fruits[0])

#What if the values are large data set
print(fruits[-4]) #This will give last data

# IF we want to get / print first value we need to print 0
# If we want to get the last values we go with negative numbers -1...

# Slicing -> to divide our list
print(fruits[0:4]) #only value before will be stopped so till index 3
print(fruits[:3]) #First 3 values
print(fruits[::3]) #Step Slicing

# Add values
fruits.append("Orange")
fruits.append("Avacado")
print(fruits)