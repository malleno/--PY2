BOOKS = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

class Library:
    def __init__(self, books: list = {}):
        self.books = books

    def get_next_book_id(self) -> int:
        if self.books == {}:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id) -> int:
        for idx, id_ in enumerate(self.books):
            # print(idx, self.books[idx].id_)
            if book_id == self.books[idx].id_:
                return idx
            else:
                raise ValueError("Книги с запрашиваемым id не существует")



if __name__ == '__main__':
    empty_library = Library() 
    print(empty_library.get_next_book_id()) 

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS 
    ]
    library_with_books = Library(books=list_books) 
    print(library_with_books.get_next_book_id()) 

    print(library_with_books.get_index_by_book_id(1)) 