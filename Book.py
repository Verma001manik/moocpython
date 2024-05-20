class Book:
    def __init__(self, name, author, genre, year) :

        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

def older_book(book1: Book, book2: Book):
    if(book1.year> book2.year):
        print(f"{book2.name} is older , it was published in {book2.year}")
    else : 
        print(f"{book1.name} is older , it was published in {book1.year}")

def books_of_genre(books: list, genre : str):
    desired_genre = []
    for book in books:
        if(book.genre == genre):
            desired_genre.append(book)
    return desired_genre
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

print("Books in the crime genre:")
for book in books_of_genre(books, "crime"):
    print(f"{book.author}: {book.name}")