JSON Student Management System

A menu-driven Python mini project that stores and manages student records using a JSON file.

📌 Project Overview
This project demonstrates how Python can be used to create a simple student management system with JSON file storage.

Student records are stored permanently in:
student_management.json

The program provides basic CRUD operations:
Create → Add student
Read → View and search students
Update → Modify student details
Delete → Remove a student

🛠️ Technologies Used
Python 3
JSON
json module
File handling
Functions
Lists
Dictionaries
Loops
Conditional statements
Exception handling

📂 Project Structure
Python_projects/
│
├── json_student_management.py
├── student_management.json   # Created automatically
└── README.md
student_management.json is created automatically when you add the first student.

✨ Features
1. Add Student
Stores:
Student ID
Name
Age
Course
Email
3. View Students
Displays all saved student records.
4. Search Student
5.Searches for a student using the Student ID.
6. Update Student
Updates the name, age, course, and email of an existing student.
7. Delete Student
Deletes a student using the Student ID.
8. Count Students
Displays the total number of students stored in the JSON file.
9. Exit
Closes the application safely.

▶️ How to Run
Open the terminal in the project folder and run:
python json_student_management.py
In Pydroid 3, open json_student_management.py and press the Run button.

🧾 Example Menu
========== JSON STUDENT MANAGEMENT ==========
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Count Students
7. Exit
=============================================
Enter your choice (1-7):
📝 Example Student Record
After adding a student, the JSON file will contain data similar to:
[
    {
        "id": "101",
        "name": "Savitha",
        "age": 22,
        "course": "Python",
        "email": "savitha@example.com"
    }
]

🔑 JSON Concepts Used
json.load()
Reads JSON data from a file.
with open(FILE_NAME, "r") as file:
    students = json.load(file)
json.dump()
Writes Python data to a JSON file.
with open(FILE_NAME, "w") as file:
    json.dump(students, file, indent=4)
🔄 CRUD Flow
Student Management System
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
      Create          Read          Update
    Add Student   View/Search     Edit Student
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                     Delete
                  Delete Student
                       │
                       ↓
             student_management.json
             
📚 What I Learned
By completing this project, I practiced:
Reading JSON files
Writing JSON files
Working with lists of dictionaries
json.load()
json.dump()
CRUD operations
Functions
Menu-driven programs
Searching and updating records
Exception handling
Persistent data storage

🚀 Future Improvements
Possible improvements:
Add marks and grades
Calculate average marks
Search by name or course
Sort students
Add login/authentication
Add a graphical user interface
Connect the project to a database

