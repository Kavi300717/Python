import random

def play_game():
    '''Function to play a single rond of Rock, Paper, Scissors'''
    print("Welcome to Rock, Paper, Scissor")

    moves = {1: "Rock", 2: "Paper", 3: "Scossor"}

    player_move = int(input("Select your move(1 for Rock, 2 for Paper, 3 for Scissor) : "))

    if player_move not in moves:
        print("Invalid input. Please enter 1, 2, or 3.")
        return
    
    computer_move = random.randint(1,3)
    print(f"Computer chose {moves[computer_move]}. You chose {moves[player_move]}")

    if player_move == computer_move:
        print("It's a tie.")
    elif (player_move == 2 and computer_move == 3) or \
        (player_move == 2 and computer_move == 1) or \
        (play_move == 3 and computer_move == 2) :
        print("You Win!")
    else:
        print("You lose!")

play_game()