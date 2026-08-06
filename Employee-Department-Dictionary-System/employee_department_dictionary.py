emp_dept={}
n=int(input("How many departmens do you want to add?"))
for i in range(n):
    name=input("Enter an employee name:")
    dept=input("Enter department:")
    emp_dept[name]=dept
print("\nEmployee Department Dictionary:")
print(emp_dept)

# Search for an employee department by name
name=input("Enter an employee name to search:")
if name in emp_dept:
    print("Department:", emp_dept[name])
else:
    print("Employee not found")
    
# Update the department of an existing employee 
name=input("Enter an employee name to update:")
if name in emp_dept:
    dept=input("Enter new department:")
    emp_dept[name]=dept
    print("Department updated successfully")
else:
    print("Employee not found")

# Delete an employee records
name=input("Enter an employee name to delete:")
if name in emp_dept:
    del emp_dept[name]
    print("Employee record deleted successfully")
else:
    print("Employee not found")
    
# Display final employee department records
print("\nFinal Employee Department Records:")
for name, dept in emp_dept.items():
    print(name, ":", dept)

  
