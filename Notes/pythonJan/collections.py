
#complex data types

# complex data types
# storing and structuring data

# lists ordered(indexed), mutable, collection of values ["a", "b", "c"]
# dictionaries unordred(no index), mutable, collection of key:values pairs {"key": "value",...}
# tuples ordered, immutable, similar to a list. () or no parenthesis x = a , b, c x =(a, b , c)
# sets - unique values, unordred, mutable {}

# lists []

#colours = ["blue", "red", "orange", "yellow"]

#print(colours)

# direct access

#print(colours[2])
#print(colours[-3])

# slicing

#print(colours[0:2]) # creates a sublist up to bt not including the final number
#print(colours[1: ])

# altering a list

#colours[0] = "purple"
#print(colours)

# delete

#del colours[1]
#print(colours)

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1], combined[1][1])

# methods

# my_fruits = ["apple", "orange", "pear", "kiwi"]

#my_fruits.append(["grapes", "blueberries"])
#print(my_fruits)

#my_fruits.insert(0, "mango")
#print(my_fruits)


# sort

#my_fruits.sort()
#print(my_fruits)

#my_fruits.sort(key=len)
#print(my_fruits)

# dictionaries

# keys need to be unique, values can be repeated(anything)

# {}

# drinks = {"fizzy": "sprite", "still": "water", "juice": "orange"}

# direct access

#print(drinks["fizzy"])

#drinks["alcoholic"] = "wine"

#print(drinks)

# methods

#print(drinks.values())
#print(drinks.keys())
#print(drinks.items())

# get

#print(drinks.get("still"))
#print(drinks.get("stilll"))
#print(drinks.get("stilll", "not-found"))


#exercise:
#make a dictonary, 3 authors as keys, multiple books per author as values [].
#have an input that asks for an author name and print
#a STRING of the books by the author. (NOT A LIST).
#consider if the user inputs incorect username. 


# # Create a dictionary with authors as keys and a list of books as values
# bookInfo = {
#     "J.K. Rowling": ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets"],
#     "Jane Austen": ["Pride and Prejudice", "Sanditon"],
#     "Harper Lee": ["To Kill a Mockingbird", "Go Set a Watchman"]
# }

# # Ask the user for an author's name
# nameOfAuthor = input("Enter the name of the author: ")

# # Use the get method with a default value of "Author not found"
# books = bookInfo.get(nameOfAuthor, ["Author not found"])

# # Convert the books to a string if it's a list, or leave it as is
# output = ", ".join(books) 

# # Print the result
# print(output)

# Tuples - similar to lists, imutable, cannot be changed

# rectangle = 10, 5

# rectangle[0] = 15

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))

print(set1.intersection(set2))

print(set.symmetric_difference(set2))
