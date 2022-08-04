import random
name = input("Hello, whats your name? ")
number = random.randint(1,25)
#could be randrange(1,25)
print("Hi" + name + ", I'm thinking of a number between 1 and 25.")
guessestaken = 0
#could be any name, but this line is necessary to put a limit in the game
while guessestaken < 5:
    guess = int(input("enter the guess: "))
    #this line could be the 7th or inside the conditionals
    guessestaken = guessestaken + 1
    if guess < number:
        print("that was too low")
    elif guess > number:
        print("that was too hight")
    else:
        break
if guess == number:
    print("winner the game")
else:
    print("you lose the game")
    