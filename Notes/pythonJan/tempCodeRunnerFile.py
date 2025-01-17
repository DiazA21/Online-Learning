
# Create a dictionary with authors as keys and a list of books as values
authors_books = {
    "J.K. Rowling": ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets"],
    "George Orwell": ["1984", "Animal Farm"],
    "J.R.R. Tolkien": ["The Hobbit", "The Lord of the Rings"]
}

# Ask the user for an author's name
author_name = input("Enter the name of the author: ")

# Use the get method to retrieve books or return "Author not found" if the author doesn't exist
books = authors_books.get(author_name, "Author not found")
