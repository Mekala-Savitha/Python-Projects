movie_ratings={}
n=int(input("How many movies do you want to add?"))
for i in range(n):
    name=input("Enter a movie name:")
    rating=int(input("Enter movie ratings from 1 to 10:"))
    movie_ratings[name]=rating
print("\nMovie Rating Dictionary:")
print(movie_ratings)

# Search a movie rating by it's name
name=input("Enter a movie name to search:")
if name in movie_ratings:
    print("Rating:", movie_ratings[name])
else:
    print("Movie not found")
    
# Update a movie's rating
name=input("Enter a movie name to update:")
if name in movie_ratings:
    rating=int(input("Enter new movie rating:"))
    movie_ratings[name]=rating
    print("Movie rating updated successfully")
else:
    print("Movie not found")
    
# Delete a movie record 
name=input("Enter a movie name to delete:")
if name in movie_ratings:
    del movie_ratings[name]
    print("Movie record deleted successfully")
else:
    print("Movie not found")
    
# Check whether a movie exists 
name=input("Enter a movie name to check:")
if name in movie_ratings:
    print("Movie found")
else:
    print("Movie not found") 
    
# Display the highest-rated movie
if movie_ratings:
    highest=max(movie_ratings,key=movie_ratings.get)
    print("\nHighest Rated Movie:",highest)
    print("Rating:",movie_ratings[highest])
else:
    print("No movie available")
    
# Display the lowest-rated movie
if movie_ratings:
    lowest=min(movie_ratings,key=movie_ratings.get)
    print("\nLowest Rated Movie:",lowest)
    print("Rating:",movie_ratings[lowest])
else:
    print("No movie available")
    
# Calculate the average rating
total=0
for value in movie_ratings.values():
    total+=value
if len(movie_ratings)>0:
    average=total/len(movie_ratings)
    print("\nAverage Rating:")
    print("Average:", average)
else:
    print("No movie records available")
   
# Display movies with ratings above 8 or more
print("\nMovies with ratings above 8 or more:")
for name, rating in movie_ratings.items():
    if rating>=8:
        print(name, ":", rating)
        
# Display movies with ratings below 5 
print("\nMovies with ratings below 5:")
for name, rating in movie_ratings.items():
    if rating<5:
        print(name, ":", rating)
        
# Sort movies by names
print("\nSorted movies by names:")
for name in sorted(movie_ratings):
    print(name, ":", movie_ratings[name])
    
# Sort movies by ratings
print("\nSorted movies by ratings:")
sorted_movies=sorted(movie_ratings.items(),key=lambda x:x[1])
for name, rating in sorted_movies:
    print(name, ":", rating)
    
