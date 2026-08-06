students={}
n=int(input("How many students do you want to add?"))
for i in range(n):
    id=int(input("Enter student ID:"))
    name=input("Enter student name:")
    age=int(input("Enter student age:"))
    course=input("Enter course:")
    marks=int(input("Enter marks:"))
    students[id]={
    "name":name,
    "age":age,
    "course":course, 
    "marks":marks
    }
print("\nStudent Management System:")
print(students)

# Search a student ID
std_id=int(input("Enter a student ID to search:"))
if std_id in students:
    print("Student Details:")
    print(students[std_id])
else:
    print("No student found")   
    
# Update student details
std_id=int(input("Enter a student ID to update:"))
if std_id in students:
    name=input("Enter new student name:")
    age=int(input("Enter new age:"))
    course=input("Enter new course:")   
    marks=int(input("Enter new marks:"))
    students[std_id]={
    "name":name,
    "age":age,
    "course":course, 
    "marks":marks
    }
    print("Student details updated successfully")
else:
    print("No student found")
    
# Delete a student record
std_id=int(input("Enter a student ID to delete:"))
if std_id in students:
    del students[std_id]
    print("Student record deleted successfully")
else:
    print("No student found")
    
# Check whether a student exists
std_id=int(input("Enter a student ID to check:"))
if std_id in students:
    print("Student found")
else:
    print("No student exists")
    
# Display the student with the highest marks
if students:
    highest=max(students, key=lambda x: students[x]["marks"])
    print("\nStudent with Highest Marks:")
    print("ID:", highest)
    print(students[highest])
else:
    print("No student available")
    
# Display the student with the lowest marks
if students:
    lowest=min(students,key=lambda x: students[x]["marks"])
    print("\nStudent with Lowest Marks:")
    print("ID:",lowest)
    print(students [lowest])
else:
    print("No student available")
    
# Calculate the average marks of all students
total=0
for student in students.values():
    total+=student["marks"]
if len(students)>0:
    average=total/len(students)
    print("Average Marks:", average)
else:
    print("No student records available")

# Display students who scored 75 or more
print("\nStudents with 75 or more score:")
for student_id,details in students. items():
    if details["marks"]>=75:
        print("ID:",student_id)
        print("Name:",details["name"])
        print("Marks:",details["marks"])
        print()
        
# Display students who scored below 40
print("\nStudents with below 40 score:")
for student_id, details in students. items():
    if details["marks"]<40:
        print("ID:",student_id)
        print("Name:",details["name"])
        print("Marks:",details["marks"])
        print()
 
# Sort students by Student ID
print("\nSorted Students by Student ID:")
for student_id in sorted(students):
    print("ID:", student_id)
    print("Name:", students[student_id]["name"])
    print("Age:", students[student_id]["age"])
    print("Course:", students[student_id]["course"])
    print("Marks:", students[student_id]["marks"])
    print()
    
# Sort students by name
print("\nSorted Students by Name:")
sorted_students=sorted(students.items(), key=lambda x: x[1]["name"])
for student_id, details in sorted_students:
    print("ID:", student_id)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Course:", details["course"])
    print("Marks:", details["marks"])
    print()
    
# Sort students by marks
print("\nSorted students by Marks:")
sorted_students=sorted(students.items(),key=lambda x:x[1]["marks"])
for student_id,details in sorted_students:
    print("ID:", student_id)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Course:", details["course"])
    print("Marks:", details["marks"])
    print()
  
