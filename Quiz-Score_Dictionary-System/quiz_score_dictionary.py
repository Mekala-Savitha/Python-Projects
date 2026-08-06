quiz_score={}
n=int(input("How many students do you want to add?"))
for i in range(n):
    name=input("Enter student name:")
    score=int(input("Enter quiz score:"))
    quiz_score[name]=score
print("\nQuiz Score Tracker:")
print(quiz_score)

# Search a student's quiz score
name=input("Enter a student to search:")
if name in quiz_score:
    print("Quiz_score:",quiz_score[name])
else:
    print("No student found")
    
# Update a student's quiz score
name=input("Enter a student name:")
if name in quiz_score:
    score=int(input("Enter new quiz score:"))
    quiz_score[name]=score 
    print("\nStudent quiz score updated successfully")
else:
    print("No student found")
    
# Delete a student record
name=input("Enter a student name to delete:")
if name in quiz_score:
    del quiz_score[name]
    print("Student record deleted successfully")
else:
    print("No student found")
    
# Check whether a student exists
name=input("Enter a student name to check:")
if name in quiz_score:
    print("Student found")
else:
    print("Student not found")
    
# Display the student with the highest quiz score
if quiz_score:
    highest=max(quiz_score,key=quiz_score.get)
    print("\nStudent with highest quiz score:", highest)
    print("Quiz Score:",quiz_score[highest])
else:
    print("No student available")

# Display the student with the lowest quiz score
if quiz_score:
    lowest=min(quiz_score,key=quiz_score.get)    
    print("\nStudent with lowest quiz score:",lowest)
    print("Quiz Score:",quiz_score[lowest])
else:
    print("No student available")
    
# Calculate the total quiz score
total=0
for value in quiz_score.values():
    total+=value
print("\nTotal Quiz Score:",total)

# Calculate the average quiz score
total=0
for score in quiz_score.values():
    total+=score
if len(quiz_score)>0:
    average=total/len(quiz_score)
    print("\nAverage Quiz Score:", average)
else:
    print("No student available")
    
# Display students who scored 80 or more
print("\nStudents with 80 or more score:")
for name, score in quiz_score.items():
    if score>=80:
        print(name, ":", score)
        
# Display students who scored below 40
print("\nStudents with below 40 score:")
for name, score in quiz_score.items():
    if score<40:
        print(name, ":", score)
        
# Sort students by name
print("\nSorted students by names:")
for name in sorted(quiz_score):
    print(name, ":", quiz_score[name])
    
# Sort students by quiz score
print("\nSorted students by quiz score:")
sorted_score=sorted(quiz_score.items(),key=lambda x:x[1])
for name,score in sorted_score:
    print(name, ":", score)
  
