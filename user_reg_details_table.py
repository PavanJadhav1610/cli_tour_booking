import mysql.connector
class action_det:
    # query for connectivity
    def __init__(self):
        self.a=mysql.connector.connect(host='localhost',
        user='root',password='Pavan@123',database='basicdb')
        self.var=self.a.cursor()
        self.a.commit()
    # now to create table :
    def Table(self):
        self.var1=self.var.execute("create table user_registration_details (name varchar(20),password varchar(100),contact_no varchar(20) unique,user_aadharcard varchar(12),user_city_name char(50))")
        self.a.cursor()
        self.a.commit()
    # mow to insert values in table:
    def inser(self,name,password,contact_no,user_aadharcard,user_city_name):
        b="insert into user_registration_details (name,password,contact_no,user_aadharcard,user_city_name)values('{}','{}','{}','{}','{}')".format(name,password,contact_no,user_aadharcard,user_city_name)
        self.var.execute(b)
        self.a.cursor()
        self.a.commit()
    def show(self):
        self.var.execute("select * from user_registration_details")
        var3=self.var.fetchall()
        print(var3)
        print("table user_registration_details created.")
        
d=action_det()
# d.Table()
# d.inser("pavan","pavan@123","1010101010","329722689868","Panvel")
# d.inser("pankaj","pankaj@123","2020202020","329722659878","Pune")
# d.show()