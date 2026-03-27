class Book:
    def __init__(self, title:str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None
    
    def __str__(self):
        borrow = f"Yes, by user: {self.borrowed_by.name}" if self.is_borrowed else "No"
        return (
                f'Title: {self.title}, '
                f'Author: {self.author}, '
                f'ISBN: {self.isbn}, '
                f'Borrowed: {borrow}')


class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f'User_id: {self.user_id}, Name: {self.name}, Email: {self.email}'


class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
            print('New book appended')

    def list_books(self):
        if not self.books:
            print('No books in the Library.')
        for book in self.books:
            print(book)
        
    def boorrow_book(self, isbn:int, user: User):
        if user.user_id in self.users:
            for book in self.books:
                if book.isbn == isbn and not book.is_borrowed:
                    book.is_borrowed = True
                    book.borrowed_by = user
                    print(f'The book "{book.title}" has been borrowed by {self.users[user.user_id].name}')
                    return
        print('Book is not available or has been borrowed')
                      
    def return_book(self, isbn: int, user_id: int):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed and book.borrowed_by.user_id == user_id:
                book.is_borrowed = False
                book.borrowed_by = None
                print(f'The user: {self.users[user_id].name} return the book: {book.title}')
                return
        print('Book is not available or has been borrowed')

    def add_user(self, user: User):
        if isinstance(user, User):
            self.users[user.user_id] = user
            print(f'The user {user.name} was addeded.')

    def list_users(self):
        if not self.users:
            print('No users to show')
            return
        for _, user in self.users.items():
            print(user)

    def update_user(self, user_id: int, name: str|None=None, email: str|None=None):
        try:
            user = self.users[user_id]
        except KeyError:
            print('The user do not exist.')

        if not name and not email:
            return
        if name:
            user.name = name
        if email:
            user.email = email
        print('User is updated')

    def delete_user(self, user_id: int):
        del self.users[user_id]
        print('Deleted user.')

            
# Create users
user1 = User(1, 'Edgar Sanchez', 'edgar@gmail.com')
user2 = User(2, 'Carlos Rodriguez', 'carlos@gmail.com')
user3 = User(3, 'Erika Reyes', 'akire@gmail.com')

# Create books
book1 = Book('Python Crash Course', 'Erick Matthes', 980567)
book2 = Book('Learn Python The Hard Way', "Zed Shaw's", 23546)
book3 = Book('Testing Python Applying Unit Test, TDD, BDD and Acceptance Testing', 'Davis Sale', 765234)
book4 = Book('How Linux Works, What Every Superuser Should Know', 'Brian Ward', 3425) 

# Agregar libros a la biblioteca
libreria = Library()
libreria.add_book(book1)
libreria.add_book(book2)
libreria.add_book(book3)
libreria.add_book(book4)

# Listar libros
libreria.list_books()

print()

libreria.list_users()

print()

# Add users
libreria.add_user(user1)
libreria.add_user(user2)
libreria.add_user(user3)

print()

libreria.list_users()

print()

# Prestar un libro
libreria.boorrow_book(980567, user1)
libreria.boorrow_book(23546, user2)
libreria.boorrow_book(980567, user2)
libreria.boorrow_book(980908878, user1)

print()

libreria.list_books()

print()

# Return book
libreria.return_book(980567, 1)
libreria.return_book(23546, 2)
libreria.return_book(980567, 3)
libreria.return_book(9805672314, 4)
libreria.return_book(9805671234, 5)

print()

libreria.list_books()

print()

libreria.update_user(1, name='Omar')
libreria.update_user(2, email='carod@gmail.com')
libreria.update_user(3, email='carod@gmail.com')
libreria.update_user(6)

print()

libreria.list_users()

print()

libreria.delete_user(1)

print()

libreria.list_users()

