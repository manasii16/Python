# Write a library class with no_of_books and books as two  instance variable.
# write the program to create a library from this library class and show how you can print all books, add a book and 
# get the number of books using different methods.
# show that your program doesn't persist the books after the program is stopped!

class library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)
    def show_books(self):
        print(f'The Library has {self.no_of_books} books.The books are ')
        for book in self.books:
            print(book)
l1=library()
l1.addbook("Harry Potter")
l1.addbook("Python")
l1.addbook("Java")
l1.show_books()
