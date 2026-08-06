shopping_cart={}
n=int(input("How many products do you want to add?"))
for i in range(n):
    name=input("Enter product name:")
    price=int(input("Enter product price:"))
    shopping_cart[name]=price
print("\nShopping Cart:")
print(shopping_cart)

# Search a product 
name=input("Enter a product name to search:")
if name in shopping_cart:
    print("Product Price:",shopping_cart[name])
else:
    print("Product not found")
    
# Update a product's price
name=input("Enter a product name to update:")
if name in shopping_cart:
    price=int(input("Enter new price for the product:"))
    shopping_cart[name]=price
    print("Product price updated successfully")
else:
    print("Product not found")
    
# Delete a product record 
name=input("Enter a product name to delete:")
if name in shopping_cart:
    del shopping_cart[name]
    print("Product record deleted successfully")
else:
    print("Product not found")
    
# Check whether a product exists
name=input("Enter a product name to check:")
if name in shopping_cart:
    print("Product found")
else:
    print("Product not found")
    
# Display the most expensive product
if shopping_cart:
    expensive=max(shopping_cart,key=shopping_cart.get)
    print("\nMost Expensive Product:", expensive)
    print("Price:", shopping_cart[expensive])
else:
    print("No product available")
    
# Display the cheapest product
if shopping_cart:
    cheapest=min(shopping_cart,key=shopping_cart.get)
    print("\nCheapest Product:", cheapest)
    print("Price:", shopping_cart[cheapest])
else:
    print("No product available")
    
# Calculate the total cost of all products
total=0
for value in shopping_cart.values():
    total+=value
print("\nTotal cost of all products:",total)

# Calculate the average product price
total=0
for price in shopping_cart.values():
    total+=price
if len(shopping_cart)>0:
    average=total/len(shopping_cart)
    print("\nAverage Product Price:",average)
else:
    print("No product records available")
    
# Display products costing ₹1000 or more
print("\nProducts costing ₹1000 or more:")
for name, price in shopping_cart.items():
    if price>=1000:
        print(name, ":", price)
        
# Display products costing less than ₹500
print("\nProducts costing less than ₹500:")
for name, price in shopping_cart.items():
    if price<500:
        print(name, ":", price)
        
# Sort products by name
print("\nSorted products by names:")
for name in sorted(shopping_cart):
    print(name, ":", shopping_cart[name])
    
# Sort products by price
print("\nSorted products by price:")
sorted_products=sorted(shopping_cart.items(),key=lambda x:x[1])
for name, price in sorted_products:
    print(name, ":", price)
    
