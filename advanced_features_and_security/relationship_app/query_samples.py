# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Query all books by a specific author
def books_by_author(author):
    return Book.objects.filter(author=author)

# Retrieve the librarian for a library
def librarian_for_library(library):
    return Librarian.objects.get(library=library)

# Retrieve a library by name and return all its books
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

