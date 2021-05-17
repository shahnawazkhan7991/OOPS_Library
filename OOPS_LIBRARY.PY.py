#Create  a Library class
#display book
#lend book-(who owns the book if not present)
#add book
#return book

#ShahnawazLibrary = Library(listofbooks, library_name)

#dictionary (books-nameofperson)

#Create a main function and run an infinite while loop asking
# users for their input.

class Library:
    def __init__(self,list,name):
        self.bookList = list
        self.name = name
        self.lendDictionary = {}

    def displayBooks(self):
        print(f"we have following books in our library:{self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDictionary.keys():
            self.lendDictionary.update({book:user})
            print("Lender-Book database has been updated. uou can take the book now")
        else:
            print(f"Book is already being used by{self.lendDictionary[book]}")

    def addBook(self,book):
        self.bookList.append(book)
        print("Book has been to the book list")
    def returnBook(self,book):
        self.lendDictionary.pop(book)

if __name__ == '__main__':
    shahnawaz = Library(['Python','Attitude is everything','Rich Dad poor Dad','Finding onself','MYsql by jai chitkara'],"Shahanfitness")

    while(True):
        print(f"Welcome to the {shahnawaz.name}library.Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice= int(input())

        if user_choice == 1:
            shahnawaz.displayBooks()

        elif user_choice == 2:
            book=input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            shahnawaz.lendBook(user,book)

        elif user_choice ==3:
            book = input("Enter the name of the book you want to add:")
            shahnawaz.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")

            shahnawaz.returnBook(book)

        else:
            print("Not a valid answer")

        print("Press q to quit and c to continue")
        user_choice2 = " "
        while(user_choice2!="c"and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue







