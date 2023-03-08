import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = None
    
    def choose(self):
        self.choice = input(f"{self.name}, choose 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
    
    def __str__(self):
        return f"{self.name}: {self.score} points"
        
class Game:
    def __init__(self, rounds):
        self.rounds = rounds
        self.players = []
        self.moves = ['r', 'p', 's']
    
    def play(self):
        print("Welcome to Rock-Paper-Scissors!")
        self.get_players()
        for round in range(1, self.rounds+1):
            print(f"\nRound {round}!")
            self.play_round()
        print("\nGame over!")
        self.print_scores()
    
    def get_players(self):
        num_players = int(input("How many players? "))
        for n in range(num_players):
            name = input(f"Enter name for player {n+1}: ")
            self.players.append(Player(name))
    
    def play_round(self):
        for player in self.players:
            player.choose()
        self.print_choices()
        self.update_scores()
    
    def print_choices(self):
        print("\n")
        for player in self.players:
            print(f"{player.name} chose {self.get_move_name(player.choice)}")
    
    def update_scores(self):
        choices = [player.choice for player in self.players]
        for player in self.players:
            others = [p for p in self.players if p != player]
            for other in others:
                if self.beats(player.choice, other.choice):
                    player.score += 1
                elif player.choice != other.choice:
                    other.score += 1
    
    def beats(self, move1, move2):
        return (move1 == 'r' and move2 == 's') or (move1 == 's' and move2 == 'p') or (move1 == 'p' and move2 == 'r')
    
    def get_move_name(self, move):
        if move == 'r':
            return 'rock'
        elif move == 'p':
            return 'paper'
        elif move == 's':
            return 'scissors'
    
    def print_scores(self):
        print("\nFinal scores:")
        for player in self.players:
            print(player)
        
game = Game(rounds=3)
game.play()
