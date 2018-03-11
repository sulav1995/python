import random

print("Welcome to Rock, paper , scissors.\nWhat do you choose?")
Suitables = ["rock","paper","scissors"]
Player = input()
while Player not in Suitables:
    print("Please write rock,paper,scissors")
    Player = input()
Opponent = random.choice(Suitables)
print('The Opponent chose ' + Opponent + ".")
if Player == Opponent:
    print("Its a tie.")
elif Player == "rock":
    if Opponent == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif Player == "scissors":
    if Opponent == "paper":
        print("You win!")
    else:
        print("You lose!")
        
    
else:
    if Opponent == "rock":
        print("You win!")
    else:
        print("You lose!")
        
    
