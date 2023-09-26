# Rock Paper Scissors Game
# - print a title
# - print the score
# - print enter your move (r) for rock, p for paper, s for scissors
# - check the what bot pick
# - check who wins
# - update score
# - print a message who win or lose
# - 6 tries

import random

print ("ROCK, PAPER, SCISSOR")
user_score = 0
computer_score = 0
draw = 0
player_text = ""

computer_choice = ["r","p","s"]



for i in range(1,6):
   
    print(str(user_score) + " Wins, " + str(computer_score) + " Losses, " + str(draw) + " Ties ")
    print("Enter your move: (r)ock (p)aper (s)cissor or (q)uit")
    player = input()

    if(player == "r"):
        player_text = "ROCK"
    elif(player == "p"):
        player_text = "PAPER"
    elif(player == "s"):
        player_text = "SCISSOR"
    elif(player == "q"):
        break

    
    print(player_text + " versus...")
    
    computer_pick = (random.choice(computer_choice))

    if(computer_pick == "r"):
        computer_text = "ROCK"
    elif(computer_pick == "p"):
        computer_text = "PAPER"
    elif(computer_pick == "s"):
        computer_text = "SCISSOR"

    print(computer_text)


    # decide who win
    if player == "p" and computer_pick == "r":
        print("You win!")
        user_score = user_score + 1
    elif player == "r" and computer_pick == "s":
        print("You win!")
        user_score = user_score + 1
    elif player == "s" and computer_pick == "p":
        print("You win!")
        user_score = user_score + 1

    elif player == "r" and computer_pick == "p":
        print("You lose!")
        computer_score = computer_score + 1
    elif player == "s" and computer_pick == "r":
        print("You lose!")
        computer_score = computer_score + 1
    elif player == "p" and computer_pick == "s":
        print("You lose!")
        computer_score = computer_score + 1
    elif player == computer_pick:
        print("It's a draw!")
        draw = draw + 1
    else:
        print("Invalid input")

print("FINAL SCORE: " + str(user_score) + " Wins, " + str(computer_score) + " Losses, " + str(draw) + " Ties ")
if user_score > computer_score:
    print("You win the series match!")
elif user_score < computer_score:
    print("Computer win in the series match!")
else:
    print("It's a draw in a series match")