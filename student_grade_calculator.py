# Student Grade Calculator 

Maths=int(input("Enter Maths marks: "))
English=int(input("Enter English marks: "))
Science=int(input("Enter Science marks: "))
Social=int(input("Enter Social marks: "))
Telugu=int(input("Enter Telugu marks: "))

def total_marks(Maths, English, Science, Social, Telugu):
    total=Maths+English+Science+Social+Telugu 
    return total
total=total_marks(Maths, English, Science, Social, Telugu)
  
average=total/5
    
if Maths<35 or English<35 or Science<35 or Social<35 or Telugu<35:
    grade="Fail" 
elif average>=90:
    grade="A+" 
elif average>=80:
    grade="A"
elif average>=70:
    grade="B"
elif average>=60:
    grade="C"
else:
    grade="Fail"
    
print("Total Marks=",total)
print("Average=", average)
print("Grade=",grade) 
  
