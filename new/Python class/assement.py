# Ask the user for a number of seconds (e.g. 3661). 
# Convert it to hours, minutes, and remaining seconds. 
# Print in the format "1 hour(s), 1 minute(s), 1 second(s)".

# total = int(input("Enter seconds: "))

# convert to h, m, s

#-----------
# Take 3 numbers from the user & perfom the following
# Provide Addition
# Provide Subtraction
# Provide Float number solution
# Take power of a & b values



# ----------
# Ask the user for a rectangle's width and height. 
# Print the area and perimeter with clear labels.

# width = float(input("Width: "))

# height = float(input("Height: "))

# calculate area and perimeter

# --------------------

# Ask for a total bill amount and the number of people 
# splitting it. Calculate each person's share (as a float), 
# round it to 2 decimal places, and print the result clearly.

# bill = float(input("Total bill: "))

# people = int(input("Number of people: "))

# calculate and print each person's share


# Write a single list which has 10 phones names & 8 cars name
#Print the following
# Get the last value printed as 'samsung'
# print the values between index value of 3 & 12

# ----
# in the above list add S24 Ultra at the last of the list & print the only
# S24 ultra
# Insert Jeepv32 at the index 5
# change the value of samsung to nokia Black


# Write a program taking input from the user & printing their grades

# write 6 table multiplication using range()

# Number Guessing Game

#secret_number = input(int("whar is no."))
#attempts = 1

#while attempts <= 5:
  #  guess = int(input(f"Attempt {attempts}/5 - Enter your guess: "))

    #if guess == secret_number:
     #   print("Congratulations! You guessed correctly.")
   #     break
  #  else:
 #       print("Wrong guess!")

#    attempts += 1

# if attempts > 5:
#    print("Better Luck Next Time!")
#    print("The number was", secret_number)
    
# Write a program using the def() function take 2 values add them & the output of this to be 30

# Restaurant Billing System

menu_items = ["Pizza", "Burger", "Pasta", "Biryani", "Sandwich"]
menu_prices = [250, 150, 200, 180, 120]

print("----- RESTAURANT MENU -----")
print(menu_items[0], "-", menu_prices[0])
print(menu_items[1], "-", menu_prices[1])
print(menu_items[2], "-", menu_prices[2])
print(menu_items[3], "-", menu_prices[3])
print(menu_items[4], "-", menu_prices[4])

item1 = input("Enter your first food item: ")
item2 = input("Enter your second food item: ")

price1 = menu_prices[menu_items.index(item1)]
price2 = menu_prices[menu_items.index(item2)]

total_amount = price1 + price2
gst = total_amount * 18 / 100
final_bill = total_amount + gst

print("----- BILL -----")
print("Selected Item 1:", item1)
print("Selected Item 2:", item2)
print("Total Amount:", total_amount)
print("GST (18%):", gst)
print("Final Bill:", final_bill)