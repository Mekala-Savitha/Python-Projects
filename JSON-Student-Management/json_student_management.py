"""
JSON Student Management System
================================

A menu-driven mini project using Python and JSON.

Features:
- Add student
- View all students
- Search student
- Update student
- Delete student
- Count students
- Exit
"""

import json

FILE_NAME = "student_management.json"

def load_students():
    """Load student records from the JSON file."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: JSON file contains invalid data.")
        return []


def save_students(students):
# Save student records to the JSON file.
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student():
# Add a new student.
    students = load_students()
    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Student Name: ").strip()
    age = int(input("Enter Age: "))
    course = input("Enter Course: ").strip()
    email = input("Enter Email: ").strip()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email
    }

    students.append(student)
    save_students(students)

    print("Student added successfully.")


def view_students():
# Display all students.
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print(f"Email  : {student['email']}")
        print("-------------------------------------")


def search_student():
# Search for a student by ID.
    students = load_students()

    student_id = input("Enter Student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("ID     :", student["id"])
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Course :", student["course"])
            print("Email  :", student["email"])
            return

    print("Student not found.")


def update_student():
# Update an existing student's details.
    students = load_students()

    student_id = input("Enter Student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nEnter new details:")

            student["name"] = input("Enter Name: ").strip()
            student["age"] = int(input("Enter Age: "))
            student["course"] = input("Enter Course: ").strip()
            student["email"] = input("Enter Email: ").strip()
            
            save_students(students)

            print("Student updated successfully.")
            return
    print("Student not found.")


def delete_student():
# Delete a student by ID.
    students = load_students()

    student_id = input("Enter Student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)

            print("Student deleted successfully.")
            return

    print("Student not found.")


def count_students():
# Display the total number of students.
    students = load_students()
    print("Total students:", len(students))


def display_menu():
# Display the main menu.
    print("\n========== JSON STUDENT MANAGEMENT ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Exit")
    print("=============================================")


def main():
# Run the student management system.
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ").strip()

        try:
            if choice == "1":
                add_student()

            elif choice == "2":
                view_students()

            elif choice == "3":
                search_student()

            elif choice == "4":
                update_student()

            elif choice == "5":
                delete_student()

            elif choice == "6":
                count_students()

            elif choice == "7":
                print("Thank you for using the Student Management System.")
                break

            else:
                print("Invalid choice. Please enter 1-7.")

        except ValueError:
            print("Invalid input. Age must be a number.")

if __name__ == "__main__":
    main()
  
