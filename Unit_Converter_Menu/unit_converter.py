def celsius_to_fahrenheit():
    celsius=float(input("Enter Celsius temperature:"))
    fahrenheit=(celsius * 9/5 + 32)
    return fahrenheit 
    
def fahrenheit_to_celsius():
    fahrenheit=float(input("Enter fahrenheit temperature:"))
    celsius=(fahrenheit - 32) * 5/9
    return celsius 
    
while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Fahrenheit=",celsius_to_fahrenheit())
    elif choice==2:
        print("Celsius=",fahrenheit_to_celsius())
    elif choice==3:
        print("Thank you for choosing Unit Converter Menu")
        break
    else:
        print("Invalid choice")          
