print("Hello World!")

# pep-8 style guide

# Age = 10 - capital reserved for class names
# AGE = constants
# class_ = 10 - avoid keywords

# PascalCase - class/file names (optional)
# camelCase - vars/functions/methods
# snake_case - vars/functions/methods
    # Choose one and be consistant within code

# Objects

# a = 100
# b = 100

# print(a is b) # interning, referencing same object
# limit 256 

# def t1():
#     c = 200
#     return c
# def t2():
#     c = 200
#     return d

# print(t1() is t2())

# Scope

# Global variables - accessible everywhere
# Local variables - only available within function / file

# Shadowing - referencing global variables in local variables

# Data types

# int
# string
# float
# boolean

# In-built functions

# print()
# input()

# escape chars

# \ take the next symbol as its literal meaning
# \t tab, \n newline, \unicode, \U extended unicode, \\ backslash, "hello , \"andrew\"

# print("Person1: \they how are you? \n Person 2: \tI'm good thanks \U0001f604")

# string concatenation

# name = input("enter your name: ") # defaults to string
# age = int(input("enter your age: "))

# # # object.method
# # message = "Your name is {}, your age is {}".format(name, age)
# # print(message)

# # print("your name is " + name) # limited to same data type
# # print("your name is", name, "your age is", age)

# print(f"your name is {name}, your age is {age}")

# BODMAS

# floor division // - 10//3 = 3 - division round down. ceiling - round up
# % 10%3 = 1 # remainder

# sting methods

# print("hello world".upper())
# print("HELLO WORLD".lower())

# print("hello world".count("o", 3, -3))
# print("hello world world world".replace("world", "class", 2))

# print("hello world".split('#'))