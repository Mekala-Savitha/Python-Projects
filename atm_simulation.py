#ATM Simulator System 

balance=5700
def check_balance():
    return balance 
  
def deposit_money(balance):
    deposit_amount=int(input("Enter deposit amount: "))
    new_balance=balance+deposit_amount 
    return new_balance
def withdraw_money(balance):
    withdraw_amount=int(input("Enter withdraw amount: "))
    if withdraw_amount<=balance:
         balance=balance-withdraw_amount
    else:
         print("Insufficient Balance")
    return balance
         
while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice=int(input("Enter your choice: "))

        if choice==1:
          print("Current Balance=",check_balance())
        elif choice==2:
            balance=deposit_money(balance)
            print("Updated Balance=", balance)
        elif choice==3:
            balance=withdraw_money(balance)
            print("Remaining Balance=", balance)
        elif choice==4:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")
