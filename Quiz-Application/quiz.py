score=0
question1="What is the Capital of India?"
print(question1)
answer=input("Enter your answer:")

if answer == "Delhi":
    print("Correct Answer")
    score+=1
else:
    print("Wrong Answer")
    
question2="What is the national animal of India?" 
print(question2)
answer=input("Enter your answer:")

if answer == "Tiger":
    print("Correct Answer")
    score+=1
else:
    print("Wrong Answer")
    
question3="Which planet is known as the Red Planet?"
print(question3)
answer=input("Enter your answer:")

if answer == "Mars":
    print("Correct Answer")
    score+=1
else:
    print("Wrong Answer")
    
question4="What is the largest ocean in the world?"
print(question4)
answer=input("Enter your answer:")

if answer == "Pacific":
    print("Correct Answer")
    score+=1
else:
    print("Wrong Answer")
    
question5="What color is the sky on a clear day?"
print(question5)
answer=input("Enter your answer:")

if answer == "Blue":
    print("Correct Answer")
    score+=1
else:
    print("Wrong Answer")
    
print("Total Score=",score)
