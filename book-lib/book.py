# http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip
import csv
path = '/home/sanjay/BX-CSV-Dump/BX-Books.csv'
path= '/tmp/test'
class Book:
    def __init__(self,
                 isbn,
                 title,
                 author,
                 yop,
                 publisher,
                 image_small,
                 image_medium,
                 image_large
                 ):
        self.isbn=isbn
        self.title = title
        self.author= author
        self.yop = yop 
        self.publisher = publisher 
        self.image_small = image_small
        self.image_medium = image_medium
        self.image_large = image_large 
    
    def __repr__(self):
        return "<BOOK {cls.title} {cls.author}>".format(cls=self)
    @classmethod
    def from_dict(cls,data):
       return  cls(**data)

class BookIterator:
    def __init__(self,books):
        self.books = books
        self.next = 0
        self.end = len(self.books.collection)-1      
        
    def __iter__():
        return self 
    
    def __next__(self):
        if self.next < self.end:
            item = self.books.collection[self.next]
            self.next = self.next +1
            return item 
        else:
            raise StopIteration()
        
class BookCollection:
    def __init__(self):
        self.collection = []
    def add(self,book):
        self.collection.append(book)
        
    def __iter__(self):
        return BookIterator(self)
        
    def __repr__(self):
        return "Collection of %d boobks"%(len(self.collection))
  
def create_books_from_csv(path):
    books = BookCollection()
    with open(path) as csv_file:
           reader = csv.DictReader(csv_file,
                                   fieldnames=[
                                     'isbn',
                                     'title',
                                     'author',
                                     'yop',
                                     'publisher',
                                     'image_small',
                                     'image_medium',
                                     'image_large'
                                   ],
                                   delimiter=';',quotechar='"')
           for data in reader:
               book = Book.from_dict(data)
               books.add(book)
    return books 
    
    
    



books = create_books_from_csv(path)

for b in books:
    print(b)
