import sys
import mysql.connector
# import numpy as np
# from user_login import registration

def get_tour_details(self):
        print("*****************************************************************")
        print("-----here we have some discounted tour packages for you------")
        print("*****************************************************************")

        mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123",database="basicdb")
        mycursor = mydb.cursor()
        mycursor.execute("select * from packages_details")
        tours = mycursor.fetchall()
        
        # a1=np.array(tours)
        print(">----this discounted packages are available for only special only-99 customers-----")
        # print(a1)
        print("\n 1] Balaji darshan","\n 2] Pithapur","\n 3] Kailash","\n 4] Akshaydham","\n 5] kerala","\n 6] Jammu kashmir",
              "\n 7] delhi","\n 8] kashi","\n 9] Chiranjeevi","\n 10] V_pattanam","\n 11] 7-shivlingas")
        print("---------------------------------------------------------------------------------")
        self.choice=int(input("type number to see details of tour from above list :"))
        print("---------------------------------------------------------------------------------")
        
        if self.choice==1:
                print("your selected tour is:",tours[0])
                # db_cursor.execute("insert into")
        elif self.choice==2:
                print("your selected tour is:",tours[1])
        elif self.choice==3:
                print("your selected tour is:",tours[2])       
        elif self.choice==4:
                print("your selected tour is:",tours[3])
        elif self.choice==5:
                print("your selected tour is:",tours[4])
        elif self.choice==6:
                print("your selected tour is:",tours[5])
        elif self.choice==7:
                print("your selected tour is:",tours[6])
        elif self.choice==8:
                print("your selected tour is:",tours[7])
        elif self.choice==9:
                print("your selected tour is:",tours[8])
        elif self.choice==10:
                print("your selected tour is:",tours[9])
        elif self.choice==11:
                print("your selected tour is/:",tours[10])
        elif self.choice>=11:
                print("---enter the valid choice number---")
        else: print("-----you have selected invalid tour package number-----")
        booking_details(self)

# ---------------------------------------------------------------------------------------------------------------------------
def booking_details(self):

        mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123",database="basicdb")
        mycursor = mydb.cursor()
        mycursor.execute("select * from packages_details")
        tours = mycursor.fetchall()
        print("\n")
        print("...................please conform your tour journey again...................")
        self.confirmation=int(input("enter your confirmation nummber of your tour :"))
        print("\n")

        if self.confirmation==1:
                print("your selected tour id/place_name/ticket amount/date_of_tour are :\n:",tours[0])
                # db_cursor.execute("insert into")
        elif self.confirmation==2:
                        print("your confirmed tour id/place_name/ticket amount/date_of_tour are :\n:",tours[1])
        elif self.confirmation==3:
                        print("your confirmed tour id/place_name/ticket amount/date_of_tour are :\n:",tours[2])       
        elif self.confirmation==4:
                        print("your confirmed tour id/place_name/ticket amount/date_of_tour are :\n:",tours[3])
        elif self.confirmation==5:
                        print("your confirmed tour id/place_name/ticket amount/date_of_tour are :\n:",tours[4])
        elif self.confirmation==6:
                        print("your confirmed tour id/place_name/ticket amount/date_of_tour are :\n:",tours[5])
        elif self.confirmation==7:
                        print("your confirmed tour id/place_name/ticket amount/date_of_tour are :\n:",tours[6])
        elif self.confirmation==8:
                        print("your confirmed tour id/place_name/ticket amount/date_of_tour are :\n:",tours[7])
        elif self.confirmation==9:
                        print("your confirmed tour id/place_name/ticket amount/date_of_tour are :\n:",tours[8])
        elif self.confirmation==10:
                        print("your confirmed tour id/place_name/ticket amount/date_of_tour are :\n:",tours[9])
        elif self.confirmation==11:
                        print("your confirmed tour id/place_name/ticket amount/date_of_tour are :\n",tours[10])
        elif self.confirmation>=11:
                        print("---enter the valid confirmation choice number---")
        else: print("-----you have selected invalid tour package number-----")

        if self.confirmation != self.choice  or  self.choice != self.confirmation:
                print("\n")
                print("----------you choosedn a diffrent tour while confirmation----------")
                print("*****..login to your account and book your tour again..*****")
        else:   
                print("\n")
                print("-----------------------------------------------------------------------")
                var1=input(">---would you want to proceed for payment? type: yes or no :")
               
                if var1=="yes":
                        user_payment(self)
                else:
                        from user_login import home
# ---------------------------------------------------------------------------------------------------------------------------
def user_payment(self):
        print("\n>---------*-*-*-its time to make your payment -*-*-*--------------")

        print("----give me your tour id no------")
        self.tour_id=int(input(">enter your tour id :"))
        if self.tour_id!=self.confirmation:
                print("\n >----you choosed diffrent tour id rather than you confirmed----")
                from user_login import login

        else:
                if self.tour_id==1:
                        print("your tour payment is of 15000rs only|--")
                elif self.tour_id==2:
                        print("your tour payment is of 20000rs only|--")
                elif self.tour_id==3:
                        print("your tour payment is of 22000rs only|--")
                elif self.tour_id==4:
                        print("your tour payment is of 25000rs only|--")
                elif self.tour_id==5:
                        print("your tour payment is of 18000rs only|--")
                elif self.tour_id==6:
                        print("your tour payment is of 30000rs only|--")
                elif self.tour_id==7:
                        print("your tour payment is of 22000rs only|--")
                elif self.tour_id==8:
                        print("your tour payment is of 12000rs only|--")
                elif self.tour_id==9:
                        print("your tour payment is of 32000rs only|--")
                elif self.tour_id==10:
                        print("your tour payment is of 27000rs only|--")
                elif self.tour_id==11:
                        print("your tour payment is of 30000rs only|--")
                elif self.tour_id>=12:
                        print("please enter the valid tour id")

        print("\n >-----please choose the payment method \n1]online payment \n2]offline payment")
        self.payment=int(input(">---enter your method of payment mode :"))
        
        
        print("\n")
        if self.payment==1:
                        b=int(input("enter the card number:"))
                        c=str(b)    
                        if len(c)>16:
                            print(">---you entered too long card number...")
                            print("...go to the payment payment option and try agian...")
                        elif len(c)<16:
                            print("...we find some missing characters while you entering card details...")
                            print("...go to the payment payment option and try agian...")
                            
                        else:
                                # print("you entered the valid card number.")
                                if len(c)==16:
                                        d=int(input("enter the card cvv:"))
                                        e=str(d)
                                        if len(e)>3:
                                                print("\n >----you entered too long cvv number.")
                                        elif len(e)<3:
                                                print("\n >----we find some missing characters while you entering cvv details.")
                                 
                                if len(c)==16 and len(e)==3:
                                        print("\n >-----your payment is sucessfull----- \n >-----enjoy rour journey on specific date-----")
                                        
                                        # creating table of booked tickets details
                                        
                                        self.confirmation==self.choice or self.choice==self.confirmation
                                        import mysql.connector
                                        mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123",database="basicdb")
                                        mycursor=mydb.cursor()
                                        data=(self.user_name,self.user_mobile_number,self.tour_id,self.user_aadharcard1)
                                        query="INSERT INTO booked_tickets_details VALUES (%s, %s,%s,%s)"
                                        mycursor.execute(query,data)
                                        mydb.commit()

                                        # displaying remaining seats for user
                                        import mysql.connector
                                        from user_reg_details_table import action_det
                                        mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123",database="basicdb")
                                        mycursor=mydb.cursor()
                                        query="select count(*) from booked_tickets_details"
                                        mycursor.execute(query)
                                        no_of_count=mycursor.fetchone()
                                        # print(no_of_count)
                                        total_seats=99

                                        for i in no_of_count:
                                                if i!=None:
                                                        self.remaining_seats=total_seats-i
                                                print(" >----more available seats are :",self.remaining_seats)


        elif self.payment==2:
                print("\n")
                print("*** go to our nearest booking centre and book your ticket in offline way*****")
                import mysql.connector
                from user_reg_details_table import action_det
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123",database="basicdb")
                mycursor=mydb.cursor()
                query="select count(*) from booked_tickets_details"
                mycursor.execute(query)
                no_of_count=mycursor.fetchone()
                # print(no_of_count)
                total_seats=99

                for i in no_of_count:
                        if i!=None:
                                remaining_seats=total_seats-i
                        print(">----more available seats are :",remaining_seats)   
                        print(">-----hurryup onlylimited seats are available----")                 
        else:
                print("-----you have entered diffrent payment method--------")
                from user_login import login
                login(self)
