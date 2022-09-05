import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    if user_input == "rock" and computer_pick == "scissors":
        print("Computer picked " + computer_pick)
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("Computer picked " + computer_pick)
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("Computer picked " + computer_pick)
        print("You won!")
        user_wins += 1
    else:
        print("Computer picked " + computer_pick)
        print("You lost!")
        computer_wins +=1

    if user_wins == 3:
        print("Victory")
        print("You score is " + str(user_wins))
        quit()
    elif computer_wins == 3:
        print("Defeat")
        print("Computer's score is " + str(computer_wins))
        quit()

print("Goodbye!")