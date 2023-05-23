''''
This is a game of rock, paper, scissors. user will choose rock, paper, or scissors. computer will choose rock, paper, or scissors.
we will display the result of the game. user can quit or play again.

'''

import random

user_score_count = 0
computer_score_count = 0
user_score = 0
computer_score = 0

def score_tally():
    global user_score
    global computer_score
    if user_score == computer_score:
        print("Tie!")
    if user_score > computer_score:
        print("You win!")
    if user_score < computer_score:
        print("You lose!")

while True:
    user_input = input("Enter rock, paper, or scissors: ").lower()
    computer_input = random.choice(["rock", "paper", "scissors"])
    print(f"You chose {user_input} and computer chose {computer_input}.")

    if user_input == computer_input:
        print(f"user score is {user_score_count} and computer score is {computer_score_count}.")
        print("Tie!")
    elif user_input == "rock" and computer_input == "scissors":
        user_score_count = user_score_count + 1
        print("you win!")
        print(f"user score is {user_score_count} and computer score is {computer_score_count}.")

    elif user_input == "paper" and computer_input == "rock":
        user_score_count = user_score_count + 1
        print("you win!")
        print(f"user score is {user_score_count} and computer score is {computer_score_count}.")
    elif user_input == "scissors" and computer_input == "paper":
        user_score_count = user_score_count + 1
        print("you win!")
        print(f"user score is {user_score_count} and computer score is {computer_score_count}.")
    else:
        computer_score_count = computer_score_count + 1
        print("You lose!")
        print(f"user score is {user_score_count} and computer score is {computer_score_count}.")

    continue_game = input("Do you want to play again? (y/n): ").lower()
    if continue_game != "y":
        break

print("Thanks for playing!")
