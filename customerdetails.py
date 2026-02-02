# Customer details
from database import *
class CustomersDetails:

    def __init__(self, username, password, name, age, city, account_number,balance,status):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_number = account_number
        self.__balance = balance
        self.__status = status

    def createuser(self):
        db_query(f"INSERT INTO customer VALUES ('{self.__username}','{self.__password}','{self.__name}',{self.__age},'{self.__city}' ,{self.__account_number},{self.__balance},{self.__status});")
        con.commit()
    
           

       
        
    
                           
        
