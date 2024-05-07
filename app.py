# import random

# options = ("rock", "paper", "scissors")
# playing = True

# while playing:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors):")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win")     
#     elif player == "paper" and computer == "rock":
#         print("You win")  
#     elif player == "scissors" and computer == "paper":
#         print("You win")  
#     else:
#         print("You lose!")

#     if  not input("Play again? (y/n): ").lower() == "y":
#         playing = False 

# print("Thanks for playing")        


import random

options = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0

while True:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        player_score += 2
    else:
        print("You lose!")
        computer_score += 2

    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")

    if player_score >= 6 or computer_score >= 6:
        break

print("Game over! Thanks for playing.")
























# options = ['rock', 'paper', 'scissors:']
# user1 = input('Enter either rock, paper or scissors')
# user2 = input('Enter either rock, paper or scissors')
# if user1 not in options:
#   print('Follow the instructions!!!!!!')
# if user2 not in options:
#   print('Follow the instructions!!!!!!')
# if user1 == user2:
#   print('It is a tie!')
# elif ( user1 == 'rock' and user2 == 'paper') or ( user1 == 'paper' and user2 == 'scissors') or ( user1 == 'scissors' and user2 == 'rock'):
#   print('Player 1 loses!')
# elif (user1 == 'rock' and user2 == 'scissors') or (user1 == 'paper' and user2 == 'rock') and (user1 == 'scissors' and user2 == 'paper'):
#   print('Player 2 wins!')
