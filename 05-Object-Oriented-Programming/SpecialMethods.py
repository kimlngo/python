class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # provide a str() method for string representation (i.e., toString() in Java)
    def __str__(self):
        return f'{self.title} by {self.author} - [{self.pages} pages]'
    
    # override the len method
    def __len__(self):
        return self.pages
    
    # del override - to be executed when the object is deleted
    def __del__(self):
        print('A book has been deleted')
    
b = Book('Python from zero to pro', 'Jose', 220)
print(b)
print(str(b))
print(len(b))

#delete an object
del b