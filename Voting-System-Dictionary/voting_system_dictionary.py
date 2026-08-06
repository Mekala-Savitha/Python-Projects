 voting_system={}
n=int(input("How many candidates do you want to add?"))
for i in range(n):
    name=input("Enter candidate name:")
    votes=int(input("Enter number of votes received:"))
    voting_system[name]=votes
print("\nVoting System:")
print(voting_system)

# Search a candidate
name=input("Enter a candidate name to search:")
if name in voting_system:
    print("Number of votes received:",voting_system[name])
else:
    print("No candidate found")
    
# Update a candidate's vote count
name=input("Enter a candidate name to update:")
if name in voting_system:
    votes=int(input("Enter new votes:"))
    voting_system[name]=votes
    print("Candidate vote count updated successfully")
else:
    print("No candidate found")
    
# Delete a candidate record 
name=input("Enter a candidate name to delete:")
if name in voting_system:
    del voting_system[name]
    print("Candidate record deleted successfully")
else:
    print("No candidate found")
    
# Check whether a candidate exists 
name=input("Enter a candidate name to check:")
if name in voting_system:
    print("Candidate found")
else:
    print("Candidate not found")
    
# Display the candidate with the highest votes (winner)
if voting_system:
    highest=max(voting_system,key=voting_system.get)
    print("\nCandidate with highest votes(Winner):", highest)
    print("Votes:",voting_system[highest])
else:
    print("No candidate available")
    
# Display the candidate with the lowest votes
if voting_system:
    lowest=min(voting_system,key=voting_system.get)
    print("\nCandidate with lowest votes:",lowest)
    print("Votes:", voting_system[lowest])
else:
    print("No candidate available")
    
# Calculate the total number of votes
total=0
for value in voting_system.values():
    total+=value
print("\nTotal number of votes:",total)

# Calculate the average number of votes per candidate
total=0
for votes in voting_system.values():
    total+=votes
if len(voting_system)>0:
    average=total/len(voting_system)
    print("\nAverage number of votes per candidate:",average)
else:
    print("No candidate available")
    
# Display candidates with 100 or more votes
print("\nCandidates with 100 or more votes:")
for name, votes in voting_system.items():
    if votes>=100:
        print(name, ":", votes)
        
# Display candidates with less than 50 votes
print("\nCandidates with less than 50 votes:")
for name, votes in voting_system.items():
    if votes<50:
        print(name, ":", votes)
    
# Sort candidates by name
print("\nSorted candidates by names:")
for name in sorted(voting_system):
    print(name, ":", voting_system[name])
    
# Sort candidates by the number of votes
print("\nSorted candidates by the number of votes:")
sorted_votes=sorted(voting_system.items(),key=lambda x:x[1])
for name, votes in sorted_votes:
    print(name, ":", votes)
    
