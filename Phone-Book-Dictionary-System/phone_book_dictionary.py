phone_book={}
n=int(input("How many contacts do you want to add?"))
for i in range(n):
    name=input("Enter person name:")
    phone_number=int(input("Enter phone number:"))
    phone_book[name]=phone_number
print("\nPhone Book Dictionary:")
print(phone_book)

# Search for a contact by name
name=input("Enter a contact name to search:")
if name in phone_book:
    print("Phone Number:",phone_book[name])
else:
    print("Contact not found")
    
# Update the phone number of an existing contact 
name=input("Enter a contact name to update:")
if name in phone_book:
    phone_number=int(input("Enter new phone number:"))
    phone_book[name]=phone_number
    print("Phone number updated successfully")
else:
    print("Contact not found")
    
# Delete a contact from phone book
name=input("Enter a contact name to delete:")
if name in phone_book:
    del phone_book[name]
    print("Contact deleted successfully")
else:
    print("Contact not found")
    
# Display final phone book records 
print("\nFinal Phone Book Records:")
for name, phone_number in phone_book.items():
    print(name, ":", phone_number)
