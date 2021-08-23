workoutRegimens=[{"lowerBMI":0,"upperBMI":18.49,"Mon":"Chest","Tue":"Biceps","Wed":"Rest","Thu":"Back","Fri":"Triceps","Sat":"Rest","Sun":"Rest"},{"lowerBMI":18.5,"upperBMI":24.99,"Mon":"Chest","Tue":"Biceps","Wed":"Cardio/Abs","Thu":"Back","Fri":"Triceps","Sat":"Legs","Sun":"Rest"},{"lowerBMI":25,"upperBMI":29.99,"Mon":"Chest","Tue":"Biceps","Wed":"Abs/Cardio","Thu":"Back","Fri":"Triceps","Sat":"Legs","Sun":"Cardio"},{"lowerBMI":30,"upperBMI":50,"Mon":"Chest","Tue":"Biceps","Wed":"Cardio","Thu":"Back","Fri":"Triceps","Sat":"Cardio","Sun":"Cardio"}]

class Member:
    members=[]

    def __init__(self):
        self.fullName=None
        self.age=None
        self.gender=None
        self.mobileNumber=None
        self.email=None
        self.BMI=None
        self.membershipDuration=None
        self.workRegimen=None

        

class SuperUser:
    superusers=[]
    loggedinSuperusers=[]

    def __init__(self):
        self.name=None
        self.username=None
        self.password=None


class Gym:
    def __init__(self):
        self.defaultSuperuser=SuperUser()
        self.defaultSuperuser.name="default"
        self.defaultSuperuser.username="admin"
        self.defaultSuperuser.password="admin"
        SuperUser.superusers.append(self.defaultSuperuser)
    
    def loginSuperuser(self):        
        username=input("Enter username  :")
        password=input("Enter password  :")
        for superuser in SuperUser.loggedinSuperusers:
            if superuser.username==username:
                print("Superuser is already logged in")
                break
        else:
            for superuser in SuperUser.superusers:
                if (superuser.username==username and superuser.password==password):
                    print("superuser logged in succesfully")
                    SuperUser.loggedinSuperusers.append(superuser)
                    break
            else:
                print("Invalid credentials")


    def createMember(self):
        if SuperUser.loggedinSuperusers:
            MobileNumber=input("Enter your mobile number  :")                       
            for member in Member.members:
                if member.mobileNumber==MobileNumber:
                    print("Member already exists")
                    break
            else:
                newMember=Member()  
                Member.members.append(newMember)      
                newMember.fullName=input("Enter your Full name  :")
                newMember.age=int(input("Enter your age  :"))
                newMember.gender=input("Enter your gender  :")
                newMember.mobileNumber=MobileNumber
                newMember.email=input("Enter your email id  :")
                BMI=int(input("Enter your BMI  :"))
                newMember.BMI=BMI
                newMember.membershipDuration=int(input("Enter your membership duration in month  :"))
                print("New member is created")
                for regimen in workoutRegimens:
                    if (BMI>=regimen["lowerBMI"] and BMI<=regimen["upperBMI"]):
                        newMember.workRegimen=regimen
                        break
        else:
            print("currently, there is no superuser active.If you are superuser please login as superuser")


    def viewMember(self):
        if SuperUser.loggedinSuperusers:
            if Member.members:
                MobileNumber=input("Enter your mobile number  :")
                for member in Member.members:
                    if member.mobileNumber==MobileNumber:
                        print("FullName =",member.fullName)
                        print("Age =",member.age)
                        print("Gender =",member.gender)
                        print("MobileNumber =",member.mobileNumber)
                        print("Email =",member.email)
                        print("BMI =",member.BMI)
                        print("MemberShipDuration =",member.membershipDuration)
                        break
                else:
                    print("Member not found.Please, check the mobile number")    
            else:
                print("Currently there is no member in the gym")
        else:
            print("currently, there is no superuser active.If you are superuser please login as superuser")

    def deleteMember(self):
        if SuperUser.loggedinSuperusers:
            if Member.members:
                MobileNumber=input("Enter your mobile number  :")
                for member in Member.members:
                    if member.mobileNumber==MobileNumber:
                        Member.members.remove(member)
                        print("member is deleted successfully")
                        break
                else:
                    print("Member not found.Please, check the mobile number")    
            else:
                print("Currently there is no member in the gym")
        else:
            print("currently, there is no superuser active.If you are superuser please login as superuser")

    def updateMember(self):
        if SuperUser.loggedinSuperusers:
            if Member.members:
                MobileNumber=input("Enter your mobile number  :")
                for member in Member.members:
                    if member.mobileNumber==MobileNumber:
                        inputData=input("Enter E to extend your membership or I to invoke your membership")        
                        if inputData=="E":
                            month=int(input("Enter for how many month you want to extend your membership"))
                            member.membershipDuration+=month
                            print("membership extend successfully for",month,"months")

                        elif inputData=="I":
                            Member.members.remove(member)
                            print("Membership invoked successfully")
                            return
                        print("if you want to update other details,then type F for name change , A for age,G for gender,M for mobile number,E for email,B for BMI else 0 for exit")
                        inputdata=input("Enter here  :")
                        while True:
                            if (inputdata=="F"):
                                member.fullName=input("Enter your updated full name")
                            elif (inputdata=="A"):
                                member.age=int(input("Enter your updated age"))
                            elif (inputdata=="G"):
                                member.gender=int(input("Enter your updated Gender"))
                            elif (inputdata=="M"):
                                member.mobileNumber=int(input("Enter your updated mobile number"))
                            elif (inputdata=="E"):
                                member.email=int(input("Enter your updated email"))
                            elif (inputdata=="B"):
                                member.BMI=int(input("Enter your updated BMI"))
                            elif (inputdata=="0"):
                                break
                            inputdata=input("Enter another input  :")
                        break
                else:
                    print("Member not found.Please, check the mobile number")    
            else:
                print("Currently there is no member in the gym")
        else:
            print("currently, there is no superuser active.If you are superuser please login as superuser")

    def createRegimen(self):
        if SuperUser.loggedinSuperusers:
            count=0
            lowerBMI=float(input("Enter lower BMI  :"))
            upperBMI=float(input("Enter upper BMI  :"))
            for regimenNO in range(len(workoutRegimens)):
                if (lowerBMI>workoutRegimens[regimenNO]["upperBMI"] and lowerBMI<workoutRegimens[regimenNO+1]["lowerBMI"]):
                    workoutRegimens.insert(regimenNO+1,{})
                    workoutRegimens[regimenNO+1]["lowerBMI"]=lowerBMI
                    workoutRegimens[regimenNO+1]["upperBMI"]=upperBMI
                    workoutRegimens[regimenNO+1]["Mon"]=input("Enter workout regimen for monday :")
                    workoutRegimens[regimenNO+1]["Tue"]=input("Enter workout regimen for tuesday :")
                    workoutRegimens[regimenNO+1]["Wed"]=input("Enter workout regimen for wednesday :")
                    workoutRegimens[regimenNO+1]["Thu"]=input("Enter workout regimen for thursday :")
                    workoutRegimens[regimenNO+1]["Fri"]=input("Enter workout regimen for friday :")
                    workoutRegimens[regimenNO+1]["Sat"]=input("Enter workout regimen for saturday :")
                    workoutRegimens[regimenNO+1]["Sun"]=input("Enter workout regimen for sunday :")
                    workoutRegimens[regimenNO]["upperBMI"]=lowerBMI-0.01
                    workoutRegimens[regimenNO+2]["lowerBMI"]=upperBMI+0.01
                    return
            for regimen in workoutRegimens:
                if (regimen["lowerBMI"]<=lowerBMI and regimen["upperBMI"]<=lowerBMI):
                    pass
                elif (regimen["lowerBMI"]<=lowerBMI or regimen["upperBMI"]<=lowerBMI):
                    regimen["upperBMI"]=lowerBMI-0.01
                    break
                count+=1
            for regimen in workoutRegimens:
                if (regimen["lowerBMI"]>upperBMI or regimen["upperBMI"]>upperBMI):
                    regimen["lowerBMI"]=upperBMI+0.01
                    break
            workoutRegimens.insert(count+1,{})
            workoutRegimens[count+1]["lowerBMI"]=lowerBMI
            workoutRegimens[count+1]["upperBMI"]=upperBMI
            workoutRegimens[count+1]["Mon"]=input("Enter workout regimen for monday :")
            workoutRegimens[count+1]["Tue"]=input("Enter workout regimen for tuesday :")
            workoutRegimens[count+1]["Wed"]=input("Enter workout regimen for wednesday :")
            workoutRegimens[count+1]["Thu"]=input("Enter workout regimen for thursday :")
            workoutRegimens[count+1]["Fri"]=input("Enter workout regimen for friday :")
            workoutRegimens[count+1]["Sat"]=input("Enter workout regimen for saturday :")
            workoutRegimens[count+1]["Sun"]=input("Enter workout regimen for sunday :")

            workoutRegimens[count+2]["lowerBMI"]=upperBMI+0.01
            count=0
            for regimen in workoutRegimens:
                if (regimen["lowerBMI"]>=regimen["upperBMI"]):
                    workoutRegimens.pop(count)
                count+=1
                

        else:
            print("currently, there is no superuser active.If you are superuser please login as superuser")


    def viewAllRegimens(self):
        if SuperUser.loggedinSuperusers:
            for item in workoutRegimens[0]:
                print(item,end=",  ")
            print()
            for length in range(len(workoutRegimens)):
                for item in workoutRegimens[0]:
                    print(workoutRegimens[length][item],end=",  ")
                print()
        else:
            print("currently, there is no superuser active.If you are superuser please login as superuser")


    def viewRegimen(self):
        if SuperUser.loggedinSuperusers:
            BMI=float(input("Enter your BMI  :"))
            for regimen in workoutRegimens:                
                if (BMI>=regimen["lowerBMI"] and BMI<=regimen["upperBMI"]):
                    print("Mon =",regimen["Mon"])
                    print("Tue =",regimen["Tue"])
                    print("Wed =",regimen["Wed"])
                    print("Thu =",regimen["Thu"])
                    print("Fri =",regimen["Fri"])
                    print("Sat =",regimen["Sat"])
                    print("Sun =",regimen["Sun"])
                    break
            else:
                print("BMI is out of range or deleted. Range of BMI is 0-50")
        else:
            print("currently, there is no superuser active.If you are superuser please login as superuser")

    def deleteRegimen(self):
        if SuperUser.loggedinSuperusers:
            BMI=float(input("Enter BMI  :"))
            for regimen in workoutRegimens:                
                if (BMI>=regimen["lowerBMI"] and BMI<=regimen["upperBMI"]):
                    workoutRegimens.remove(regimen)
                    print("Regimen deleted successfully")
                    print("Caution : There is a gap of BMI in your workoutRegimens from",regimen["lowerBMI"],"to",regimen["upperBMI"],".Please,fill this BMI gap by creating one or more regimens")
                    break
            else:
                print("BMI is out of range or deleted. Range of BMI is 0-50")
        else:
            print("currently, there is no superuser active.If you are superuser please login as superuser")

    def updateRegimen(self):
        if SuperUser.loggedinSuperusers:
            count=0
            BMI=float(input("Enter BMI  :"))
            for regimen in workoutRegimens:                
                if (BMI>=regimen["lowerBMI"] and BMI<=regimen["upperBMI"]):
                    regimen["lowerBMI"]=float(input("Enter updated lower BMI"))
                    regimen["upperBMI"]=float(input("Enter updated upper BMI"))
                    regimen["Mon"]=input("Enter workout regimen for monday :")
                    regimen["Tue"]=input("Enter workout regimen for tuesday :")
                    regimen["Wed"]=input("Enter workout regimen for wednesday :")
                    regimen["Thu"]=input("Enter workout regimen for thursday :")
                    regimen["Fri"]=input("Enter workout regimen for friday :")
                    regimen["Sat"]=input("Enter workout regimen for saturday :")
                    regimen["Sun"]=input("Enter workout regimen for sunday :")
                    break
                count+=1
            workoutRegimens[count-1]["upperBMI"]=workoutRegimens[count]["lowerBMI"]-0.01
            workoutRegimens[count+1]["lowerBMI"]=workoutRegimens[count]["upperBMI"]+0.01
        else:
            print("currently, there is no superuser active.If you are superuser please login as superuser")


    def showMyProfile(self):
        if Member.members:
            MobileNumber=input("Enter your mobile number  :")
            for member in Member.members:
                if member.mobileNumber==MobileNumber:
                    print("FullName =",member.fullName)
                    print("Age =",member.age)
                    print("Gender =",member.gender)
                    print("MobileNumber =",member.mobileNumber)
                    print("Email =",member.email)
                    print("BMI =",member.BMI)
                    print("MemberShipDuration =",member.membershipDuration)
                    break
            else:
                print("Member not found.Please, check the mobile number")    
        else:
            print("Currently there is no member in the gym.Please ask a superuser to create your account.To be a superuser change your functionality")

    def showMyRegimen(self):
        if Member.members:
            MobileNumber=input("Enter your mobile number  :")
            for member in Member.members:
                if member.mobileNumber==MobileNumber:
                    print("Mon =",member.workRegimen["Mon"])
                    print("Tue =",member.workRegimen["Tue"])
                    print("Wed =",member.workRegimen["Wed"])
                    print("Thu =",member.workRegimen["Thu"])
                    print("Fri =",member.workRegimen["Fri"])
                    print("Sat =",member.workRegimen["Sat"])
                    print("Sun =",member.workRegimen["Sun"])
                    break
            else:
                print("Member not found.Please, check the mobile number")    
        else:
            print("Currently there is no member in the gym.Please ask a superuser to create your account.To be a superuser change your functionality")


Rgym=Gym()   
while True:
    print("0.Enter 0 to exit\n1.Enter 1 to get a superuser functionality\n2.Enter 2 to get a member functionality") 
    try:
        inputData=int(input("Enter a number input  :"))
        if inputData==0:
            print("app is closing...........")
            break
        elif inputData==1:
            print("Welcome as a superuser")
            print("1.Enter 'back' to change your functionality or back to previous menu\n2.Enter 'login' to login as a superuser(default username and password is admin)\n3.Enter 'create member' to create a new member\n4.Enter 'view member' to see profile of an individual member by mobile number\n5.Enter 'delete member' to delete a member\n6.Enter 'update member' to update their profile also you can extend and invoke their membership\n7.Enter 'create regimen' to create a regimen\n8.Enter 'view regimen' to view any regimen by BMI\n9.Enter 'view allregimen' to see all regimen\n10.Enter 'delete regimen' to delete a regimen\n11.Enter 'update regimen' to update a regimen")
            while True:
                inputdata=input("Enter your input  :")
                if inputdata=="back":
                    break
                elif inputdata=="login":
                    Rgym.loginSuperuser()
                elif inputdata=="create member":
                    Rgym.createMember()
                elif inputdata=="view member":
                    Rgym.viewMember()
                elif inputdata=="delete member":
                    Rgym.deleteMember()
                elif inputdata=="update member":
                    Rgym.updateMember()
                elif inputdata=="create regimen":
                    Rgym.createRegimen()
                elif inputdata=="view regimen":
                    Rgym.viewRegimen()
                elif inputdata=="view allregimen":
                    Rgym.viewAllRegimens()
                elif inputdata=="delete regimen":
                    Rgym.deleteRegimen()
                elif inputdata=="update regimen":
                    Rgym.updateRegimen()
                else:
                    print("Please,Enter a valid input")
                

        elif inputData==2:
            print("Welcome as a member")
            print("1.Enter 'back' to change your functionality or back to previous menu\n2.Enter 'regimen' to see your regimen\n3.Enter 'profile' to see your profile")
            
            while True:
                inputdata=input("Enter your input  :")
                if inputdata=="back":
                    break
                elif inputdata=="regimen":
                    Rgym.showMyRegimen()
                elif inputdata=="profile":
                    Rgym.showMyProfile()
                else:
                    print("Please,Enter a valid input")
        else:
            print("Please give a correct input")
    except:
        print("Please,Enter a number input")



