import re
from datetime import datetime 




class Admin:


    listOfAdmins=[]
    listOfLoggedInAdmins=[]


    def __init__(self):
        self.name=None
        self.email=None
        self.password=None




class User:
    listOfUsers=[]        
    listOfLoggedInUsers=[]


    def __init__(self):
        self.name=None
        self.phoneNumber=None
        self.email=None
        self.address=None
        self.password=None
        self.isActiveLogin=False
        self.orderHistory=None


          

class Food:


    foodList=[]


    def __init__(self):
        self.foodID=None
        self.foodName=None
        self.quantity=None
        self.unit=None
        self.price=None
        self.discount=None
        self.stock=None
     

    @classmethod 
    def showFoodListToUser(cls):
        if (User.listOfLoggedInUsers):
            for food in cls.foodList:
                if (food.stock>=food.quantity):
                    print(food.foodID,".",sep="",end=" ")
                    print(food.foodName,end=" ")    
                    print("(",food.quantity,food.unit,")",end=" ")
                    print("[INR",end="")
                    print(food.price,"]",sep="")
        else:
            print("Please, first login as a user")


    @classmethod 
    def showFoodListToAdmin(cls):
        if (Admin.listOfLoggedInAdmins):
            for food in cls.foodList:            
                print(food.foodID,".",sep="",end=" ")
                print(food.foodName,end=" ")    
                print("(",food.quantity,food.unit,")",end=" ")
                print("[INR",end="")
                print(food.price,"]",sep="",end=", ") 
                print("discount=",food.discount,"%",sep="",end=", ") 
                print("stock=",food.stock,food.unit,end=" ") 
                if (food.stock<food.quantity):
                    print("[",end="")
                    print("Currently unavailable for sale,please add some stock]",end=" ")
                print("") 
        else:
            print("Please, first login as admin")




class FoodOrderingApp:
    def __init__(self):
        self.default_admin=Admin()
        self.default_admin.name="default"
        self.default_admin.email="admin"
        self.default_admin.password="admin"
        Admin.listOfAdmins.append(self.default_admin)
        

    #ADMIN FUNCTIONALITIES 
    def loginAdmin(self):
        username=input("Enter your Email Id  :")
        password=input("Enter your password  :")
        for admin in Admin.listOfLoggedInAdmins:
            if(admin.email==username and admin.password==password):
                print(admin.name,"you are already logged in as admin")
                break
        else:
            for admin in Admin.listOfAdmins:                
                if(admin.email==username and admin.password==password):
                    print(admin.name,"your login is successful as admin")
                    Admin.listOfLoggedInAdmins.append(admin)
                    break
            else:
                print("This credentials are not valid.Please check it")


    def addFood(self):        
        if (Admin.listOfLoggedInAdmins):
            foodName=input("Enter name of the food   :")
            quantity=int(input("Enter the quantity of the food you want to set for one unit   :"))
            unit=input("Enter unit of the food   :")
            price=int(input("Enter price of one unit   :"))
            discount=int(input("Enter the discount percentage on the food   :"))
            stock=int(input("Enter the quantity of food you want to add"))
            for food in Food.foodList:
                if (food.foodName==foodName and food.unit==unit and food.price==price and food.discount==discount):
                    food.stock += stock
                    print(foodName, "is added successfully")
                    break
            else:    
                new_food=Food()
                if Food.foodList:
                    new_food.foodID = Food.foodList[len(Food.foodList)-1].foodID + 1
                else:
                    new_food.foodID=1
                new_food.foodName=foodName
                new_food.quantity=quantity
                new_food.unit=unit
                new_food.price=price 
                new_food.discount=discount
                new_food.stock=stock
                Food.foodList.append(new_food)
                print(foodName, "is added successfully")
        else:
            print("Please, first login as admin") 


    def editFood(self):        
        if (Admin.listOfLoggedInAdmins):
            foodID=int(input("Enter the food Id of the food you want to edit   :"))
            foodName=input("Enter the changed name   :")
            quantity=int(input("Enter the changed quantity   :"))
            unit=input("Enter the changed unit   :")
            price=int(input("Enter changed price   :"))
            discount=int(input("Enter the changed discount   :"))
            stock=int(input("Enter the changed stock   :"))
            for food in Food.foodList:
                if (food.foodID==foodID):
                    print(food.foodName, "is edited succesfully")
                    food.foodName=foodName
                    food.quantity=quantity
                    food.unit=unit
                    food.price=price
                    food.discount=discount
                    food.stock=stock
                    break
            else:
                print("This food is not available in our foodlist")    
        else:
            print("Please, first login as admin") 


    def removeFood(self):        
        if (Admin.listOfLoggedInAdmins):
            foodID=int(input("Enter food Id of the food which you want to remove    :"))
            for food in Food.foodList:
                if (food.foodID==foodID):
                    Food.foodList.remove(food)
                    print(food.foodName,"is removed successfully")
                    break
            else:
                print("This food is not available in our foodlist")    
        else:
            print("Please, first login as admin") 




    #USERS FUNCTIONALITIES
    def registerUser(self):
        name = input("Enter name of the user   :")        
        phoneNumber = input("Enter phone number of the user   :")
        email=input("Enter the Email Id of the user   :")
        while(re.search("^[a-zA-Z0-9]{1,30}@[a-zA-Z]{1,15}.[a-zA-Z]{2,3}$",email)==None):       
            print("Invalid email")
            email = input("Please enter again   :")
        address = input("Enter the address of the user   :")
        password = input("Enter the password of the user   :")
        for user in User.listOfUsers:
            if(user.email==email):
                print("There is already an account with this credentials")
                break
        else:
            newUser=User()
            newUser.name=name
            newUser.phoneNumber=phoneNumber
            newUser.email=email
            newUser.address=address
            newUser.password=password
            User.listOfUsers.append(newUser)
            print(newUser.name,"registered succesfully as user") 


    def loginUser(self): 
        email=input("Enter your Email Id   :")
        password=input("Enter your password   :")
        for user in User.listOfLoggedInUsers:
            if (user.email==email):
                print(user.name,"you are already logged in as user")
                break 
        else: 
            for user in User.listOfLoggedInUsers:
                user.isActiveLogin=False         
            for user in User.listOfUsers: 
                if(user.email==email and user.password==password):
                    print(user.name,"your login is successful as user")
                    User.listOfLoggedInUsers.append(user)
                    user.isActiveLogin=True
                    break 
            else:
                print("This credentials are not valid ,If you want you can register yourself") 


    def placeNewOrder(self):        
        if (Admin.listOfLoggedInAdmins):
            if (Food.foodList):
                if (User.listOfLoggedInUsers):
                    email=input("Enter your Email Id   :")
                    for user in User.listOfLoggedInUsers:
                        if (user.email==email):
                            Food.showFoodListToUser()  
                            orderedFood=input("Enter foodID in the form of a list   :") 
                            orderedFoodList=re.findall("[0-9]",orderedFood)
                            # print(orderedFoodList)
                        #checking ordered food can be order or not
                            isOrder=True
                            orderedFoodListFromSet=list(set(orderedFoodList))
                            orderedFoodStockList={}
                            for fooditem in orderedFoodListFromSet:
                                for food in Food.foodList:
                                    if (food.foodID==int(fooditem)):
                                        orderedFoodStockList[food.foodID]=food.stock
                            for fooditem in orderedFoodList:
                                for food in Food.foodList:
                                    if (food.foodID==int(fooditem)):
                                        if (orderedFoodStockList[food.foodID] >= food.quantity):
                                            orderedFoodStockList[food.foodID] -= food.quantity 
                                        else:
                                            print("Sorry",user.name,"Due to insufficient stock of",food.foodName,"your order can not be processed")          
                                            isOrder=False
                            #after checking
                            if (isOrder):
                                print("your ordered items are  :")
                                sum=0
                                for fooditem in orderedFoodList:
                                    for food in Food.foodList:
                                        if (food.foodID==int(fooditem)):
                                            print(food.foodID,".",sep="",end=" ")
                                            print(food.foodName,end=" ")    
                                            print("(",food.quantity,food.unit,")",end=" ")
                                            print("[INR",end="")
                                            print(food.price,"]",sep="")
                                            sum += (food.price*(1-(food.discount/100)))
                                print("Your bill will be",sum,"rs . Do you want to order, if yes then enter Y or enter N  :")
                                isOrdered=input() 
                                if (isOrdered=="Y"):
                                    print(user.name,", your order is placed successfully")
                                    for fooditem in orderedFoodList:
                                        for food in Food.foodList:
                                            if (food.foodID==int(fooditem)):                                            
                                                    food.stock -= food.quantity 
                                    if (user.orderHistory):
                                        user.orderHistory.append([orderedFoodList,sum,datetime.now()])
                                    else:
                                        user.orderHistory=[[orderedFoodList,sum,datetime.now()]]
                                else:
                                    print(user.name,"you didn't place any order")           
                            break
                    else:
                        print("Enter a valid email")
                else:
                    print("Please , First login as a user")
            else:
                print("There is no food in the food list, Please add some food")                
        else:
            print("Please , First login as an admin")


    def orderedHistory(self):
        if (User.listOfLoggedInUsers):
            email=input("Enter your Email Id   :")
            for user in User.listOfLoggedInUsers:
                if (user.email==email):
                    orderDetails=[]
                    if (user.orderHistory):                                       
                        for history in user.orderHistory:
                            details={}
                            details["fooditem"]=set()
                            for fooditem in history[0]:
                                for food in Food.foodList:
                                    if (food.foodID==int(fooditem)):
                                        details["fooditem"].add(food.foodName)
                            details["price"]=history[1]            
                            details["date"]=history[2]
                            orderDetails.append(details)                    
                        print("Order history of",user.name,orderDetails) 
                    else:
                        print(user.name,"your order history is empty")       
                break
            else:
                print("Enter a valid email")
        else:
            print("Please, First login as a user")        


    def activateLogin(self):
        if User.listOfLoggedInUsers:
            email=input("Enter your Email Id   :")
            for user in User.listOfLoggedInUsers:
                user.isActiveLogin=False
            for user in User.listOfLoggedInUsers:
                if (user.email==email):
                    print(user.name,"Your login is activated")
                    user.isActiveLogin=True
                    break
            else:
                print("There is no user with this email id")    
        else:
            print("There is no logged in user currently.Please log in as a user")


    def updateProfile(self):        
        print("By default it will update profile of current/last login user,to update profile of other user you have to first activate their login using activateLogin method" )
        if(User.listOfLoggedInUsers):
            name=input("Enter your updated name   :")
            phoneNumber=input("Enter your updated phone number   :")
            emailNew=input("Enter your updated Email Id   :")
            while(re.search("^[a-zA-Z0-9]{1,30}@[a-zA-Z]{1,15}.[a-zA-Z]{2,3}$",emailNew)==None):       
                print("Invalid email")
                emailNew = input("Please enter again   :")
            address=input("Enter your updated address")
            password=input("Enter your updated password   :")
            for user in User.listOfLoggedInUsers:
                if (user.isActiveLogin):
                    print(user.name,",Your profile is updated successfully")
                    user.name=name
                    user.phoneNumber=phoneNumber
                    user.email=emailNew
                    user.address=address
                    user.password=password 
                    break
            else:
                print("There is no user currently with active login.To update profile any user first activate their login with their email id")    
        else:
            print("Please,first login as a user")


     
                       
                


rajkumar=FoodOrderingApp()

print("0. exit from the app\n1.  rajkumar.loginAdmin()         ->for admin login(default email=admin and password=admin) \n2.  rajkumar.addFood()            ->for adding food\n3.  rajkumar.editFood()           ->for editing food details\n4.  Food.showFoodListToAdmin()    ->for showing list of food with all details to admin\n5.  rajkumar.removeFood()         ->for removing any food from foodlist\n6.  rajkumar.registerUser()       ->for registering any user\n7.  rajkumar.loginUser()          ->for login any user\n8.  rajkumar.placeNewOrder()      ->for placing any order\n9.  rajkumar.orderedHistory()     ->to see order history of any user\n10. rajkumar.updateProfile()      ->for updating user details\n11. rajkumar.activateLogin()      ->to activate login of any user\n12. Food.showFoodListToUser()     ->for showing list of food with details to user")

while True:
    try:
        Action=int(input("Enter a action  :"))
        if (Action==0):
            break
        elif (Action==1):
            rajkumar.loginAdmin()
        elif (Action==2):
            rajkumar.addFood()
        elif (Action==3):
            rajkumar.editFood()
        elif (Action==4):
            Food.showFoodListToAdmin()
        elif (Action==5):
            rajkumar.removeFood()
        elif (Action==6):
            rajkumar.registerUser()
        elif (Action==7):
            rajkumar.loginUser()
        elif (Action==8):
            rajkumar.placeNewOrder()
        elif (Action==9):
            rajkumar.orderedHistory()
        elif (Action==10):
            rajkumar.updateProfile()
        elif (Action==11):
            rajkumar.activateLogin()    
        elif (Action==12):
            Food.showFoodListToUser()
        else:
            print("Please enter a valid input")
    except:
        print("Please input a number")
    
    