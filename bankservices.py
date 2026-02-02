# Services offered by the bank
from database import *
import datetime

class Bank:
    def __init__(self,username,account_number):
        self.__username = username
        self.__account_number = account_number
    def create_transaction_table(self):
        db_query(
            f"""
            CREATE TABLE IF NOT EXISTS {self.__username}_transactions (
                timedate VARCHAR(30),
                account_number BIGINT,
                remarks VARCHAR(30),
                amount BIGINT
            )""")
    def balanceenquiry(self):
        balance = db_query(f"select balance from customer where username='{self.__username}';")
        print(f"{self.__username} Balance is {balance[0][0]}")
    def deposit(self,amount):
        dep =  db_query(f"select balance from customer where username='{self.__username}';")
        money = amount + dep[0][0]
        db_query(f"update customer set balance = '{money}' where username='{self.__username}';")
        self.balanceenquiry()
        db_query(f"insert into {self.__username}_transactions values("
            f" '{datetime.datetime.now()}',"
            f" {self.__account_number},"
            f" 'Amount Deposit',"
            f" {amount}"
            f")")
        print( f"{self.__username} Amount is Sucessfully depositted from Your Account {self.__account_number}")
    def withdraw(self,amount):
        balance =  db_query(f"select balance from customer where username='{self.__username}';")
        if amount>balance[0][0]:
            print('Insufficient Balance')
        else:
            money = balance[0][0]-amount
            db_query(f"update customer set balance = '{money}' where username='{self.__username}';")
            self.balanceenquiry()
            db_query(f"insert into {self.__username}_transactions values("
                f" '{datetime.datetime.now()}',"
                f" {self.__account_number},"
                f" 'Amount Withdraw',"
                f" {amount}"
                f")")
            print( f"{self.__username} Amount is Sucessfully Withdrawn from Your Account{self.__account_number}")
    def fundtransfer(self,receiverac_no,amount):
        balance = db_query(f"select balance from customer where username = '{self.__username}';")
        if amount>balance[0][0]:
            print("Insufficient Money, Can't be transferred")
        else:
            receiver = db_query(f"select balance from customer where account_number={receiverac_no};")
            if receiver==[]:
                print('Account Number Does not Exist')
            else:
                balance = balance[0][0] -  amount
                receiver = receiver[0][0] + amount
                db_query(f"update customer set balance = {balance} where username = '{self.__username}';")
                db_query(f"update customer set balance = {receiver} where account_number = {receiverac_no};")
                receiver_name = db_query(f" select username from customer where account_number = {receiverac_no};")
                self.balanceenquiry()
                db_query(f"insert into {receiver_name[0][0]}_transactions values("
                    f" '{datetime.datetime.now()}',"
                    f" {self.__account_number},"
                    f" 'Fund Transfer by {self.__account_number}',"
                    f" {amount}"
                    f")")
                print( f"{self.__username} Amount is Sucessfully Transferred from Your Account {self.__account_number}")
                db_query(f"insert into {self.__username}_transactions values("
                    f" '{datetime.datetime.now()}',"
                    f" {self.__account_number},"
                    f" 'Fund Transfer to {receiverac_no}',"
                    f" {amount}"
                    f")")
                print( f"{self.__username} Amount is Sucessfully Transferred from Your Account {self.__account_number}")

                
            
            
            

        
