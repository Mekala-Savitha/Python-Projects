inventory_mngnt={}
n=int(input("How many products do you want to add?"))
for i in range(n):
    name=input("Enter product name:")
    quantity=int(input("Enter stock quantity:"))
    inventory_mngnt[name]=quantity 
print("\nInventory Management Dictionary:")
print(inventory_mngnt)

# Search for a product by it's name
name=input("Enter a product name to search:")
if name in inventory_mngnt:
    print("Stock Quantity:", inventory_mngnt[name])
else:
    print("Product not found")
    
# Update the stock quantity of an existing product 
name=input("Enter a product name to update:")
if name in inventory_mngnt:
    quantity=int(input("Enter new stock quantity:"))
    inventory_mngnt[name]=quantity 
    print("Stock Quantity updated successfully")
else:
    print("Product not found")

# Delete a product record 
name=input("Enter a product name to delete:")
if name in inventory_mngnt:
    del inventory_mngnt[name]
    print("Product record deleted successfully")
else:
    print("Product not found")
    
# Display the final inventory management record 
print("\nInventory Management Dictionary:")
for name, quantity in inventory_mngnt.items():
    print(name, ":", quantity)
    
