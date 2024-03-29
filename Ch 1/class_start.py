class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None  # private variable
    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    def getbooklist():
        if Book.__booklist == None:
            Book.__list = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title

        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype



# TODO: access the class attribute
print("Book types: ", Book.get_book_types())

# TODO: Create some book instances
b1 = Book("Titlel", "HARDCOVER")
b2 = Book("Tittel", "COMIC")


# TODO: Use the static method to access a singleton object


