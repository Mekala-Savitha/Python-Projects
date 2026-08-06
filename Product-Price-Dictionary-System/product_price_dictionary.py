product={}
n=int(input("How many products do you want to add?"))
for i in range(n):
    name=input("Enter product name:")
    price=int(input("Enter product price RS:"))
    product[name]=price
print("\nProduct Price Dictionary:")
print(product)

# Search for a product by it's name
product_name=input("Enter a product name to search:")
if product_name in product:
    print("Price:", product[product_name])
else:
    print("Product not found")

# Update the price of an existing product 
name=input("Enter a product name to update:")
if name in product :
    price=int(input("Enter new price:"))
    product[name]=price
    print("Price updated successfully")
else:
    print("Product not found.")
   
# Delete a product 
name = input("Enter a product name to delete: ")
if name in product:
    del product[name]
    print("Product deleted successfully.")
else:
    print("Product not found.")
    
# Display the final product details 
print("\nFinal Product Details:")
for name, price in product. items():
    print(name, ":", price)
 
