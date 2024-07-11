class Book:
    """ A single book.
    """
    def __init__(self, name: str, pages: int) -> None:
        self.name= name
        self.pages = pages
    


class BooksStack:
    """ A stack of books.
    """
    def __init__(self) -> None:
        self.stack = []


    def add_book(self, book: type[Book]) -> None:
        self.stack.append(book)
        print(f"Livro adicionado: {book.name}")


    def remove_book(self) -> None:
        if self.stack:
            book = self.stack.pop()
            print(f"Livro removido: {book.name}")
        else:
            print("Nenhum livro na pilha.")


    def peek_top(self) -> type[Book]:
        if self.stack:
            top_book = self.stack.pop()
            self.stack.append(top_book)
            print(f"Livro no topo: {top_book.name}")
            return top_book
        else:
            print("Nenhum livro na pilha.")
    

    def list_all_books(self) -> None:
        if self.stack:
            print("Pilha de livros:")
            for book in reversed(self.stack):
                print(f"{book.name} \t {book.pages} páginas")
        else:
            print("Nenhum livro na pilha.")
        print("\n")

    
def main():
    try:
        print("\n")
        books_stack = BooksStack()
        book1 = Book("The Fellowship Of The Ring", 300)
        book2 = Book("The Two Towers", 280)
        book3 = Book("The Return Of The King", 360)

        books_stack.list_all_books()

        # add
        books_stack.add_book(book1)
        books_stack.add_book(book2)
        books_stack.peek_top()
        books_stack.list_all_books()

        # remove
        books_stack.remove_book()
        books_stack.peek_top()
        books_stack.list_all_books()

        # add
        books_stack.add_book(book3)
        books_stack.peek_top()
        books_stack.list_all_books()

    except Exception as e:
        print(f"Erro: {e}")


main()