class Library:
    # Constructor
    def __init__(self, list, name):
        self.list = list
        self.name = name
        self.lendDict = {}

    def display_books(self):
        print("We have following books in the Library: ")
        for book in self.list:
            print(book)

    def lend_book(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book database has been updated. You can take your book now")
        else:
            print("The book has already been issued")

    def add_book(self, book):
        self.list.append(book)
        print("Book has been added to the book list")

    def return_book(self, book):
        self.lendDict.pop(book)
        print("The book has been returned")


if __name__ == '__main__':
    lib = Library(["Zero to One", "Sapiens", "How To Win Friends & Influence People", "Influence", "Algorithms"], "Central Lib")

    while(True):

        print("Welcome to the Library. Enter your choice to continue: ")
        print("1. Display book")
        print("2. Lend book")
        print("3. Add book")
        print("4. Return book")

        user_choice = int(input())

        if user_choice == 1:
            lib.display_books()

        elif user_choice == 2:
            user = input("Enter your name: ")
            book = input("Enter the name of the book you want to lend: ")
            lib.lend_book(user, book)

        elif user_choice == 3:
            book = input("Enter the book name ou want to add: ")
            lib.add_book(book)

        elif user_choice == 4:
            book = input("Enter the book name ou want to add: ")
            lib.return_book(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue: ")
        user_choice2 = ""

        while(user_choice2 != "q" and user_choice2 != "c"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
