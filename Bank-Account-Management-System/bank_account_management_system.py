accounts={}
n=int(input("How many accounts do you want to add?"))
for i in range(n):
    number=int(input("Enter Account Number:"))
    name=input("Enter Account Holder Name:")
    age=int(input("Enter age:"))
    type=input("Enter Account Type (Savings/Current):")
    branch=input("Enter Branch:")
    balance=int(input("Enter Account Balance:"))
    accounts[number]={
    "name":name, 
    "age":age, 
    "type":type, 
    "branch":branch, 
    "balance":balance
    }
print("\nBank Account Management System:")
print(accounts)

# Search an account by Account Number
acc_no=int(input("Enter an account number to search:"))
if acc_no in accounts:
    print("Bank Account Details:")
    print(accounts[acc_no])
else:
    print("No account found")
    
# Update account details
acc_no=int(input("Enter an account number to update:"))
if acc_no in accounts:
    name=input("Enter new account holder name:")
    age=int(input("Enter new age:"))
    type=input("Enter new account type:")
    branch=input("Enter new branch:")
    balance=int(input("Enter new account balance:"))
    accounts[acc_no]={
    "name":name, 
    "age":age, 
    "type":type, 
    "branch":branch, 
    "balance":balance
    }
    print("Account details updated successfully")
else:
    print("No account found")
    
# Delete an account record
acc_no=int(input("Enter an account number to delete:"))
if acc_no in accounts:
    del accounts[acc_no]
    print("Account record deleted successfully")
else:
    print("No account record found")
    
# Check whether an account exists
acc_no=int(input("Enter an account number to check:"))
if acc_no in accounts:
    print("Account found")
else:
    print("No account found")
    
# Display the account with the highest balance
if accounts:
    highest=max(accounts,key=lambda x: accounts[x]["balance"])
    print("Account with highest balance:")
    print("Number:", highest)
    print(accounts[highest])
else:
    print("No account available")
    
# Display the account with the lowest balance
if accounts:
    lowest=min(accounts,key=lambda x: accounts[x]["balance"])
    print("Account with lowest balance:")
    print("Number:",lowest)
    print(accounts[lowest])
else:
    print("No account available")
    
# Calculate the average account balance
total=0
for account in accounts.values():
    total+=account["balance"]
if len(accounts)>0:
    average=total/len(accounts)
    print("Average Account Balance:", average)
else:
    print("No account available")
    
# Display accounts with a balance of ₹1,00,000 or more
print("\nAccounts with ₹1,00,000 or more balance:")
for acc_no,details in accounts.items():
    if details["balance"]>=100000:
        print("Number:",acc_no)
        print("Name:",details["name"])
        print("Balance:",details["balance"])
        print()
       
# Display accounts with a balance below ₹10,000
print("\nAccounts with a balance of ₹10,000:")
for acc_no,details in accounts.items():
    if details["balance"]<10000:
        print("Number:",acc_no)
        print("Name:",details["name"])
        print("Balance:",details["balance"])
        print()
        
# Sort accounts by Account Number
print("\nSorted Accounts by Account Number:")
for acc_no in sorted(accounts):
    print("Number:",acc_no)
    print("Name:", accounts[acc_no]["name"])
    print("Age:", accounts[acc_no]["age"])
    print("Type:", accounts[acc_no]["type"])
    print("Branch:",accounts[acc_no]["branch"])
    print("Balance:", accounts[acc_no]["balance"])
    print()
    
# Sort accounts by Account Holder Name
print("\nSorted Accounts by Account Holder Name:")
sorted_accounts=sorted(accounts.items(),key=lambda x: x[1]["name"])
for acc_no,details in sorted_accounts:
    print("Number:",acc_no)
    print("Name:", accounts[acc_no]["name"])
    print("Age:", accounts[acc_no]["age"])
    print("Type:", accounts[acc_no]["type"])
    print("Branch:",accounts[acc_no]["branch"])
    print("Balance:", accounts[acc_no]["balance"])
    print()
    
# Sort accounts by Balance
print("\nSorted Accounts by Account Balance:")
sorted_accounts=sorted(accounts.items(),key=lambda x: x[1]["balance"])
for acc_no,details in sorted_accounts:
    print("Number:",acc_no)
    print("Name:", accounts[acc_no]["name"])
    print("Age:", accounts[acc_no]["age"])
    print("Type:", accounts[acc_no]["type"])
    print("Branch:",accounts[acc_no]["branch"])
    print("Balance:", accounts[acc_no]["balance"])
    print()

