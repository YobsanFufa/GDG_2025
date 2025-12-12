class Library: 
    def add_books(self, books):
        self.add_books= books
    def show_books(self):
        return self.add_books
b1 = Library()
b1.add_books(input("Enter the books title you want to add: "))
print(b1.show_books())