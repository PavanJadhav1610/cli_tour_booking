import sys 
import mysql.connector
from user_reg_details_table import action_det
import user_menu as ud
# --------------------------------------------------------------------------------------
class tour:
    def __init__(self):
            self.user_det=[]
# --------------------------------------------------------------------------------------
    def user_admin(self):
        print("\n")
        print("********************************************")
        print("        |>---welcome to admin page----<|\n")
        print("********************************************")
        admin_name="python"
        admin_password="python123"

        admin_login_name=input(" >-----enter your default name-----< : ")
        admin_login_password=input(" >-----enter your default password-----< : ")
        
        if admin_login_name==admin_name and admin_login_password==admin_password:
            print("\n")
            print("-*-*-*-* welcome admin",admin_name,"*-*-*-*-\n")
            print("1] delete registered user \n2] delete booked ticket user \n3] add new user")
            admin_activity=int(input(" enter your choice :"))
            if admin_activity==1:
                delete_user=input("enter the name of user that you want to delete :")
                delete_user1=str(delete_user)
                print("registered user",delete_user1,"deleted sucessfully")

                import mysql.connector
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123",database="basicdb")
                mycursor = mydb.cursor()
                delete_query="delete from user_registration_details where name = '"+delete_user1+"'"
                mycursor.execute(delete_query)
                mydb.commit()
                
            elif admin_activity==2:
                print("----you are going to remove or delete booked tickets----")
                delete_ticket=input(" >enter the name of user that you want to delete his tickets :")
                delete_ticket1=str(delete_ticket)

                import mysql.connector
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123",database="basicdb")
                mycursor = mydb.cursor()
                delete_ticket_query="delete from booked_tickets_details where user_name= '"+delete_ticket1+"'"
                mycursor.execute(delete_ticket_query)
                mydb.commit()
                print(" > you deleted ",delete_ticket1,"booked ticket")
            elif admin_activity==3:
                print("\n >----you have to register a new user and then procced further")
                self.registration()
                print("\n >---admin",admin_name,"you registered a new mwmber",self.user_name,"sucessfully \n")
                self.login()

            else:
                print(">---------enter the valid choice-----------<")
        else:
            print("\n <----------please check your admin details and try again------------->")
# -----------------------------------------------------------------------------------------------------------------------------
    def registration(self):

        name=input("->enter your name to regiter :")
        self.user_name=(name)

        if name.isdigit():
                    print("------name does not conatin any digit-------")
                    print("------enter valid name-------")
        else:
            self.user_password=input("->enter your password more than 5 characters :")
            if len (self.user_password)<=5:
                 print(" >---password should be minimum 5 characters-----")
                 self.home()
            else:
                user_mobile=input("->enter your mobile no :")
                self.user_mobile_number=str(user_mobile)
                
                if len(self.user_mobile_number)==10:
                    user_aadharcard=int(input("->enter your adhar card number :"))
                    self.user_aadharcard1=str(user_aadharcard)
                    if len(self.user_aadharcard1)==12:
                        self.city_from=input("->enter your city name :")
                        self.city=str(self.city_from)
                        if len(self.city)<=1:
                            print("\n>----enter the valid city name")
                        else:
                            print("\n>---you entered a valid details---<")
                            mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123",database="basicdb")
                            mycursor = mydb.cursor()
                            data=(self.user_name,self.user_password,self.user_mobile_number,self.user_aadharcard1,self.city)
                            query="INSERT INTO user_registration_details VALUES (%s, %s,%s,%s,%s)"
                            mycursor.execute(query,data)
                            mydb.commit()
                            print("***user",self.user_name,"registered sucessfully***")
                         
                    else:
                        print("\n----please enter a valid aadharcard number---")
                    
                else:
                    print(" >--- please enter valid mobile number")
# -----------------------------------------------------------------------------------------------------------------------------------
    def login(self):
        
        print("-----welcome to login page user-----")
        while(True):
            print("\n")
            login_Mobile=input("enter your registered mobile number :")
            login_userpassword=input("enter your password :")
            if len(login_userpassword)>=5:
                
                try:
                    mycursor.execute("Select contact_no from user_registration_details")
                    result=mycursor.fetchall()
                except:
                    print(Exception)
                try:
                    mycursor.execute("Select password from user_registration_details where contact_no={}".format(login_Mobile))
                    result1=mycursor.fetchone()
                except:
                    print(Exception)
                for i in result:
                    temp,=i
                    if temp==login_Mobile:
                        result=temp
                        break
                if result1:
                    temp,=result1
                    if (result==login_Mobile and temp==login_userpassword):
                        print(" /n>----Welcome back user-----")
                        ud.get_tour_details(self)
                        break
                        
                    else:
                        print(" >-----please check your details or register again -----")
                else:
                    print(" >----you are not registered user try again----\n >----register yourself and then login-----")
            else:
                print(" >----length of password should be minimum 6 characters----")


# -------------------------------------------------------------------------------------------------------------------------------------
    def home(self):
        while True :
            print("\n")
            print("***************************************************************************")
            print("              |------welcome to sai tours @ travellers------|")
            print("***************************************************************************")
            print("\n")
            print("-->press 1 for admin login.")
            print("-->press 2 for your registration.")
            print("-->press 3 for user login.")
            print("-->press 4 for exit from webpage.")
            print("\n")
            var1=int(input("Enter your choice : "))
            if var1==1:
                self.user_admin()
            elif var1==2:
                self.registration()
            elif var1==3:
                self.login()
            elif var1==4:
                print("\n")
                print("...#.#.# you sucessfully exited site #.#.#...\n")
                break
            else:
                print("-----enter the valid choice-----")
# -------------------------------------------------------------------------------------------------------------
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123",database="basicdb")
mycursor=mydb.cursor()

# calling home....
obj=tour()
obj.home()