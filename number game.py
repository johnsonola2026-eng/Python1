import random
playing = True
number=str(random.randint(0,9))
print("i will generate a number between 0 and 9, you have to guess the number one at a time")
print("the game ends when you get 1 hero")
while playing:
    guess=input("give me your best guess!:\n")
    if guess == number:
        print("you win the game")
        print("the number was",number)
        break
    else:
        print("your guess isn't quite right, try again.\n")