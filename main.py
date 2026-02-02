from register import *
from bankservices import *

status = False

print("Welcome to Banking Project")
while True:
    try:
        register = int(input("1.SignUp\n"
                             "2.SignIn\n"
                             "Please Choose an Option:"))
        if register==1 or register==2:
            if register==1:
                SignUp()
            if register==2:
                user = SignIn()
                status=True
                break
        else:
            print("Please enter a valid input from options")
    except ValueError:
        print("Invalid Input Please Try with Numbers")
account_number= db_query(f"Select account_number from customer where username ='{user}';")
while status:
    print(f"Welcome {user.capitalize()},Please Choose a Banking Service\n")
    try:
        facilities = int(input("1.Balance Enquiry\n"
                               "2. Cash Deposit\n"
                               "3. Cash Withdrawl\n"
                               "4. Fund Transfer\n"
                               "5. Exit\n"
                               ))
        if facilities>=1 and facilities<=5:
            if facilities==1:
                bobj = Bank(user,account_number[0][0])
                bobj.balanceenquiry()
            elif facilities==2:
                while True:
                    try:
                        amount = int(input('Enter the amount to deposit:'))
                    #deposit
                        bobj = Bank(user,account_number[0][0])
                        bobj.deposit(amount)
                        con.commit()
                        break
                    except ValueError:
                        print('Enter valid amount')
                        continue
            elif facilities==3:
                while True:
                    try:
                        amount = int(input('Enter the amount to withdraw:'))
                        #withdrawl
                        bobj = Bank(user,account_number[0][0])
                        bobj.withdraw(amount)
                        con.commit()
                        break
                    except ValueError:
                        print('Please enter a valid amount')
                        continue
            elif facilities==4:
                while True:
                    try:
                        receiverac_no = int(input('Enter the receiver account number:'))
                        amount = int(input('Enter the amount to transfer:'))
                        bobj = Bank(user,account_number[0][0])
                        bobj.fundtransfer(receiverac_no,amount)
                        con.commit()
                        break
                    except ValueError:
                        print('Please enter a valid account number')
                        continue
            elif facilities==5:
                print('Thank You for using Our Banking Services,Please Visit again!!')
                break
        else:
            print("Please enter a valid input from options")
            continue
    except ValueError:
        print("Invalid Input Please Try with Numbers")
        continue

                
        
                               
