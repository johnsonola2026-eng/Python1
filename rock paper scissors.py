import random
while True:
    user_choice=input("choose your choice(rock,paper,scissors):")
    possible_actions=["rock","paper","scissors"]
    computer_actions=random.choice(possible_actions)
    print(f"\nyou chose {user_choice}, computer chose {computer_actions}.\n")
    if user_choice==computer_actions:
        print(f"both players selected {user_choice} it a tie!")
    elif user_choice=="rock":
        if computer_actions=="scissors":
            print("rock smashes scissors! you win!")
        else:
            print("paper covers rock! you lose.")
    elif user_choice=="paper":
        if computer_actions=="rock":
            print("paper covers rock! you win!")
        else:
            print("scissors cuts paper! you lose.")
    elif user_choice=="scissors":
        if computer_actions=="paper":
            print("scissors cuts paper! you win!")
        else:
            print("rock smashes scissors! you lose.")
    play_again=input("play again?(y/n):")
    if play_again.lower()!="y":
     break