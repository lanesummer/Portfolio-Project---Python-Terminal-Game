# tic-tac-toe game

# --Imports--
import random
from tic_tac_toe_title import title

# --Title and Welcome--
# print title of game, create and print welcome message
print(title)
welcome = '''             Welcome to Tic-Tac-Toe!

*************************************************

Before the game can begin, I need to know who will be playing
'''
print(welcome)

# --Variables--
# create global variables

# new_dict is used to reset dict when you start a new game
new_dict = {'a':' ', 'b':' ', 'c':' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ', 'h':' ', 'i':' '}
new_dict_num = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
# dict is the dict that is used during the game
dict = {'a':' ', 'b':' ', 'c':' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ', 'h':' ', 'i':' '}
dict_num = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
# input dict converts the space number to its corresponding place in dict
input_dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i'}
# allow variables are used to compare-- these are the allowed values the input will be checked against
allow_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
allow_yes_no = ['yes', 'y', 'no', 'n']
allow_x_o = ['x', 'o']
# combos for winning
win_combo = [['a','b','c'], ['d','e','f'], ['g','h','i'], ['a','d','g'], ['b','e','h'], ['c','f','i'], ['a','e','i'], ['c','e','g']]

# create variables to keep track of player scores
player1_total = 0
player2_total = 0

board_key = '''
*************************************************
Input Legend:
*************************************************
Use the cooresponding number below when making your move

     |     |
  1  |  2  |  3
_____|_____|_____
     |     |
  4  |  5  |  6
_____|_____|_____
     |     |
  7  |  8  |  9
     |     |
'''


# --Functions--
# create function to print game board -- also updates board with new values
def print_board():
    board = '''
     |     |
 {a}   |  {b}  |  {c}
_____|_____|_____
     |     |
 {d}   |  {e}  |  {f}
_____|_____|_____
     |     |
 {g}   |  {h}  |  {i}
     |     |
'''.format(**dict)
    print(board)



# create function to create a player -- using player input
def create_player(num):
    name = input('''Player {num}:
    -What is your name? '''.format(num = num))
    name = name.title()
    print(' Nice to meet you {name}\n'.format(name = name))
    return name




# --Classes--
# create class --Player--
class Player():

    def __init__(self, name):
        self.name = name
        self.player = ''
        self.symbol = ''
        self.moves = []
        self.total = 0

    def make_move(self):
        choice = input('{player}, pick a number: '.format(player = self.name))
        choice = int(self.check_num(choice))
        while (dict_num[choice] == ' ') != True:
            choice = input('That space has already been played. Please try again: ')
            choice = int(choice)
        dict_num[choice] = self.symbol
        key = input_dict[choice]
        self.moves.append(key)
        print(self.moves)
        dict[key] = self.symbol
        print_board()

    def pick_symbol(self):
        choice = input("{player}, would you like to be 'X' or 'O'? ".format(player = self.name))
        self.symbol = self.check_x_o(choice).upper()
        if player1.symbol == 'X':
            player2.symbol = 'O'
        elif player1. symbol == 'O':
            player2.symbol = 'X'
        elif player2.symbol == 'X':
            player1.symbol = 'O'
        elif player2.symbol == 'O':
            player1.symbol = 'X'
        return self.symbol

    def check_win(self):
        i = 0
        while i < 8:
            x = 0
            for move in self.moves:
                if move in win_combo[i]:
                    x += 1
                    if x == 3:
                        # print('win')
                        # self.total += 1
                        return True
            i += 1
        return False

    def check_x_o(self, choice):
        check = choice.lower() in allow_x_o
        while check == False:
            choice = input('That is not a valid response. Please try again: ')
            check = choice.lower() in allow_x_o
        return choice

    def check_num(self, choice):
        check = choice in str(allow_num)
        while check == False:
            choice = input('That is not a valid response. Please try again: ')
            check = choice in str(allow_num)
        return choice





# create class --Game--
class Game():

    def __init__(self):
        self.players = player1.name, player2.name
        self.player_obj = []
        self.start_player = ''

    def play_order(self):
        order = random.randint(1,2)
        if order == 1:
            player1.player = 1
            self.start_player = player1
            self.player_obj.append(player1)
            player2.player = 2
            self.player_obj.append(player2)
            print('{player}, you have been randomly selected to go first.\n'.format(player = player1.name))
            player2.pick_symbol()

        else:
            player1.player = 2
            self.start_player = player2
            self.player_obj.append(player2)
            player2.player = 1
            self.player_obj.append(player1)
            print('{player}, you have been randomly selected to go first.\n'.format(player = player2.name))
            player1.pick_symbol()


    def game_setup(self):
        self.play_order()
        # board input legend
        print(board_key)
        # starting blank board
        print('''
*************************************************
Let\'s start playing!
*************************************************''')
        print_board()

    def play_game(self):
        i = 0
        while i <= 8:
            for player in self.player_obj:
                player.make_move()
                player.check_win()
                if player.check_win() == True or i == 8:
                    i = 9
                    player.total += 1
                    print('\n{player}, you have won the round!\n'.format(player = player.name))
                    break
                i += 1
        print('{player}: {score}'.format(player = player1.name, score = player1.total))
        print('{player}: {score}'.format(player = player2.name, score = player2.total))











# --Players--
# create players
player1 = Player(create_player(1))
player2 = Player(create_player(2))






# --Testing--
# playing with and testing current code to test functionality




game = Game()


game.game_setup()
game.play_game()
