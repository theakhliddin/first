"""class Pet:
    __slots__ = ['__species', '__name']
    def __init__(self, species, name):
        self.__species = species
        self.__name = name"""

class Book:

    def __init__(self, title, author, nm_pages):
        self.title = title
        self.author = author
        self.nm_pages = nm_pages

def __str__(self):
    return self.title + " by " + self.author + ", " + str(self.nm_pages) + " pages"
def __repr__(self):
    return "Book" + self.title + ", " + self.author + ", " + str(self)
def __gt__(self, other):
    return self.nm_pages > other.nm_pages
def __eq__(self, other):
    if type(self) == type(other):
        return self.title == other.title and self.author == other.author and self.nm_pages == other.nm
    else:
        return False
def __ne__(self, other):
    return not self.__eq__(other)
def __hash__(self):
    return self.title.__hash__() + self.author.__hash__() + self.nm_pages.__hash__()
def get
def main():
    book1 = Book("Python Programming", "John Smith", 300)
    book2 = Book("Discipline", "John MOrgan", 400)
    print(book1)
    print(repr(book1))
    print(book1 < book2)
    print(book1 > book2)
    print(book1 == book2)
    print(book1 != book2)


main()