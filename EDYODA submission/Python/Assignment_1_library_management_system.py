import re
from datetime import datetime, timedelta


class Admin:
    admins=[]
    logged_in_admins=[]

    def __init__(self):
        self.name=None
        self.username=None
        self.password=None


class Borrower:
    borrowers=[]
    logged_in_borrowers=[]

    def __init__(self):
        self.name=None
        self.dob=None
        self.contact_no=None
        self.username=None
        self.password=None
        self.borrowedBook=None
        self.oldBorrowedBook=None


class Book:
    total_books=[]
    deleted_books=[]

    def __init__(self):
        self.bookID=None
        self.bookTitle=None
        self.authorName=None
        self.totalPages=None
        self.numberOfCopies=None
        self.numberOfAvailableCopies=None
        self.isbn=None
        self.publishedYear=None
        self.borrowHistory=None
        self.oldBorrowHistory=None

    @classmethod
    def bookDetailsOfEachBorrowedBook(cls):
        detailList=[]
        for book in cls.total_books:
            if (book.borrowHistory):                                    
                details={}   
                details["bookID"] = book.bookID
                details["bookTitle"]=book.bookTitle
                details["authorName"]=book.authorName
                details["totalPages"]=book.totalPages
                details["numerOfCopies"]=book.numberOfCopies
                details["numberOfAvailableCopies"]=book.numberOfAvailableCopies
                details["isbn"]=book.isbn
                details["publishedYear"]=book.publishedYear
                details["borrowers"]=[]
                for history in book.borrowHistory:                    
                    information={}
                    information["emailId"]=history[0].username
                    information["numberOfBorrowedCopies"]=history[1]
                    information["borrowDate"]=history[2]
                    information["returnDate"]=history[3]
                    details["borrowers"].append(information)
                # print(details)
                detailList.append(details)
        if (detailList):
            return detailList
        else:
            return "currently no book is borrowed"        
                

class Library:

    #define constructor
    def __init__(self):
        self.default_admin=Admin()
        self.default_admin.name="default"
        self.default_admin.username="admin"
        self.default_admin.password="admin"
        Admin.admins.append(self.default_admin)

    #ADMIN FUNCTIONALITIES 
    def login_admin(self):
        username=input("Enter your username  :")
        password=input("Enter your password  :")
        for admin in Admin.logged_in_admins:
            if(admin.username==username and admin.password==password):
                print(admin.name,"you are already logged in as admin")
                break
        else:
            for admin in Admin.admins:                
                if(admin.username==username and admin.password==password):
                    print(admin.name,"your login is successful as admin")
                    Admin.logged_in_admins.append(admin)
                    break
            else:
                print("This credentials are not valid , If you want you can contact admin to create your account")                             
               
    def create_admin(self):        
        if (Admin.logged_in_admins): 
            name=input("Enter your name  :")
            username=input("Enter your username  :")
            while(re.search("^[a-zA-Z0-9]{1,30}@[a-zA-Z]{1,15}.[a-zA-Z]{2,3}$",username)==None):       
                print("Invalid email")
                username = input("Please enter again   :")
            password=input("Enter your password  :")           
            for admin in Admin.admins:
                if(admin.username==username and admin.password==password):
                    print("There is already an account with this credentials")
                    break
            else:
                new_admin=Admin()
                new_admin.name=name    
                new_admin.username=username
                new_admin.password=password
                Admin.admins.append(new_admin)
                print(new_admin.name,"added succesfully as admin") 
        else:
            print("Please, First login as admin") 

    def create_borrower(self):        
        if (Admin.logged_in_admins):
            name=input("Enter your name  :")
            dob=input("Enter your date of birth  :")
            contact_no=input("Enter your contact no  :")
            email_id=input("Enter your Email Id  :")
            while(re.search("^[a-zA-Z0-9]{1,30}@[a-zA-Z]{1,15}.[a-zA-Z]{2,3}$",email_id)==None):       
                print("Invalid email")
                email_id = input("Please enter again   :")
            password=input("Enter your password  :")            
            for borrower in Borrower.borrowers:
                if(borrower.username==email_id):
                    print("There is already an account with this credentials")
                    break
            else:
                new_borrower=Borrower()
                new_borrower.name=name
                new_borrower.dob=dob
                new_borrower.contact_no=contact_no
                new_borrower.username=email_id
                new_borrower.password=password
                Borrower.borrowers.append(new_borrower)
                print(new_borrower.name,"added succesfully as borrower") 
        else:
            print("Please, First login as admin")

    def viewBookDetailsBorrowingHistoryBasedOnBookID(self):
        if (Admin.logged_in_admins):
            if (Book.total_books):
                bookID=int(input("Enter your book Id  :"))
                detailList=[]
                for book in Book.total_books:
                    if (book.bookID==bookID):                                        
                        details={}   
                        details["bookID"] = book.bookID
                        details["bookTitle"]=book.bookTitle
                        details["authorName"]=book.authorName
                        details["totalPages"]=book.totalPages
                        details["numberOfCopies"]=book.numberOfCopies
                        details["numberOfAvailableCopies"]=book.numberOfAvailableCopies
                        details["isbn"]=book.isbn
                        details["publishedYear"]=book.publishedYear
                        if (book.borrowHistory):
                            details["currentborrowers"]=[]
                            for history in book.borrowHistory:                            
                                information={}
                                information["emailId"]=history[0].username
                                information["numberOfBorrowedCopies"]=history[1]
                                information["borrowDate"]=history[2]
                                information["returnDate"]=history[3]
                                details["currentborrowers"].append(information)
                        if (book.oldBorrowHistory):
                            details["pastborrowers"]=[]
                            for history in book.oldBorrowHistory:                            
                                information={}
                                information["emailId"]=history[0].username
                                information["numberOfBorrowedCopies"]=history[1]
                                information["borrowDate"]=history[2]
                                information["returnDate"]=history[3]
                                details["pastborrowers"].append(information)                    
                        detailList.append(details)
                if (detailList):
                    print(detailList)
                else:
                    print("book is not found")  
            else:
                print("There is no book in the library")   
        else:
            print("Please, first login as an admin")        

    def add_books(self):
        if (Admin.logged_in_admins):
            BookTitle=input("Enter your book title  :")
            AuthorName=input("Enter author name of the book  :")
            TotalPages=int(input("Enter total number of pages of the book  :"))
            NumberOfCopies=int(input("Enter number of copies you want to add  :"))
            PublishedYear=input("Enter published year of the book  :")
            ISBN=input("Enter isbn of the book  :")
            if (all([any(list(map(lambda x:x.bookTitle==BookTitle,Book.total_books))),any(list(map(lambda x:x.authorName==AuthorName,Book.total_books))),any(list(map(lambda x:x.totalPages==TotalPages,Book.total_books))),any(list(map(lambda x:x.publishedYear==PublishedYear,Book.total_books)))])):
                while(re.search("^[0-9]{13}$",ISBN)==None or any(list(map(lambda x:x.isbn==ISBN,Book.total_books)))==False):
                        print("ISBN is not correct or not matched with your previously added same book,please Enter again")
                        ISBN=input("Enter isbn of the book  :")
            else:
                while(re.search("^[0-9]{13}$",ISBN)==None or any(list(map(lambda x:x.isbn==ISBN,Book.total_books)))):
                        print("ISBN is not correct or may be it matched with any other book's isbn,please Enter again")
                        ISBN=input("Enter isbn of the book  :")            
            for book in Book.total_books:
                if (book not in Book.deleted_books):
                    if (book.bookTitle==BookTitle and book.authorName==AuthorName and book.totalPages==TotalPages and book.isbn==ISBN and book.publishedYear==PublishedYear):
                        book.numberOfCopies += NumberOfCopies
                        book.numberOfAvailableCopies += NumberOfCopies
                        print("Book is added successfully")
                        break
                else:
                    print("This book already deleted, you can't add this book")
            else:    
                new_book=Book()
                if Book.total_books:
                    new_book.bookID = Book.total_books[len(Book.total_books)-1].bookID + 1
                else:
                    new_book.bookID=1
                new_book.bookTitle=BookTitle
                new_book.authorName=AuthorName
                new_book.totalPages=TotalPages
                new_book.numberOfCopies=NumberOfCopies 
                new_book.numberOfAvailableCopies=NumberOfCopies                
                new_book.isbn=ISBN             
                new_book.publishedYear=PublishedYear
                print("Book is added successfully")
                Book.total_books.append(new_book)
        else:
            print("Please, First login as admin") 

    def edit_book(self):
        if (Admin.logged_in_admins):
            if(Book.total_books):
                BookID=int(input("Enter book id of the book you want to edit  :"))                
                for book in Book.total_books:
                    if (book not in Book.deleted_books):
                        if(book.bookID==BookID):
                            if (book.numberOfCopies == book.numberOfAvailableCopies):
                                BookTitle=input("Enter your book title  :")
                                AuthorName=input("Enter author name of the book  :")
                                TotalPages=int(input("Enter total number of pages of the book  :"))
                                NumberOfCopies=int(input("Enter number of copies you want to add  :"))
                                ISBN=input("Enter isbn of the book  :")
                                PublishedYear=input("Enter published year of the book  :")
                                difference=book.numberOfCopies - book.numberOfAvailableCopies
                                book.bookTitle=BookTitle
                                book.authorName=AuthorName
                                book.totalPages=TotalPages
                                book.numberOfCopies=NumberOfCopies
                                book.numberOfAvailableCopies=NumberOfCopies-difference
                                book.isbn=ISBN
                                book.publishedYear=PublishedYear
                                print("details of book are editted successfully")
                            else:
                                print("you can't edit this book as some of these books are already issued")
                            break
                    else:
                        print("You can't edit any deleted book")
                        break
                else:
                    print("book is not found")
            else:
                print("There is currently no book to edit")
        else:
            print("Please, login as an admin")

    def delete_book(self):
        if (Admin.logged_in_admins):
            if(Book.total_books):
                BookID=int(input("Enter book id of the book you want to delete  :"))
                for book in Book.total_books:
                    if (book not in Book.deleted_books):
                        if(book.bookID==BookID):
                            if (book.numberOfCopies == book.numberOfAvailableCopies):
                                # Book.total_books.remove(book)
                                book.numberOfCopies=0
                                book.numberOfAvailableCopies=20
                                Book.deleted_books.append(book)
                                print("book is deleted successfully")
                            else:
                                print("you can't delete this book as some of these books are already issued")
                            break
                    else:
                        print("This book is already deleted")
                        break
                else:
                    print("book is not found")
            else:
                print("There is currently no book to delete")
        else:
            print("Please, login as an admin")            

    def listOfAllBorrowersAndTheirDetails(self):
        if (Admin.logged_in_admins):
            if (Borrower.borrowers):
                detailList=[]
                for borrower in Borrower.borrowers:                                                        
                    details={}   
                    details["name"] = borrower.name
                    details["dob"]=borrower.dob
                    details["contact_no"]=borrower.contact_no
                    details["username"]=borrower.username
                    details["password"]=borrower.password
                    if (borrower.borrowedBook):
                        details["currentlyBorrowed"]=[]
                        for book in borrower.borrowedBook:                            
                            for history in book.borrowHistory:
                                if (history[0]==borrower): 
                                    information={}
                                    information["bookTitle"]=book.bookTitle
                                    information["borrowDate"]=history[2]
                                    details["currentlyBorrowed"].append(information)
                    else:
                        details["currentlyBorrowed"]=[]
                    if (borrower.oldBorrowedBook):
                        details["pastBorrowed"]=[]
                        for book in borrower.oldBorrowedBook:                            
                            for history in book.oldBorrowHistory:
                                if (history[0]==borrower):
                                    information={}
                                    information["bookTitle"]=book.bookTitle
                                    information["borrowDate"]=history[2]
                                    details["pastBorrowed"].append(information)
                    else:
                        details["pastBorrowed"]=[]                
                    # print(details)
                    detailList.append(details)                
                print(detailList)
            else:
                print("There is no borrower currently registered")        
        else:
            print("Please, first login as an admin")



    #BORROWER FUNCTIONALITIES
    def register_borrower(self):
        name=input("Enter your name  :")
        dob=input("Enter your date of birth  :")
        contact_no=input("Enter your contact no  :")
        email_id=input("Enter your Email Id  :")
        while(re.search("^[a-zA-Z0-9]{1,30}@[a-zA-Z]{1,15}.[a-zA-Z]{2,3}$",email_id)==None):       
                print("Invalid email")
                email_id = input("Please enter again   :")
        password=input("Enter your password  :")           
        for borrower in Borrower.borrowers:
            if(borrower.username==email_id):
                print("There is already an account with this credentials")
                break
        else:
            new_borrower=Borrower()
            new_borrower.name=name
            new_borrower.dob=dob
            new_borrower.contact_no=contact_no
            new_borrower.username=email_id
            new_borrower.password=password
            Borrower.borrowers.append(new_borrower)
            print(new_borrower.name,"registered succesfully as borrower") 

    def login_borrower(self):
        if (Borrower.borrowers):
            username=input("Enter your Email Id  :") 
            password=input("Enter your password  :")
            for borrower in Borrower.logged_in_borrowers:
                if (borrower.username==username and borrower.password==password):
                    print(borrower.name,"you are already logged in borrower")
                    break 
            else:          
                for borrower in Borrower.borrowers: 
                    if(borrower.username==username and borrower.password==password):
                        print(borrower.name,"your login is successful as borrower")
                        Borrower.logged_in_borrowers.append(borrower)
                        break 
                else:
                    print("This credentials are not valid ,If you want you can register yourself or contact admin to create your account")
        else:
            print("There is currently no borrower registerd")        

    def borrow_book(self):
        if (Admin.logged_in_admins):
            if (Borrower.logged_in_borrowers):
                email_id=input("Enter your Email Id  :")
                for borrower in Borrower.logged_in_borrowers:                    
                    if (borrower.username == email_id):
                        print("welcome",borrower.name)
                        BookID=int(input("Enter your book id  :"))
                        for book_no in range(len(Book.total_books)):
                            if (Book.total_books[book_no] not in Book.deleted_books):
                                if (Book.total_books[book_no].bookID==BookID):
                                    if (Book.total_books[book_no].numberOfAvailableCopies >= 1):
                                        if (borrower.borrowedBook):
                                            borrower.borrowedBook.append(Book.total_books[book_no])
                                        else:
                                            borrower.borrowedBook = [(Book.total_books[book_no])]
                                        Book.total_books[book_no].numberOfAvailableCopies -= 1
                                        Book.total_books[book_no].borrower=borrower
                                        print(Book.total_books[book_no].bookTitle,"is issued to",borrower.name)
                                        if(Book.total_books[book_no].borrowHistory != None):
                                            Book.total_books[book_no].borrowHistory.append([borrower,1,datetime.now(),(datetime.now()+timedelta(days=14))])
                                        else:
                                            Book.total_books[book_no].borrowHistory=[[borrower,1,datetime.now(),(datetime.now()+timedelta(days=14))]]      
                                    else:
                                        print("Sorry, This book is not available for now")
                                    break
                            else:
                                print("This book is already deleted") 
                                break   
                        else:
                            print("There is no book available with this bookid")
                        break        
                else:
                    print("There is no borrower present with this email id")
            else:
                print("There is no borrower currently logged in .")
        else:
            print("There is no admin currently logged in.Please,First login as admin")

    def return_book(self):
        if (Admin.logged_in_admins):
            if (Borrower.logged_in_borrowers):
                email_id=input("Enter your Email Id  :")
                for borrower in Borrower.logged_in_borrowers:
                    if (borrower.username == email_id):
                        BookID=int(input("Enter your Book Id  :"))
                        for book_no in range(len(Book.total_books)):
                            if (Book.total_books[book_no].bookID==BookID):
                                if (Book.total_books[book_no].borrowHistory):
                                    for history in Book.total_books[book_no].borrowHistory:
                                        if(history[0]==borrower and history[1]==1 and history[3]>=datetime.now()):
                                            Book.total_books[book_no].numberOfAvailableCopies += 1
                                            Book.total_books[book_no].borrowHistory.remove(history)
                                            if (Book.total_books[book_no].oldBorrowHistory==None):
                                                Book.total_books[book_no].oldBorrowHistory=[history]
                                            else:
                                                Book.total_books[book_no].oldBorrowHistory.append(history)
                                            borrower.borrowedBook.remove(Book.total_books[book_no])
                                            if (borrower.oldBorrowedBook==None):
                                                borrower.oldBorrowedBook = [Book.total_books[book_no]]
                                            else:                                            
                                                borrower.oldBorrowedBook.append(Book.total_books[book_no])                                            
                                            print(borrower.name,"your book is succesfully returned")
                                        elif(history[0]==borrower and history[1]==1 and history[3]<datetime.now()):
                                            Book.total_books[book_no].numberOfAvailableCopies += 1
                                            Book.total_books[book_no].borrowHistory.remove(history)
                                            if (Book.total_books[book_no].oldBorrowHistory==None):
                                                Book.total_books[book_no].oldBorrowHistory=[history]
                                            else:
                                                Book.total_books[book_no].oldBorrowHistory.append(history)
                                            borrower.borrowedBook.remove(Book.total_books[book_no])                                            
                                            if (borrower.oldBorrowedBook==None):
                                                borrower.oldBorrowedBook = [Book.total_books[book_no]]
                                            else:                                            
                                                borrower.oldBorrowedBook.append(Book.total_books[book_no])                                             
                                            print(borrower.name,"It's more than 14 days . So, you have to pay fine of 100rs")
                                            print(borrower.name,"your book is succesfully returned")
                                        else:
                                            print("Sorry,",borrower.name,"this book is not issued to you")
                                else:
                                    print("This book is not borrowed")            
                                break
                        else:
                            print("There is no book available with this bookid")
                        break        
                else:
                    print("There is no borrower present with this email id")
            else:
                print("There is no borrower currently logged in .")
        else:
            print("There is no admin currently logged in.Please,First login as admin")

    def showCurrentlyBorrowedBooks(self):
        if (Borrower.logged_in_borrowers):
            detailList=[]
            for book in Book.total_books:
                if (book.borrowHistory):
                    details={}   
                    details["bookTitle"]=book.bookTitle
                    details["remaining time"]=[]
                    for history in book.borrowHistory:                        
                        details["remaining time"].append((history[3]-datetime.now()))               
                    detailList.append(details)
            if (detailList):
                print(detailList)
            else:
                print("currently no book is borrowed")   
        else:
            print("Please, First login as borrower")        

    def bookDetailsOfEachBorrowedBook(self):
        if (Borrower.logged_in_borrowers):
            print(Book.bookDetailsOfEachBorrowedBook())
        else:
            print("Please, First login as borrower")

    def showBorrowingHistory(self):
        if (Borrower.logged_in_borrowers):
            detailList=[]
            for book in Book.total_books:
                if (book.oldBorrowHistory):                                        
                    details={}   
                    details["bookID"] = book.bookID
                    details["bookTitle"]=book.bookTitle
                    details["authorName"]=book.authorName
                    details["totalPages"]=book.totalPages
                    details["numberOfCopies"]=book.numberOfCopies
                    details["numberOfAvailableCopies"]=book.numberOfAvailableCopies
                    details["isbn"]=book.isbn
                    details["publishedYear"]=book.publishedYear
                    details["borrowers"]=[]
                    for history in book.oldBorrowHistory:                        
                        information={}
                        information["emailId"]=history[0].username
                        information["numberOfBorrowedCopies"]=history[1]
                        information["borrowDate"]=history[2]
                        information["returnDate"]=history[3]
                        details["borrowers"].append(information)
                    # print(details)
                    detailList.append(details)
            if (detailList):
                print(detailList)
            else:
                print("currently no book is borrowed/returned") 
        else:
            print("Please, First login as borrower")
               
                        


rajkumar=Library()

print("0.  To exit from the app\n1.  rajkumar.login_admin()                                 ->To login into the app for Admin(default username and password is admin)\n2.  rajkumar.create_admin()                                ->To create an Admin\n3.  rajkumar.create.borrower()                             ->To create a borrower\n4.  rajkumar.viewBookDetailsBorrowingHistoryBasedOnBookID()->To see book details and borrowing history based on book id\n5.  rajkumar.add_books()                                   ->To add books in the book list\n6.  rajkumar.edit_book()                                   ->To edit details of any book based on book id\n7.  rajkumar.delete_book()                                 ->To delete any book based on book id\n8.  rajkumar.listOfAllBorrowersAndTheirDetails()           ->To list all borrowers and view their details\n9.  rajkumar.borrow_book()                                 ->To borrow a book using book Id and borrower's email id\n10. rajkumar.return_book()                                 ->To return a book using book Id and borrower's email id\n11. rajkumar.register_borrower()                           ->To register a borrower\n12. rajkumar.login_borrower()                              ->To login a borrower\n13. rajkumar.showCurrentlyBorrowedBooks()                  ->To see currently borrowed books with remaining time\n14. rajkumar.bookDetailsOfEachBorrowedBook()               ->To view book details of each borrowed book\n15. rajkumar.showBorrowingHistory()                        ->To view past borrowing history")


while True:
    try:
        Action=int(input("Enter a action  :"))
        if (Action==0):
            break
        elif (Action==1):
            rajkumar.login_admin()
        elif (Action==2):
            rajkumar.create_admin()
        elif (Action==3):
            rajkumar.create_borrower()
        elif (Action==4):
            rajkumar.viewBookDetailsBorrowingHistoryBasedOnBookID()
        elif (Action==5):
            rajkumar.add_books()
        elif (Action==6):
            rajkumar.edit_book()
        elif (Action==7):
            rajkumar.delete_book()
        elif (Action==8):
            rajkumar.listOfAllBorrowersAndTheirDetails()
        elif (Action==9):
            rajkumar.borrow_book()
        elif (Action==10):
            rajkumar.return_book()
        elif (Action==11):
            rajkumar.register_borrower()    
        elif (Action==12):
            rajkumar.login_borrower()
        elif (Action==13):
            rajkumar.showCurrentlyBorrowedBooks() 
        elif (Action==14):
            rajkumar.bookDetailsOfEachBorrowedBook()
        elif (Action==15):
            rajkumar.showBorrowingHistory()  
        else:
            print("Please enter a valid input")
    except:
        print("Please input a number")
