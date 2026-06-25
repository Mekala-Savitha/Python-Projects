import grade

maths = int(input("Enter Maths marks:"))
english = int(input("Enter English marks:"))
science = int(input("Enter Science marks:"))
social = int(input("Enter Social marks:"))
telugu = int(input("Enter Telugu marks:"))
total,average,grade_result = grade.calculate_grade(
    maths,english,science,social,telugu
)

print("Total Marks =",total)
print("Average =",average)
print("Grade =",grade_result)
