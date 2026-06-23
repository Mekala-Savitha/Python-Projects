# Number Guessing Game 

secret_number=3

while True:
    guess=int(input("Enter your guess:"))
    
    if guess==secret_number:
        print("You Won")
        break
    elif guess>secret_number:
        print("Too High")
    else:
        print("Too Low")
        
