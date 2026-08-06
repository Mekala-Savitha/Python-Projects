employees={}
n=int(input("How many employees do you want to add?"))
for i in range(n):
    id=int(input("Enter employee ID:"))
    name=input("Enter employee name:")
    age=int(input("Enter employee age:"))
    dept=input("Enter department:")
    salary=int(input("Enter employee salary RS:"))
    employees[id]={
    "name":name, 
    "age":age, 
    "department":dept, 
    "salary":salary
    }
print("\nEmployee Management System:")
print(employees)

# Search an employee by Employee ID
emp_id=int(input("Enter an employee ID to search:"))
if emp_id in employees:
    print("Employee Details:")
    print(employees[emp_id])
else:
    print("No employee found")
    
# Update an employee details
emp_id=int(input("Enter an employee ID to update:"))
if emp_id in employees:
    name=input("Enter new employee name:")
    age=int(input("Enter new age:"))
    dept=input("Enter new department:")   
    salary=int(input("Enter new salary:"))
    employees[emp_id]={
    "name":name,
    "age":age,
    "department":dept, 
    "salary":salary
    }
    print("Employee details updated successfully")
else:
    print("No employee found")
    
# Delete an employee record
emp_id=int(input("Enter an employee ID to delete:"))
if emp_id in employees:
    del employees[emp_id]
    print("Employee record deleted successfully")
else:
    print("No employee found")
    
# Check whether an employee exists
emp_id=int(input("Enter an employee ID to check:"))
if emp_id in employees:
    print("Employee found")
else:
    print("No employee exists")
    
# Display the employee with the highest salary
if employees:
    highest=max(employees, key=lambda x: employees[x]["salary"])
    print("\nEmployee with Highest Salary:")
    print("ID:", highest)
    print(employees[highest])
else:
    print("No employee available")
    
# Display the employee with the lowest salary
if employees:
    lowest=min(employees,key=lambda x: employees[x]["salary"])
    print("\nEmployee with Lowest Salary:")
    print("ID:",lowest)
    print(employees[lowest])
else:
    print("No employee available")
    
# Calculate the average salary all employees
total=0
for employee in employees.values():
    total+=employee["salary"]
if len(employees)>0:
    average=total/len(employees)
    print("Average Salary:", average)
else:
    print("No employee records available")
    
# Display employees with a salary of ₹50,000 or more
print("\nEmployees with ₹50,000 or more salary:")
for emp_id,details in employees.items():
    if details["salary"]>=50000:
        print("ID:",emp_id)
        print("Name:",details["name"])
        print("Salary:",details["salary"])
        print()
        
# Display employees with a salary of less than ₹30,000
print("\nEmployees with below ₹30,000 salary:")
for emp_id, details in employees.items():
    if details["salary"]<30000:
        print("ID:",emp_id)
        print("Name:",details["name"])
        print("Salary:",details["salary"])
        print()
        
# Sort employees by Employee ID
print("\nSorted Employees by Employee ID:")
for emp_id in sorted(employees):
    print("ID:", emp_id)
    print("Name:", employees[emp_id]["name"])
    print("Age:", employees [emp_id]["age"])
    print("Department:", employees[emp_id]["department"])
    print("Salary:", employees [emp_id]["salary"])
    print()
    
# Sort employees by employee name
print("\nSorted Employees by Name:")
sorted_employees=sorted(employees.items(), key=lambda x: x[1]["name"])
for emp_id, details in sorted_employees:
    print("ID:", emp_id)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Department:", details["department"])
    print("Salary:", details["salary"])
    print()
    
# Sort employees by salary
print("\nSorted Employees by Salary:")
sorted_employees=sorted(employees.items(),key=lambda x:x[1]["salary"])
for emp_id,details in sorted_employees:
    print("ID:", emp_id)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Department:", details["department"])
    print("Salary:", details["salary"])
    print()
    
