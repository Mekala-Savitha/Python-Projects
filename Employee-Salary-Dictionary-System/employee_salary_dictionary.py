employee_salary={}
n = int(input("Enter the number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    employee_salary[name] = salary

print("\nEmployee Salary Dictionary:")
print(employee_salary)

# Search salary
employee = input("\nEnter employee name to search: ")
print("Salary:", employee_salary.get(employee, "Employee not found"))

# Update salary
employee = input("\nEnter employee name to update salary: ")
if employee in employee_salary:
    new_salary = float(input("Enter new salary: "))
    employee_salary[employee] = new_salary
    print("Salary updated successfully.")
else:
    print("Employee not found.")

# Delete employee
employee = input("\nEnter employee name to delete: ")
if employee in employee_salary:
    del employee_salary[employee]
    print("Employee deleted successfully.")
else:
    print("Employee not found.")

# Display final dictionary
print("\nFinal Employee Salary Dictionary:")
for name, salary in employee_salary.items():
    print(name, ":", salary)
