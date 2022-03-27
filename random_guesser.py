import random

top = input("Type a number: ")
if top.isdigit():
    top = int(top)
    if(top<=0):
        print("Type a number greater than zero next time.")
        quit()
else:
    print("Please a valid number next time.")
    quit()

rand_num = random.randint(0, top)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number... ")
        continue

    if user_guess == rand_num:
        print("You got it!")
        break
    elif user_guess<rand_num:
        print("You are below the number.. ")
    else:
        print("You are above the number.. ")

print("You got it in", guess, "guesses.")