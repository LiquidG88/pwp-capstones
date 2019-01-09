class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("You have changed your email too, {}.".format(self.email))
        return self.email
    
    def read_book(self, book, rating=None):
        if rating in range(0, 5):
            self.books[book] = rating
            
    def get_average_rating(self):
        total_rating = 0
        if len(self.books) > 0:
            for value in self.books.values():
                total_rating += value
                return total_rating / len(self.books)
        else:
            return total_rating

    def __repr__(self):
        return "User - {}  email: {}, books read: {}".format(self.name,
                                                             self.email, len(self.books))

    def __eq__(self, other_user):
        pass


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("You have changed your ISBN too, {}.".format(self.isbn))
        return self.isbn
    
    def add_rating(self, rating):
        if rating in range(0, 5):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    
    def get_average_rating(self):
        total_ratings = 0
        for rating in self.ratings:
            total_ratings += rating
        return total_ratings / len(self.ratings)
    
    def __hash__(self):
        return hash((self.title, self.isbn))
        
    def __eq__(self, other_user):
        pass


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{} by {}".format(self.title, self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level,
                                              self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(self, title, isbn):
        book = Book(title, isbn)
        self.books[book] = 0
        return book
    
    def create_novel(self, title, author, isbn):
        book_novel = Fiction(title, author, isbn)
        self.books[book_novel] = 0
        return book_novel
    
    def create_non_fiction(self, title, subject, level, isbn):
        book_non_fiction = Non_Fiction(title, subject, level, isbn)
        self.books[book_non_fiction] = 0
        return book_non_fiction
    
    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            self.users[email].read_book(email, rating)
            book.add_rating(rating)
            if book.title in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email: {}!".format(email))

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[user.email] = user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email, book.get_average_rating)
                
    def print_catalog(self):
        for key in self.books:
            print(key.title)

    def print_users(self):
        for user in self.users:
            print(user)
    
    def get_most_read_book(self):
        num_read_book = 0
        for book in self.books:
            if self.books[book] > num_read_book:
                num_read_book = self.books[book]
                most_read_book = book.title
        return most_read_book
        
    def highest_rated_book(self):
        book_rating = 0
        highest_rated_book = ""
        for book in self.books:
            if book.get_average_rating() > book_rating:
                book_rating = book.get_average_rating()
                highest_rated_book = book.title
        return highest_rated_book

    def most_positive_user(self):
        user_rating = 0
        most_positive_user = ""
        for user in self.users:
            if self.users[user].get_average_rating() > user_rating:
                user_rating = self.users[user].get_average_rating()
                most_positive_user = self.users[user].name
        return most_positive_user


