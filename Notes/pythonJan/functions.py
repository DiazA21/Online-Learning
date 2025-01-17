# return value or perform a task
#repeatability

# General rule: print or input shouldn't be in a function

# def greet(name): # parameters that allow the arguements to be passed to the function
#     print(f"Hello {name}")
    
# greet("Andrew")

# def greet1(firstName, lastName, age): 
#     print(f"{firstName} {lastName} is {age}")

# greet1("Andrew", "Diaz", 30)

# def greet1(firstName, lastName, age = 10): # default values should be at the end
#     print(f"{firstName} {lastName} is {age}")

# greet1("Andrew", "Diaz", 30)

# return

# def greeter(name):
#     return f"hello {name}"

# x = greeter("Andrew")
# print(x)

# print(greeter("Andrew"))

# *args - arguements
# if we don't know how many args will be passed through
# tuple of args received

# def makePizza(size, *toppings):
#     print(f"order for {size}-inch pizza with the following toppings: ")
#     for topping in toppings:
#         print(topping)
        
# makePizza(10, "tomato base", "mushrooms", "pineapple", "ham", "cheese", "cheese crust")

# keyword args
# order doesn't matter when calling keyword args
# sends args as key:value pairs

# def fruitList(fruit1, fruit2, fruit3):
#     print(f"fave is {fruit1}")
#     print(f"2nd fave is {fruit2}")
#     print(f"3rd fave is {fruit3}")

# fruitList(fruit3 = "apple", fruit2 = "banana", fruit1 = "strawberry")

# **kwargs 

# def favFood(**food):
#     print("fave food is", food["desert"], "hot", food["dairy"]) # , does the space automatically
    
# favFood(dairy="milk", fruit="apple", desert="pudding")

# combined

# def combine(*args, **kwargs):
#     print("args:", args)
#     print("kwags:", kwargs)
    
# combine(2, c=3, a=5, b=10)

# / introduced 3.8
# before the / must be positional args
# after can be keywords but not enforced
# * would enforce keywords after the star

# def example(a, b, /, *, c, d):
#     print(f"a = {a}, b = {b}, c = {c}, d = {d}")
    
# example("a", "b", c = "c", d = "d")

# example("a", "b",  "c", d = "d") # error , c must be kwarg

# def mathsFunction(a, b, /, operation="add", *, decimalPlace=4):
#     if operation == "add":
#         result = a + b
#     elif operation == "subtract":
#         result = a - b
#     else:
#         raise ValueError("invalid operation")
#     return round(result, decimalPlace)

# print(mathsFunction(10, 15))

# def mathsFunction(a: int, b: int, /, operation="add", *, decimalPlace=4):
#     if operation == "add":
#         result = a + b
#     elif operation == "subtract":
#         result = a - b
#     else:
#         raise ValueError("invalid operation")
#     return round(result, decimalPlace)

# print(mathsFunction(10, 15))

# recurssion

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial (n - 1)

# print(factorial(5))

# lambda functions
# short, unnamed functions, calculate a single expression

# lambda argument: expression (iterable)

# addLambda = lambda x, y: x + y
# print(addLambda(2,4))

# numbers = [1, 2, 3, 4]

# squared = map(lambda x: x**2, numbers)

# print(list(squared))

# high order functions

# either takes in a function as an arg or returns a func

# def square(x):
#     return x * x

# def applyFunction(func, value):
#     return func(value)

# print(applyFunction(square, 5))


