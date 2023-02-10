import random

def rps(choice):
    strings = ["rock", "paper", "scissors"]
    opp = random.choice(strings)
    if choice == opp:
        print("Opponent chooses rock")
        print("Tie")
    elif choice == "rock":
        if opp == "paper":
            print("Opponent chooses paper")
            print("You lose :(")
        else:
            print("Opponent chooses scissors")
            print("You win!!!")
    elif choice == "paper":
        if opp == "scissors":
            print("Opponent chooses scissors")
            print("You lose :(")
        else:
            print("Opponent chooses rock")
            print("You win!!!")
    elif choice == "scissors":
        if opp == "rock":
            print("Opponent chooses rock")
            print("You lose :(")
        else:
            print("Opponent chooses paper")
            print("You win!!!")
    else:
        print("Invalid Output")

def main():
    choice = input("Please choose: rock, paper, or scissors\n")
    rps(choice)
    playAgain = input("Enter y to play again\n")
    if playAgain == "y":
        main()

main()