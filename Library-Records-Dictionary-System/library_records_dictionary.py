library={}
n=int(input("How many books you want to add? "))
for i in range(n):
    name=input("Enter Book Name:")
    author=input("Enter author name:")
    library[name]=author
print("\nLibrary Records Dictionary:")
print(library)

# Search for a book by it's name
book=input("Enter a book name to search:")
print("\nSearch for a book:")
print(library.get(book,"Book not found"))

# Update author or book details 
name=input("Enter a book name to update:")
if name in library:
    author=input("Enter the new author name:")
    library[name]=author
    print("Book updated successfully.")
else:
    print("Book not found.")

# Delete a book record 
name=input("Enter a book name to delete:")
if name in library:
    del library[name]
    print("Book deleted.")
else:
    print("Book not found.")
    
# Display the final library records 
print("\nFinal Library Records:")
for name, author in library. items():
    print(name, ":", author)
    
