# myprojects
#first project-   "Library management system"

class Library:
    def __init__(self,list,name):
        self.books=list
        self.name=name
        self.lenddict={}
    def display_book(self):
        return f"These are following books present in {self.name} \n {self.books}"

    def lend_book(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender-Book DataBase has been updated. Now you can take book Properly")
        else:
            print(f"Book has been issuesd by {self.lenddict[book]}")


    def add_book(self,book):
        self.books.append(book)
        print("Book has been added successfully")


    def return_book(self,book):
        self.books.pop(book)

if __name__ == '__main__':
    shubham=Library(["Physics","Chemistry","Maths","History","Geography"],"ShubhamLibrary")
    while True:
        print("Welcome to the Shubham Library!\n"
              "press 1 for display books\n"
              "press 2 for lend book\n"
              "press 3 for add book\n"`
              "press 4 for return book")

        user_choice1 = int(input())
        if user_choice1 == 1:
            print(shubham.display_book())

        elif user_choice1 == 2:
            book = input("enter a book name")
            user = input("enter your name")
            shubham.lend_book(user, book)

        elif user_choice1 == 3:
            book = input("which book do you want to add:")
            shubham.add_book(book)
        elif user_choice1 == 4:
            book = input("which book do you want to return:")
            shubham.return_book(book)
        else:
            print("invalid input !")

        print("\n1For Quit 'q'\n For Continues 'c'")
        user_choice2 = ""
        while (user_choice2!="q" and user_choice2!="c"):
            user_choice2=input()
            if user_choice2=="q":
                exit()

            else:
                continue




