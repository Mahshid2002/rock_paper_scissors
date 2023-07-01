import random

user_score = 0
computer_score = 0

options = ["rock" , "paper" , "scissors"]   # indeces start at 0
 
while True:
    user_input = input("Type rock/paper/scissors or quit: ").lower()
    if user_input == "quit":
        break

    if user_input not in ["rock" , "paper" , "scissors"]:
        continue    # which means start the loop again

    random_number = random.randint(0,2)
    # rock: 0 , paper: 1 , scissors: 2
    computer_pick = options[random_number]
    print("comp picked", computer_pick ,".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won")
        user_score += 1 
        
    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        user_score += 1 
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won")
        user_score += 1 
    elif user_input == "rock" and computer_pick == "rock":
        print("non of you wins")
    elif user_input == "paper" and computer_pick == "paper":
        print("non of you wins")
    elif user_input == "scissors" and computer_pick == "scissors":
        print("non of you wins")

    else:
        print("Computer wins")
        computer_score += 1

print("You won" , user_score , "times.")
print("computer won" , computer_score , "times.")
print("Thanks for playing")
    

 