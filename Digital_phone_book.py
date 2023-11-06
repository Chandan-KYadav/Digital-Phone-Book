#Digital phone book a Menu Driven Console Based Application
import psycopg2
from datetime import datetime 
from datetime import date

class login :

    def __init__(self) :

         try :

            self.con = psycopg2.connect(
                 host = "127.0.0.1",
                 port = "5432",
                 database = "postgres",
                 user = "postgres",
                 password = "root"
                 )
         except Exception as err :
            print(err)
         else :
            print("[User logged in]")
            self.date = date.today()
            self.time = datetime.now()
            print(f"{self.date.day} {self.date.strftime("%b %d %Y")} {self.time.hour}: {self.time.minute} {self.time.strftime("%p")}")
            print("----------------------------")


class Telephone_book :
    def __init__(self,id=None,first=None,last=None,email=None,phone=None) :
        self.contactid = id
        self.firstname = first
        self.lastname = last 
        self.emailid = email
        self.phone_no = phone

   

    def set_f_name(self,_fname_ ):
        self.firstname = _fname_

    def set_l_name(self,_lname_ ):
        self.lastname = _lname_

    def set_email(self,_email_):
        self.emailid = _email_

    def set_mobile(self,_num_ ):
        self.phone_no =_num_

class menu_driven(Telephone_book,login):

    def add_in_database(self) :
        login.__init__(self)
        command = "insert into telephone_book values('"+self.contactid+"','"+self.firstname+"','"+self.lastname+"','"+self.emailid+"','"+self.phone_no+"')"
        obj = self.con.cursor()
        obj.execute(command)
        self.con.commit()
        print("Contact added")

    def view_all_database(self) :
        login.__init__(self)
        command = "select * from telephone_book order by contactid"
        obj = self.con.cursor()
        obj.execute(command)
        fetch = obj.fetchall()
        for e in fetch :
            print(e)
        print("Want to store in file ?")
        print("1.Yes")
        print("2.No")
        choice = eval(input("enter your choice: "))
        if(choice == 1) :
            f_w = open('telephone_book.txt','w')
            for e in fetch :
                f_a = open('telephone_book.txt','a')
                f_a.write(""+str(e)+"\n")
                
                f_a.close()
            f_w.close()
        else :
             print("Data not saved") 

                
    def view_database(self) :
        login.__init__(self) 
        command = "select * from telephone_book where contactid ='"+self.contactid+"'"
        obj = self.con.cursor()
        obj.execute(command)
        fetch = obj.fetchall()
        print(fetch)

    def delete_database(self) :
        login.__init__(self)
        command = " Delete from telephone_book where contactid = '"+self.contactid+"'"
        obj = self.con.cursor()
        obj.execute(command)
        self.con.commit()

    def update_database(self) :
        login.__init__(self) 
        command = "update telephone_book set firstname ='"+self.firstname+"',lastname ='"+self.lastname+"', emailid ='"+self.emailid+"', phone_no = '"+self.phone_no+"' where contactid = '"+self.contactid+"'"
        obj = self.con.cursor()
        obj.execute(command)
        self.con.commit()
        print("Record updated")


def add_contact() :
    id = input("Enter contact Id ")
    firstname = input("enter first name ")
    lastname = input("enter last name ")
    email = input("enter email Id ")
    mobile = input("enter mobile No. ")
    user = menu_driven(id,firstname,lastname,email,mobile)
    user.add_in_database()
    
def view_all() :
    user = menu_driven()
    user.view_all_database()
    

def view() :
    id = input("Enter contact Id ")
    user = menu_driven(id)
    user.view_database()

def delete() :
    id = input("Enter contact Id ")
    user = menu_driven(id)
    user.delete_database()

def update() :
    id = input("Enter contact Id ")
    firstname = input("enter first name ")
    lastname = input("enter last name ")
    email = input("enter email Id ")
    mobile = input("enter mobile No. ")
    user = menu_driven(id=id)
    user.set_f_name(firstname)
    user.set_l_name(lastname)
    user.set_email(email)
    user.set_mobile(mobile)
    user.update_database()
    


#--------------------------Driven code--------------------------#

print("1.Register")
print("2.login")
match_auth = eval(input("Enter Your Choice: "))
if(match_auth==2):
    user = login()

match match_auth :


    case 1 :
        print("Register on Postgress firstly......")
    case 2 : 
        
        print("What do you want to do?")
        print("1.[view -all]")
        print("2.[view]")
        print("3.[add]")
        print("4.[del]")
        print("5.[update]")
        print("6.[exit]")
        match_expression = eval(input("Enter your choice: "))
            
        match match_expression :

            case 1 :
                view_all()
            case 2 :
                view()
            case 3 :
                add_contact()
            case 4 :
                delete()
            case 5 :
                update()
            case 6 :
                exit






    


