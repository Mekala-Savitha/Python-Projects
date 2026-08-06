electricity_bill={}
n=int(input("How many customers do you want to add?"))
for i in range(n):
    name=input("Enter customer name:")
    amount=int(input("Enter electricity bill amount:"))
    electricity_bill[name]=amount
print("\nElectricity Bill Calculator:")
print(electricity_bill)

# Search a customer's bill
name=input("Enter a customer name to search:")
if name in electricity_bill:
    print("Electricity Bill Amount:",electricity_bill[name])
else:
    print("Customer not found")
    
# Update customer's bill
name=input("Enter a customer name to update:")
if name in electricity_bill:
    amount=int(input("Enter new electricity bill:"))
    electricity_bill[name]=amount
    print("Electricity Bill updated successfully")
else:
    print("Customer not found")
    
# Delete a customer record 
name=input("Enter a customer name to delete:")
if name in electricity_bill:
    del electricity_bill[name]
    print("Customer record deleted successfully")
else:
    print("Customer not found")
    
# Check whether a customer exists
name=input("Enter a customer name to check:")
if name in electricity_bill:
    print("Customer found")
else:
    print("Customer not found")
    
# Display the customer with the highest electricity bill
if electricity_bill:
    highest=max(electricity_bill,key=electricity_bill.get)
    print("\nHighest Electricity Bill:",highest)
    print("Amount:", electricity_bill[highest])
else:
    print("No customer available")
    
# Display the customer with the lowest electricity bill
if electricity_bill:
    lowest=min(electricity_bill,key=electricity_bill.get)
    print("\nLowest Electricity Bill:",lowest)
    print("Amount:", electricity_bill[lowest])
else:
    print("No customer found")
    
# Calculate the total electricity bill amount
total=0
for value in electricity_bill.values():
    total+=value
print("\nTotal Electricity Bill Amount:",total)

# Calculate the average electricity bill amount
total=0
for amount in electricity_bill.values():
    total+=amount
if len(electricity_bill)>0:
    average=total/len(electricity_bill)
    print("\nAverage Electricity Bill:", average)
else:
    print("No customer records available")
    
# Display customers whose bill is ₹1000 or more
print("\nCustomers with ₹1000 or more bill:")
for name, amount in electricity_bill.items():
    if amount>=1000:
        print(name, ":", amount)
        
# Display customers whose bill is less than ₹500
print("\nCustomers with less than ₹500 bill:")
for name, amount in electricity_bill.items():
    if amount<500:
        print(name, ":", amount)
       
# Sort customers by name
print("\nSorted customers by names:")
for name in sorted(electricity_bill):
    print(name, ":", electricity_bill[name])
    
# Sort customers by bill amount
print("\nSorted customers by bill amount:")
sorted_customers=sorted(electricity_bill.items(),key=lambda x:x[1])
for name,amount in sorted_customers:
    print(name, ":", amount)
  
