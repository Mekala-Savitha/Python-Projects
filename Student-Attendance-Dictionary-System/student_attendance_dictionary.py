student_attendance={}
n=int(input("How many students do you want to add?"))
for i in range(n):
    name=input("Enter student name:")
    status=input("Enter student is present or absent:")
    student_attendance[name]=status 
print("\nStudent Attendance Dictionary:")
print(student_attendance)

# Search for a student's attendance 
name=input("Enter a student name to search:")
if name in student_attendance:
    print("Status:", student_attendance[name])
else:
    print("Student not found")
    
# Update the attendance status
name=input("Enter a student name to update:")
if name in student_attendance:
    status=input("Enter student present or absent:")
    student_attendance[name]=status
    print("Attendance status updated successfully")
else:
    print("Student not found")
    
# Delete a student's attendance record
name=input("Enter a student name to delete:")
if name in student_attendance:
    del student_attendance[name]
    print("Student attendance record deleted successfully")
else:
    print("Student not found")
    
# Display final attendance record 
print("\nFinal Attendance Record:")
for name, status in student_attendance.items():
    print(name, ":", status)
    
