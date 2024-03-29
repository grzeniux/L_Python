
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"        # " __ "are invisible outside the class

    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price


    def setdiscount(self, amount):
            self._discount = amount


b1 = Book("Brave New World", "Leo Tolsoy", 1225, 39.95)  # objects
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95 )

# print(b1.getprice())
#
# print(b2.getprice())
# b2.setdiscount(0.25)
# print(b2.getprice())

print(b2.__secret)          # " __ "are invisible outside the class
print(b2._Book__secret)     # it is not a perfect mechanism because it can be done like this



