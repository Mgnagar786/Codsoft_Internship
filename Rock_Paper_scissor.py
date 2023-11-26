import random

options = ("rocks", "paper", "scissors")
running = True

while True:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a Tie")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print("you win")
    else:
        print("you lose!")

    if not input("play again? (y/n): ").lower() == "Y":
        break

print("Thanks for Playing!")



