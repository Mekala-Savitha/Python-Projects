# Student Marks Dictionary System Project 

student_marks={}
n=int(input("How many students do you want to add? "))
for i in range(n):
    name=input("Enter student name:")
    marks=int(input("Enter student marks:"))
    student_marks[name]=marks
print("\nStudent Marks Dictionary:")
print(student_marks)

# Search marks by student name
student=input("Enter student name to search:")
print("\nStudent's Marks by Name:")
print(student_marks.get(student,"Student not found"))

# Update a Student's marks
name=input("Enter student name to update:")
marks=int(input("Enter new marks:"))
print("\nUpdated Student's Marks:")
student_marks[name]=marks
print(student_marks)

# Delete a student record 
name=input("Enter student name to delete:")
if name in student_marks:
    del student_marks[name]
    print("Record deleted.")
else:
    print("Student not found.") 

# Check whether a student exists 
student=input(" Enter a student name:")
if student in student_marks:
    print("Found")
else:
    print("Not Found")
    
# Display the highest marks
highest_student=""
highest_marks=-1
for name,marks in student_marks.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_student = name
print("\nHighest Marks:")
print(highest_student, ":", highest_marks)

# Display the lowest marks
lowest_student=""
lowest_marks=None 
for name, marks in student_marks.items():
    if lowest_marks is None or marks<lowest_marks:
        lowest_marks=marks
        lowest_student=name
print("\nLowest  Marks:")
print(lowest_student, ":", lowest_marks)

# Calculate the average marks
total=0
for value in student_marks.values():
    total+=value
if len(student_marks) > 0:
    average = total / len(student_marks)
    print("\nAverage Marks:")
    print("Average:", average)
else:
    print("\nNo student records available.")

# Display all students who scored above 75
print("\nStudents who scored above 75:")
for name, marks in student_marks.items():
    if marks>75:
             print(name, ":", marks)
        
# Sort students by names
print("\nSorted Students by Names:")
for name in sorted(student_marks):
    print(name, ":", student_marks[name])
    
# Sort students by marks
print("\nSorted Students by Marks:") 
sorted_students=sorted(student_marks.items(),key=lambda x: x[1])
for name, marks in sorted_students:
    print(name, ":", marks)
