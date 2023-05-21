# tic-tac-toe game

# --Imports--
import random
from tic_tac_toe_title import title

# --Title and Welcome--
# print title of game, create and print welcome message
print(title)
welcome = 'Welcome to Tic-Tac-Toe!\n'
print(welcome)

# --Variables--
# create global variables

new_dict = {'a': ' ', 'b': ' ', 'c': ' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ', 'h':' ', 'i':' '}
dict = {'a': ' ', 'b': ' ', 'c': ' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ', 'h':' ', 'i':' '}
input_dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i'}

board_key = '''
  Input Legend:
    -use the following numbers when making your move

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
print(board_key)

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

# --Classes--
# create class --Player--
class Player():

    def __init__(self, name):
        self.name = name
        self.player = ''
        self.symbol = ''

    def make_move(self, num):
        key = input_dict[num]
        dict[key] = self.symbol

    def get_order(self):
        pass

def create_player():
    name = input('What is your name? ')
    return name
