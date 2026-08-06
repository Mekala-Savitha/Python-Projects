country_capital={}
n=int(input("How many capitals do you want to add?"))
for i in range(n):
    country=input("Enter country name:")
    capital=input("Enter capital of that country:")
    country_capital[country]=capital
print("\nCountry Capital Dictionary:")
print(country_capital)

# Search for a country capital by name
country=input("Enter a country name to search:")
if country in country_capital:
    print("Capital:", country_capital[country])
else:
    print("Country not found")
    
# Update the capital of an existing country
country=input("Enter a country name to update:")
if country in country_capital:
    capital=input("Enter new capital name:")
    country_capital[country]=capital
    print("Capital is updated successfully")
else:
    print("Country not found")
    
# Delete a country record 
country=input("Enter a country name to delete:")
if country in country_capital:
    del country_capital[country]
    print("Country record deleted successfully")
else:
    print("Country not found")
    
# Display the final country capital records
print("\nFinal Country Capital Records:")
for country, capital in country_capital.items():
    print(country, ":", capital)
    
