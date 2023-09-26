
# Guess a random number game
# - Print a message with "I am thinking a number between 1 to 20."
# - Print a message Take a guess
# - input of user for a guess
# - check if the input is right
# - if wrong, check if it is lower or higher
# - if the answer is right print a message "Saying you got it right" and execute the program
# - 7 guess only

import random
random_number = random.randint(1,20)

print("I am thinking a number between 1 to 20.")
number_guess = 0
for number_guess in range(1,7):
    print("Take a guess.")
    user_guess = int(input())

    if user_guess == random_number:
        print("You got it right, the random number is " + str(random_number))
        print("You got it in just " + str(number_guess) + " guesses")
        break
    elif user_guess > random_number:
        print("Your guest is to High!")
    elif user_guess < random_number:
        print("Your guess is to Low!")

if user_guess != random_number:
    print("You failed to guess the number. Sorry")

# while True:
#     print("Take a guess.")
#     user_guess = int(input())

    
#     if user_guess == random_number:
#         print("You got it right, the secret number is " + str(random_number))
#         break
#     elif user_guess > random_number:
#         print("Your guess is to High!")
#         continue
#     elif user_guess < random_number:
#         print("Your guess is to Low!")
#         continue
   