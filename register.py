# User Registration

from database import *
from customerdetails import *
from bankservices import Bank 
import random

def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customer where username = '{username}';")
    if temp:
        print("Username Already Exists")
        return SignUp()
    else:
        print("Username is Available Please Proceed")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = int(input("Enter Your Age: "))
        city = input("Enter Your City: ")
        status=1
        balance = 0
        while True:
            account_number = int(random.randint(100000000000, 999999999999))
            temp = db_query(f"SELECT account_number FROM customer WHERE account_number = {account_number};")
            if temp:
                continue
            else:
                print("Your Account Number",account_number)
                break
    cobj = CustomersDetails(username, password, name, age, city, account_number,balance,status)
    cobj.createuser()
    bobj = Bank(username,account_number)
    bobj.create_transaction_table()
def SignIn():
    username = input('Enter your username: ')
    temp = db_query(f"SELECT username FROM customer WHERE username = '{username}';")
    if not temp:
        print('Incorrect Username, please try again!')
        return SignIn()
    # If username exists, get password
    stored_password = db_query(f"SELECT password FROM customer WHERE username = '{username}';")
    stored_password = stored_password[0][0]# extract actual password string
    while True:
        password = input('Enter password:')
        if password==stored_password:
            print('Login Successful!')
            return username
        else:
            print('Incorrect Password!Try Again')
   
    



