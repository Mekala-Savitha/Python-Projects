scorecard={}
n=int(input("How many players are in the team?"))
for i in range(n):
    name=input("Enter player name:")
    runs=int(input("Enter runs scored:"))
    scorecard[name]=runs
print("\nCricket Scorecard Dictionary:")
print(scorecard)

# Search a player's score 
name=input("Enter a player name to search:")
if name in scorecard:
    print("Score:", scorecard [name])
else:
    print("Player not found")
    
# Update a player's runs
name=input("Enter a player name to update:")
if name in scorecard:
    runs=int(input("Enter new runs:"))
    scorecard[name]=runs
    print("Player's runs updated successfully")
else:
    print("Player not found")
    
# Delete a player's record 
name=input("Enter a player's name to delete:")
if name in scorecard:
    del scorecard[name]
    print("Player's record deleted successfully")
else:
    print("Player not found")
    
# Check whether a player exists 
name=input("Enter a player name to check:")
if name in scorecard:
    print("Player found")
else:
    print("Player not found")
    
# Display a player with highest score 
if scorecard:
    highest = max(scorecard,key = scorecard.get)
    print("\nPlayer with highest score:", highest)
    print("Highest Score:",scorecard[highest])
else:
    print("No player records available")

# Display a player with lowest score 
if scorecard:
    lowest = min(scorecard,key=scorecard.get)
    print("\nPlayer with lowest score:",lowest)
    print("Lowest Score:", scorecard[lowest])
else:
    print("No player records available")

# Calculate the total team score
total=0
for value in scorecard.values():
    total+=value
print("\nTotal Team Score:",total)

# Calculate the average runs per player
total=0
for runs in scorecard.values():
    total+=runs
if len(scorecard)>0:
    average=total/len(scorecard)
    print("\nAverage Runs per Player:", average)
else:
    print("No player records available.")
    
# Display players who scored a half-century(50 or more runs)
print("\nPlayers who scored a half-century:")
for name, runs in scorecard. items():
    if runs>=50:
        print(name, ":", runs)
        
# Display players who scored a century (100 or more runs)
print("\nPlayers who scored a century:")
for name, runs in scorecard. items():
    if runs>=100:
        print(name, ":", runs)
        
# Display players who got out for zero (Duck)
print("\nPlayers who got out for zero:")
for name, runs in scorecard. items():
    if runs==0:
        print(name, ":", runs)
        
# Sort players by name
print("\nSorted players by names:")
for name in sorted(scorecard):
    print(name, ":", scorecard[name])
    
# Sort players by runs
print("\nSorted players by runs:")
sorted_players=sorted(scorecard.items(), key=lambda x: x[1])
for name, runs in sorted_players:
    print(name, ":", runs)
