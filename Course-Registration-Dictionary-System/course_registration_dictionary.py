course_registration={}
n=int(input("How many courses do yo want to add?"))
for i in range(n):
    course_name=input("Enter course name:")
    student_count=int(input("Enter number of enrolled students:"))
    course_registration[course_name]=student_count
print("\nCourse Registration Dictionary:")
print(course_registration)
    
# Search a course 
name=input("Enter a course name to search:")
if name in course_registration:
    print("Number of enrolled students:",course_registration[name])
else:
    print("Course not found")
    
# Update the number of enrolled students 
name=input("Enter a course name to update:") 
if name in course_registration:
    student_count=int(input("Enter new enrolled students:"))
    course_registration[name]=student_count
    print("Enrolled students updated successfully")
else:
    print("Course not found")
    
# Delete a course 
name=input("Enter a course name to delete:")
if name in course_registration:
    del course_registration[name]
    print("Course deleted successfully")
else:
    print("Course not found")
    
# Check whether a course exists 
name=input("Enter a course name to check:")
if name in course_registration:
    print("Course found")
else:
    print("Course not found")
    
# Display the course with highest enrollment 
if course_registration:
    highest=max(course_registration,key=course_registration.get)
    print("\nHighest Enrollment Course:",highest)
    print("Enrollment:",course_registration[highest])
else:
    print("No course available")
    
# Display the course with lowest enrollment 
if course_registration:
    lowest=min(course_registration,key=course_registration.get)
    print("\nLowest Enrollment Course:",lowest)
    print("Enrollment:", course_registration[lowest])
else:
    print("No course available")
    
# Calculate the total number of enrolled students
total=0
for value in course_registration.values():
    total+=value
print("\nTotal number of enrolled students:",total)
    
# Calculate the average number of students per course
total=0
for students in course_registration.values():
    total+=students
if len(course_registration)>0:
    average=total/len(course_registration)
    print("\nAverage number of students:", average)
else:
    print("No student records available.")
    
# Display courses with 50 or more enrolled students
print("\nCourses with 50 or more enrolled students:")
for name, student_count in course_registration.items():
    if student_count>=50:
        print(name, ":", student_count)
        
# Display courses with less than 20 enrolled students
print("\nCourses with less than 20 enrolled students:")
for name, student_count in course_registration.items():
    if student_count<20:
        print(name, ":", student_count)
        
# Sort courses by name
print("\nSorted courses by names:")
for name in sorted(course_registration):
    print(name, ":", course_registration[name])    
    
# Sort courses by the number of enrolled students
print("\nSorted courses by the number of enrolled students:")
sorted_courses=sorted(course_registration.items(),key=lambda x:x[1])
for name,student_count in sorted_courses:
    print(name, ":", student_count)
    
