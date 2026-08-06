library={}
n=int(input("How many books do you want to add?"))
for i in range(n):
    id=int(input("Enter Book ID:"))    
    name=input("Enter Book Name:")
    author=input("Enter Author Name:")
    category=input("Enter category:")
    copies=int(input("Number of copies:"))
    library[id]={
    "name":name, 
    "author":author, 
     "category": category, 
     "copies":copies
    }
print("\nLibrary Management System:")
print(library)

# Search a book by book ID
book_id=int(input("Enter a book ID to search:"))
if book_id in library:
    print("Library Details:")
    print(library [book_id])
else:
    print("No book found")
    
# Update book details
book_id=int(input("Enter a book ID to update:"))
if book_id in library:
    name=input("Enter new book name:")
    author=input("Enter new author name:")
    category=input("Enter new category:")
    copies=int(input("Enter new number of copies:"))
    library[book_id]={
    "name":name, 
    "author":author, 
    "category": category, 
    "copies":copies
    }
    print("Book details updated successfully")
else:
    print("No book found")
    
# Delete a book record
book_id=int(input("Enter Book ID to delete:"))
if book_id in library:
    del library[book_id]
    print("Book record deleted successfully")
else:
    print("No book found")
    
# Check whether a book exists
book_id=int(input("Enter Book ID to check"))
if book_id in library:
    print("Book found")
else:
    print("Book not found")
    
# Display the book with the highest number of copies
if library:
    highest=max(library,key=lambda x: library[x]["copies"])
    print("Book with highest number of copies:")
    print("ID:", highest)
    print(library[highest])
else:
    print("No book available")  
    
# Display the book with the lowest number of copies
if library:
    lowest=min(library,key=lambda x: library [x]["copies"])
    print("Book with lowest number of copies:")
    print("ID:",lowest)
    print(library[lowest])
else:
    print("No book available")
    
# Calculate the average number of copies
total=0
for book in library.values():
    total+=book["copies"]
if len(library)>0:
    average=total/len(library)
    print("Average number of copies:", average)
else:
    print("No book records available")
    
# Display books with 10 or more copies
print("\nBooks with 10 or more copies:")
for book_id, details in library.items():
    if details["copies"]>=10:
        print("ID:",book_id)
        print("Name:", details["name"])
        print("Copies:",details["copies"])
        print()
        
# Display books with less than 5 copies
print("\nBooks with less than 5 copies:")
for book_id,details in library.items():
    if details["copies"]<5:
        print("ID:",book_id)
        print("Name:", details["name"])
        print("Copies:",details["copies"])
        print()
        
# Sort books by Book ID
print("\nSorted Books by Book ID:")
for book_id in sorted(library):
    print("ID:",book_id)
    print("Name:", library[book_id]["name"])
    print("Author:", library[book_id]["author"])
    print("Category:", library[book_id]["category"])
    print("Copies:", library[book_id]["copies"])
    print()
    
# Sort books by Book Name
print("\nSorted Books by Name:")
sorted_library=sorted(library.items(),key=lambda x: x[1]["name"])
for book_id, details in sorted_library:
    print("ID:",book_id)
    print("Name:",details["name"])
    print("Author:", details["author"])
    print("Category:", details["category"])
    print("Copies:", details["copies"])
    print()
    
# Sort books by Number of Copies
print("\nSorted Books by Number of Copies:")
sorted_library=sorted(library.items(),key=lambda x: x[1]["copies"])
for book_id, details in sorted_library:
    print("ID:",book_id)
    print("Name:",details["name"])
    print("Author:", details["author"])
    print("Category:", details["category"])
    print("Copies:", details["copies"])
    print()

