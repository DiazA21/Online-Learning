#loops
# for, while, while true

# while

# need a condition to start the loop
# need a condition to stop the loop
# continuoisly execure a block of code
# known conditions

# x = 0
# while x < 101:
#     print(x)
#     x += 1
    
# break and continue

# i = 0
# while i < 6:
#     if i ==3:
#         break
#     print(i)
#     i += 1

# j = 0

# while j < 6:
#     j += 1
#     if j == 3:
#         continue # skips to next iteration
#     print(j)


# for loop
# unknown conditions / parameters
# used for looping through an iterable

# myFruits = ["apple", "pear", "orange", "kiwi"]

#     #item    #iterable
# for fruit in myFruits:
#     print(fruit)
    
# l = 0 
# while l < len(myFruits):
#     print(myFruits[l])
#     l += 1

# range

# for a in range(5): # index position 0 1 2 3 4
#     print(a)

# for a in range(1,5): 
#     print(a)

# for a in range(1, 10, 2): # steps
#     print(a)

# strings

# for letter in "hello":
#     print(letter)

# list comprehension - used for making lists
      # expression  # item  # iterable
# result = [x**2 for x in range(5)]
# print(result)

# without list comprehension

# results = []

# for x in range(5):
#     results.append(x**2)

# print(results)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    # expression  # item  # iterable  #condition
#  evenSquaredNumbers = [number**2 for number in numbers if number % 2 == 0]
# evenSquaredNumbers = [x**2 for x in [int(number) for number in numbers]]

# print(evenSquaredNumbers)

# dictionaries

# for i in {"Still":"water"}: # collects key
#     print(i)
    
# for i in {"Still":"water"}.values(): # collects values
#     print(i)
    
# for i, j in {"Still":"water"}.items(): # collects items / key:value
#     print(i, j) # outputs as a tuple
    
# exercise
# write a loop that takes in 5 names as input and prints name + "is cool"
# while loop
# for loop
# list comp
# optional - 1 line list comp



# i = 0
# while i < 5:
#     name = input("Enter a name: ")
#     print(name + " is cool")
#     i += 1


# for name in range(5):
#     names = input("Give me a names: ")
#     print(names + " is cool")

# names = [input("Enter name: ") for name in range(5)]
# for name in names:
#     print(f"{name} is cool")

#          # expression              # item           # iterable
# [print(input("Enter a name: ") + " is cool") for name in range(5)]

# print() default output is none
# x = [print(input("Enter a name: ") + " is cool") for name in range(5)]
# print(x)
