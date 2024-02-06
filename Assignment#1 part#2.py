# assignment1_part2.py

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")

# Instantiate two objects from the Book class
book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Ivanhoe: A Romance")

# Print both objects using their display() functions
book1.display()
book2.display()
