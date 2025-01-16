# if, elifs, elses
# allows for different pathways for our code to take

# isAdmin = False
# isVerified = False
# onHoliday = False

# if someCondition:
#     codeBlockExecutes

# if isAdmin or (isVerified and not onHoliday):
#     print("Access Granted")
# else:
#     print("Denied!")
    
# if should be the desired outcome, else is the negative outcome

# temp = 28

# if temp >=30:
#     print("very hot")
# elif

# Exercise 
# user to input mark/grade
# mark over 80 print distinction
# mark over 60 print pass
# else fail

# mark = print(input("What mark di you acheive?"))
 
# if mark >= 80:
#      print("You got a Distinction!")
# elif mark >= 60:
#     print("You passed!")
# else:
#     print("Fail")

# multiple comparators

# deposit = 99
# password = "password"

# if 0 < deposit < 100 and password == "password":
#     print(f"Thank you for the deposit of {deposit}")
# else:
#     print("failed to deposit")
    
# not

# if not 0 < deposit < 100 and password != "password":
#     print("failed to deposit")
# else:
#     print("thanks")

# in and not in 

# name = "root123"

# if name in ("root", "admin", "user"):
#     print("invalid username")
# else:
#     print("accepted")

# better code
# if name not in ("root", "admin", "user"):
#     print("accepted")
# else:
#     print("invalid username")

# exercise:

# weight convertor app
# user to input weight
# input for kgs or lbs
# if statements to check unit
# converts value
# print result
# 1 kg = 2.2 lbs

# optional - error handling for upper/lower case + incorrect unit input
# optional 2 - error handling for numeric input (input)

# Ask the user to input their weight
# weight = float(input("Enter your weight: "))

# # Ask the user for the unit of weight (kgs or lbs)
# unit = input("Is this weight in (K)gs or (L)bs? ").strip().lower()

# Convert weight based on the unit and print the result
# if unit == "k":
#     converted_weight = weight * 2.2  # Convert kg to lbs
#     print(f"{weight} kg is equal to {converted_weight:.2f} lbs.")
# elif unit == "l":
#     converted_weight = weight / 2.2  # Convert lbs to kg
#     print(f"{weight} lbs is equal to {converted_weight:.2f} kg.")
# else:
#     print("Invalid unit. Please enter 'K' for kgs or 'L' for lbs.")

# Weight Converter App with Error Handling
# try:
    # Ask the user to input their weight
    # weight = float(input("Enter your weight: "))

    # Ask the user for the unit of weight (kgs or lbs)
    # unit = input("Is this weight in (K)gs or (L)bs? ").strip().lower()

    # Convert weight based on the unit and print the result
#     if unit == "k":
#         converted_weight = weight * 2.2  # Convert kg to lbs
#         print(f"{weight} kg is equal to {converted_weight:.2f} lbs.")
#     elif unit == "l":
#         converted_weight = weight / 2.2  # Convert lbs to kg
#         print(f"{weight} lbs is equal to {converted_weight:.2f} kg.")
#     else:
#         print("Invalid unit. Please enter 'K' for kgs or 'L' for lbs.")
# except ValueError:
#     print("Invalid input. Please enter a numeric value for the weight.")

# try and except for Error handling
# masking - programming technique that allows certain data bits to be altered or passed through while keeping others hidden or unaltered
# bubbling - 

# highest number

# num = 10 
# num1 = 20

# if num > num1:
#     print(num)
# else:
#     print(num1)

# rewrite without an if statement or any in built functions (max)

# num = 10
# num1 = 20

# print((num1, num)[num > num1])

# Key Idea:
# In Python, when you index a tuple or list, the index starts from 0. Therefore:

# Index 0 corresponds to the first element of the tuple.
# Index 1 corresponds to the second element.
# How It Works:
# python
# Copy code
# (num1, num)[num > num1]
# Create the tuple:

# python
# Copy code
# (num1, num)  # This is equivalent to (20, 10)
# Evaluate the boolean expression:

# python
# Copy code
# num > num1  # This checks if 10 > 20, which is False.
# False in Python is represented as 0.
# True in Python is represented as 1.
# Use the boolean as an index:

# If num > num1 evaluates to False (0), the tuple is indexed at 0, so num1 (the first element) is selected.
# If num > num1 evaluates to True (1), the tuple is indexed at 1, so num (the second element) is selected.
# Why Can't It Be Reversed?
# The order in the tuple (num1, num) determines which number is chosen for True or False. If you reverse the tuple, like this:

# python
# Copy code
# (num, num1)[num > num1]
# Now:

# If num > num1 is True (1), num1 (the second element) will be selected.
# If num > num1 is False (0), num (the first element) will be selected.
# Summary:
# The key is the order of the tuple:

# (num1, num): num1 for False, num for True.
# (num, num1): num for False, num1 for True.