hospital={}
n=int(input("How many patients do you want to add?"))
for i in range(n):
    id=int(input("Enter patient ID:"))
    name=input("Enter patient name:")
    age=int(input("Enter patient age:"))
    disease=input("Enter disease:")
    doctor=input("Enter doctor name:")
    bill=int(input("Enter Bill Amount RS:"))
    hospital[id]={
    "name":name, 
    "age":age, 
    "disease": disease, 
    "doctor": doctor, 
    "bill":bill
    }
print("\nHospital Management System:")
print(hospital)

# Search a patient by Patient ID
patient_id=int(input("Enter a patient ID to search:"))
if patient_id in hospital:
    print("Hospital Details:")
    print(hospital [patient_id])
else:
    print("No patient found")
    
# Update patient details
patient_id=int(input("Enter a patient ID to update:"))
if patient_id in hospital:
    name=input("Enter new patient name:")
    age=int(input("Enter new patient age:"))
    disease=input("Enter new disease name:")
    doctor=input("Enter new doctor:")
    bill=int(input("Enter new bill:"))
    hospital[patient_id]={
    "name":name, 
    "age":age, 
    "disease": disease, 
    "doctor": doctor, 
    "bill":bill
    }
    print("Patient details updated successfully")
else:
    print("No patient found")
    
# Delete a patient record
patient_id=int(input("Enter a patient ID to delete:"))
if patient_id in hospital:
    del hospital[patient_id]
    print("Patient record deleted successfully")
else:
    print("No patient found")
    
# Check whether a patient exists
patient_id=int(input("Enter a patient ID to check:"))
if patient_id in hospital:
    print("Patient found")
else:
    print("No patient found")
    
# Display the patient with the highest bill amount
if hospital:
    highest=max(hospital,key=lambda x: hospital[x]["bill"])
    print("Patient with highest bill amount:")
    print("ID:", highest)
    print(hospital[highest])
else:
    print("No patient available")
   
# Display the patient with the lowest bill amount
if hospital:
    lowest=min(hospital,key=lambda x: hospital[x]["bill"])
    print("Patient with lowest bill amount")
    print("ID:",lowest)
    print(hospital[lowest])
else:
    print("No patient available")
    
# Calculate the average bill amount
total=0
for patient in hospital.values():
    total+=patient ["bill"]
if len(hospital)>0:
    average=total/len(hospital)
    print("Average Bill Amount:", average)
else:
    print("No patient records available")
    
# Display patients whose bill is ₹50,000 or more
print("\nPatients  with ₹50,000 or more bill:")
for patient_id, details in hospital.items():
    if details["bill"]>=50000:
        print("ID:", patient_id)
        print("Name:", details["name"])
        print("bill:",details["bill"])
        print()
        
# Display patients whose bill is less than ₹10,000
print("\nPatients  with ₹10,000 or less bill:")
for patient_id, details in hospital.items():
    if details["bill"]<10000:
        print("ID:", patient_id)
        print("Name:", details["name"])
        print("bill:",details["bill"])
        print()
        
# Sort patients by Patient ID
print("\nSorted Patients by Patient ID:")
for patient_id in sorted(hospital):
    print("ID:", patient_id)
    print("Name:", hospital [patient_id]["name"])
    print("Age:", hospital [patient_id]["age"])
    print("Disease:", hospital [patient_id]["disease"])
    print("Doctor:", hospital [patient_id]["doctor"])
    print("Bill:", hospital[patient_id]["bill"])
    print()
    
# Sort patients by Patient Name
print("\nSorted Patients by Name:")
sorted_hospital=sorted(hospital.items(),key=lambda x: x[1]["name"])
for patient_id, details in sorted_hospital:
    print("ID:", patient_id)
    print("Name:",details["name"])
    print("Age:", hospital [patient_id]["age"])
    print("Disease:", hospital [patient_id]["disease"])
    print("Doctor:", hospital [patient_id]["doctor"])
    print("Bill:", hospital[patient_id]["bill"])
    print()
    
# Sort patients by Bill Amount
print("\nSorted Patients by Bill Amount:")
sorted_hospital=sorted(hospital.items(),key=lambda x: x[1]["bill"])
for patient_id, details in sorted_hospital:
    print("ID:", patient_id)
    print("Name:",details["name"])
    print("Age:", hospital [patient_id]["age"])
    print("Disease:", hospital [patient_id]["disease"])
    print("Doctor:", hospital [patient_id]["doctor"])
    print("Bill:", hospital[patient_id]["bill"])
    print()
   
