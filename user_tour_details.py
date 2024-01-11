import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Pavan@123")
mycursor=mydb.cursor()
class tour_details:
    def __init__(self):
        self.a=mysql.connector.connect(host='localhost',user='root',password='Pavan@123',database='basicdb')
        self.var=self.a.cursor()
        self.a.commit()

    def Table(self):
        self.var1=self.var.execute("create table packages_details (id int(1),place varchar(15),package int(5),day_of_tour DATE)")
        self.a.cursor()
        self.a.commit()
        print("table created sucessfully")

    def inser(self,id,place,package,day_of_tour):
        b="insert into packages_details(id,place,package,day_of_tour)values('{}','{}','{}','{}')".format(id,place,package,day_of_tour)
        self.var.execute(b)
        self.a.cursor()
        self.a.commit()

    def show(self):
        self.var.execute("select * from packages_details")
        var3=self.var.fetchall()
        print(var3)
        print("table displayed sucessfully")
        
obj=tour_details()
# obj.Table()
# obj.inser(1,"balaji darshan",15000,("2023-11-10"))
# obj.inser(2,"pithapur",20000,("2023-11-15"))
# obj.inser(3,"kailash",22000,("2023-11-20"))
# obj.inser(4,"akshaydham",25000,("2023-11-25"))
# obj.inser(5,"kerala",18000,("2023-11-30"))
# obj.inser(6,"jammu kashmir",30000,("2023-12-4"))
# obj.inser(7,"delhi",22000,("2023-12-8"))
# obj.inser(8,"kashi",12000,("2023-12-12"))
# obj.inser(9,"chiranjeevi",32000,("2023-12-20"))
# obj.inser(10,"V_pattanam",27000,("2023-12-26"))
# obj.inser(11,"7-lingas",31000,("2023-12-30"))
obj.show()


