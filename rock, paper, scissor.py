import random

while True:
 user_action = input("Enter a choice(rock, paper, scissor):")
 possible_action =["rock", "paper", "scissor"]
 computer_action = random.choice(possible_action)
 print(f"\nyou chose '{user_action}'. computer chose '{computer_action}'.\n")
 
 if user_action == computer_action:
    print(f"You both chose {user_action}. It is a tie!\n")
 elif user_action == "rock":
    if computer_action == "paper":
        print("you lose\n")
    else:
        print("you win\n") 
 elif user_action == "paper":
    if computer_action == "scissor":
        print("you lose\n")
    else:
        print("you win\n")
 elif user_action == "scissor":
    if computer_action == "rock":
        print("you lose\n")
    else:
        print("you win\n")
 play_again = input("wanna play again? (yes/no): ")
 if play_again == "no":
     break
 
