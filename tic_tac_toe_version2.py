# tic-tac-toe game

# --Imports----------------------------------------------------------------------------------------------------
import random
from tic_tac_toe_print_texts import *

# --Title and Welcome------------------------------------------------------------------------------------------
# print title of game, create and print welcome message
print(title)
print(welcome)

# --Variables--------------------------------------------------------------------------------------------------
# create variables to track moves made in a game
played_moves = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
num_played = []
# combos for winning
win_combo = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['1','4','7'], ['2','5','8'], ['3','6','9'], ['1','5','9'], ['3','5','7']]
# create variables to keep track of player scores for all games played
player1_total = 0
player2_total = 0

# --Function outside classes---------------------------------------------------------------------------------------------------
# create function to create a player -- using player input
def create_player(num):
    name = input('''Player {num}:
    -What is your name? '''.format(num = num)).title()
    print('\nNice to meet you {name}\n'.format(name = name))
    return name

# --Classes-----------------------------------------------------------------------------------------------------
# create class --Player-----------------------------------------------------------------------------------------
class Player():
    def __init__(self, name):
        self.name = name
        self.player = ''
        self.symbol = ''
        self.moves = []
        self.total = 0

    # create function to take input from player, check and store it to make a move
    def make_move(self):
        choice = input('{player}, pick a number: '.format(player = self.name))
        # check whether choice is valid--is an integer 1-9 and is a spot that hasn't already been played
        while not choice.isdigit() or int(choice) not in range(1,10) or choice in num_played:
            if choice in num_played:
                choice = input('That space has already been played. Please try again: ')
            else:
                choice = input('That is not a valid response. Please try again: ')
        # add move to num_played array--array that is used to check if spot has already been played
        num_played.append(choice)
        played_moves[choice] = self.symbol
        self.moves.append(choice)
        game.print_board()

    # create function to have player going 2nd pick if they want X or O
    def pick_symbol(self):
        choice = input("{player}, would you like to be 'X' or 'O'? ".format(player = self.name)).upper()
        # check whether choice is valid
        while not choice in ['X', 'O']:
            choice = input('That is not a valid response. Please try again: ').upper()
        self.symbol = choice
        return self.symbol

    # create function to check if player has a winning combo (won the game)
    def check_win(self):
        for combo in win_combo:
            x = 0
            for move in self.moves:
                if move in combo:
                    x += 1
                    if x == 3: return True
        return False

# create class --Game-------------------------------------------------------------------------------------------
class Game():
    def __init__(self):
        self.players = player1.name, player2.name
        self.start_player = ''
        self.last_player = ''
        self.random_order = True

    # create a function to determine random play order and allow player going 2nd to pick their symbol
    def play_order(self):
        # if first game or last game tie--random select player to go first
        if self.random_order:
            player1.player = random.randint(1,2)
        # player who lost last game goes first
        else:
            player1.player = 2 if player1.player == 4 else 1
        # assign player numbers (1 or 2), start player and last player
        if player1.player == 1:
            self.start_player = player1; player2.player = 2; self.last_player = player2
        else:
            self.last_player = player1; player2.player = 1; self.start_player = player2
        # print statement with which player goes first
        if self.random_order:
            print('{player}, you have been randomly selected to go first.\n'.format(player = self.start_player.name))
        else:
            print('{player}, you lost the last game so you will go first.\n'.format(player = self.start_player.name))
        # player not going first gets to pick their symbol (X or O), set symbol for other player
        self.last_player.pick_symbol()
        self.start_player.symbol = 'O' if self.last_player.symbol == 'X' else 'X'

    # create function to print game board -- also updates board with new values after a move is made
    def print_board(self):
        board = '''
         |     |
     {0}   |  {1}  |  {2}
    _____|_____|_____
         |     |
     {3}   |  {4}  |  {5}
    _____|_____|_____
         |     |
     {6}   |  {7}  |  {8}
         |     |
    '''.format(*played_moves.values())
        print(board)

    # create function to reset all values to begin a game
    def new_game(self):
        self.play_order()
        played_moves.update({'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '})
        num_played.clear()
        player1.moves = []
        player2.moves = []

    def end_game(self):
        # ends game - determines and prints overall winner
        win_player = player1 if player1.total > player2.total else player2 if player1.total < player2.total else 'tie'
        if win_player == 'tie':
            print(tie_message.format(score1 = player1.total, score2 = player2.total))
        else:
            print(win_message.format(score = win_player.total, player = win_player.name))
        print('\nThanks for playing!\n')


    def start_game(self):
        if player1.total == 0 and player2.total == 0:
            self.new_game()
            print(board_key)
            print(start_message_new)
        else:
            print(start_message_more)
            self.new_game()
        self.print_board()
        game.play_game()

    # create function to play the game
    def play_game(self):
        # players make moves until someone wins or the game ends in a tie
        i = 0
        while i < 9:
            player = self.start_player if i % 2 == 0 else self.last_player
            player.make_move()
            if player.check_win() == True:
                i = 9
                player.total += 1
                print('\n{player}, you have won the game!\n'.format(player = player.name))
                player.player = 4
                self.random_order = False
            elif i == 8:
                print('It looks like a tie.\n')
                i = 9
                self.random_order = True
            i += 1

        # game ended -- then prints games scores -- how many games each player has one overall
        print('''Score:
        {player1}: {score1}
        {player2}: {score2}
        '''.format(player1 = player1.name, score1 = player1.total, player2 = player2.name, score2 = player2.total))

        # ask if another game wants to be played -- if yes, start new game with blank boards--totals continue
        choice = input("{player1} and {player2}, would you like to play another game? ".format(player1 = player1.name, player2 = player2.name)).lower()
        while choice not in ['yes', 'y', 'no', 'n']:
            choice = input('That is not a valid response. Please try again: ').lower()
        if choice in ('n', 'no'): #'n' or choice == 'no':
            self.end_game()
        elif choice in ('y', 'yes'):
            self.start_game()

# --Players-----------------------------------------------------------------------------------------------------
# create players
player1 = Player(create_player(1))
player2 = Player(create_player(2))

# --Play game---------------------------------------------------------------------------------------------------
# create game and play it
game = Game()
game.start_game()
