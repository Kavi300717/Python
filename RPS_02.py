import random #for random module 

class RockPaperScissor:
    '''Class to handle the Rock, Paper, Scissor game'''

    def __init__(self):
        self.moves = {1: "Rock", 2: "Paper", 3: "Scissor"}
        print("Welcome to Rock, Paper, Scissor!")

    def get_player_move(self):
        try:
            player_move = int(input("Select your move(1 for Rock, 2 for Paper, 3 for Scisscor) : "))
            if player_move not in self.moves:
                print("Invalid input. Please enter 1, 2, or 3.")
                return None
            return player_move
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def get_computer_move(self):
        return random.randint(1,3)

    def determine_winner(self, player_move, computer_move):
        print(f"Computer chose {self.moves[computer_move]}. You chose {self.moves[player_move]}.")

        if player_move == computer_move:
            print("It's a Tie!")
        elif (player_move == 1 and computer_move == 3) or \
        (player_move == 2 and computer_move == 1) or \
        (player_move == 3 and computer_move == 2):
            print("You win!")
        else:
            print("You lose!")

    def play(self):
        player_move = self.get_player_move()
        if player_move:
            computer_move = self.get_computer_move()
            self.determine_winner(player_move, computer_move)

game = RockPaperScissor()
game.play()