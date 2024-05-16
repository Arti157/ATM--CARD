import time
print("Please insert Your CARD")
time.sleep(5)
password=1234
pin=int(input("enter your atm pin"))
balance = 5000
if pin==password:
    while True:
        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """
             )
        try:
            option=int(input("Please enter your choise"))
        except:
            print("Please enter valid option")
        if option == 1:
            print("Your current balance is {5000}")
            print("----------------------------------------------------------------")
            
        if option == 2:
            withdraw_amount=int(input("please enter withdrow_amount"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your updated balance is {balance}")
            print("----------------------------------------------------------------")
            
        if option == 3:
             deposit_amount=int(input("please enter deposit_amount"))
             balance=balance+deposit_amount
             print(f"{deposit_amount} is credited from your account")
             print(f"your updated balance is {balance}")
             print("----------------------------------------------------------------")
             
        if option == 4:
            break
else:
    print("Wrong pin Please try again")
