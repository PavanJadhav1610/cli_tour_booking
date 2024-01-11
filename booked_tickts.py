import sys
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123")
mycursor=mydb.cursor()

class tour_details:
    def __init__(self):
        self.a=mysql.connector.connect(host='localhost',
        user='root',password='Pavan@123',database='basicdb')
        self.var=self.a.cursor()
        self.a.commit()

    def Table(self):
        self.var1=self.var.execute("create table booked_tickets_details (user_name varchar(20),contact_no varchar(20) unique,tour_id int(2),user_adharcard varchar(12))")
        self.a.cursor()
        self.a.commit()

    def inser(self,user_name,user_mobile_no,tour_id,user_adharcard,city):
        b="insert into booked_tickets_details(user_name,user_mobile_no,tour_id,user_adharcard)values('{}','{}','{}','{}')".format(user_name,user_mobile_no,self.tour_id,self.user_adharcard)
        self.var.execute(b)
        self.a.cursor()
        self.a.commit()

    def show(self):
        self.var.execute("select * from booked_tickets_details ")
        var3=self.var.fetchall()
        print(var3)
        # print("table booking details created sucessfully")
        
obj=tour_details()
obj.Table()
obj.show()