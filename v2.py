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
# dict is the dict that is used during the game
dict = {'a':' ', 'b':' ', 'c':' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ', 'h':' ', 'i':' '}
dict_num = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
# input dict converts the space number to its corresponding place in dict
input_dict = {2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i'}

print(input_dict)
# input_dict += {1:'x'}
input_dict[1] = 'x'
print(input_dict)
# allow variables are used to compare -- these are the allowed values the input will be checked against
# allow_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
allow_yes_no = ['yes', 'y', 'no', 'n']
allow_x_o = ['x', 'o']
# combos for winning
win_combo = [['a','b','c'], ['d','e','f'], ['g','h','i'], ['a','d','g'], ['b','e','h'], ['c','f','i'], ['a','e','i'], ['c','e','g']]
# create variables to keep track of player scores for all games played
player1_total = 0
player2_total = 0
# input legend to show what numbers are used to make a move in a specific square
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
# create function to create a player -- using player input
def create_player(num):
    name = input('''Player {num}:
    -What is your name? '''.format(num = num))
    name = name.title()
    print('\nNice to meet you {name}\n'.format(name = name))
    return name


played_moves = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
num_played = []


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
        num_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # move_check = played_moves.copy()
        choice = input('{player}, pick a number: '.format(player = self.name))
        # while int(choice) not in num_options:
        #     choice = input('That is not a valid response. Please try again: ')
        # choice = int(self.check_num(choice))
        # while (game.dict_num[choice] == ' ') != True:
        print('Played moves: ')
        print(played_moves)
        print('----------------------')
        # print('Move check: ')
        # print(move_check)
        # print('----------------------')
        #----------------------------------------------------------------------------
        #-------------------------HERE------------------------------------------------
        #-----------------trying to get it to check right and still unpack the tuple correctly
        # for key, value in move_check.items():
        # while not choice:
        #     if int(choice) not in num_options:
        #         choice = input('That is not a valid response. Please try again: ')
        #         return False
        #     if choice in num_played:
        #         choice = input('That space has already been played. Please try again: ')
        #         return False
        #     return True

        while int(choice) not in num_options or choice in num_played:
            if choice in num_played:
                choice = input('That space has already been played. Please try again: ')
            else:
                choice = input('That is not a valid response. Please try again: ')
            # print(choice in num_played)
            # while choice in num_played:
                # choice = input('That space has already been played. Please try again: ')


        num_played.append(choice)
        print(num_played)
        # while choice in move_check.items():
        #     # for value in move_check.values():
        #     if value in move_check.values() != ' ':
        #         choice = input('That space has already been played. Please try again: ')
            # choice = int(self.check_num(choice))
        # move.setdefault(self.symbol, choice)
        # print('Played')
        # print(self.symbol)
        played_moves[choice] = self.symbol
        self.moves.append(choice)
        # played_moves.pop([int(choice)-1])
        # played_moves.update(move)
        print(played_moves)
        print(self.moves)

        # game.dict_num[choice] = self.symbol
        # key = input_dict[choice]
        # self.moves.append(key)
        # game.dict[key] = self.symbol

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
                        return True
            i += 1
        return False

    # create funtion to check input X/O
    def check_x_o(self, choice):
        check = choice.lower() in allow_x_o
        while check == False:
            choice = input('That is not a valid response. Please try again: ')
            check = choice.lower() in allow_x_o
        return choice

    # create funtion to check input is allowed number
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
        self.dict = {'a':' ', 'b':' ', 'c':' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ', 'h':' ', 'i':' '}
        self.dict_num = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

    # create a function to determine random play order and allow player going 2nd to pick their symbol
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

    # create function to print game board -- also updates board with new values
    # def print_board(self):
    #     board = '''
    #      |     |
    #  {a}   |  {b}  |  {c}
    # _____|_____|_____
    #      |     |
    #  {d}   |  {e}  |  {f}
    # _____|_____|_____
    #      |     |
    #  {g}   |  {h}  |  {i}
    #      |     |
    # '''.format(**self.dict)
    #     print(board)

    # def print_board(self):
    #     board = '''
    #      |     |
    #  {1}   |  {2}  |  {3}
    # _____|_____|_____
    #      |     |
    #  {4}   |  {5}  |  {6}
    # _____|_____|_____
    #      |     |
    #  {7}   |  {8}  |  {9}
    #      |     |
    # '''.format(played_moves.keys())
    #     print(board)

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
        self.player_obj = []
        player1.player = ''
        player2.player = ''
        player1.symbol = ''
        player2.symbol = ''
        self.play_order()
        self.dict = {'a':' ', 'b':' ', 'c':' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ', 'h':' ', 'i':' '}
        self.dict_num = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
        player1.moves = []
        player2.moves = []

    def end_game(self):
        # ends game - determines overall winner
        if player1.total > player2.total:
            print('''With a score of {score}
    **********
    {player} Wins!
    **********'''.format(score = player1.total, player = player1.name))
        elif player1.total < player2.total:
            print('''With a score of {score}
    **********
    {player} Wins!
    **********'''.format(score = player2.total, player = player2.name))
        else:
            print('''With a score of {score1} to {score2}
    **********
    It\'s a Tie!
    **********'''.format(score1 = player1.total, score2 = player2.total))
        print('\nThanks for playing!\n')

    def start_game(self):
        if player1.total == 0 and player2.total == 0:
            self.new_game()
            print(board_key)
            print('''
*************************************************
Let\'s start playing!
*************************************************''')
        else:
            print('''
*************************************************
Let\'s play another game!
*************************************************
''')
            self.new_game()
        self.print_board()
        game.play_game()

    # create function to play the game
    def play_game(self):
        # players make moves until someone wins or the game ends in a tie
        i = 0
        while i < 9:
            for player in self.player_obj:
                player.make_move()
                self.print_board()
                player.check_win()
                if player.check_win() == True:
                    i = 9
                    player.total += 1
                    print('\n{player}, you have won the game!\n'.format(player = player.name))
                    break
                elif i == 8:
                    print('It looks like a tie.\n')
                    i = 9
                    break
                i += 1
        # prints games scores -- how many games each player has one
        print('''Score:
        {player1}: {score1}
        {player2}: {score2}
        '''.format(player1 = player1.name, score1 = player1.total, player2 = player2.name, score2 = player2.total))
        # ask if another game wants to be played -- if yes, start new game with blank boards--totals continue
        choice = input("{player1} and {player2}, would you like to play another game? ".format(player1 = player1.name, player2 = player2.name))
        choice = self.check_yes_no(choice).lower()
        if choice == 'n' or choice == 'no':
            print('')
            self.end_game()
        elif choice == 'y' or choice == 'yes':
            self.start_game()

    # create funtion to check input yes/no
    def check_yes_no(self, choice):
        check = choice.lower() in allow_yes_no
        while check == False:
            choice = input('That is not a valid response. Please try again: ')
            check = choice.lower() in allow_yes_no
        return choice


# --Players--
# create players
player1 = Player(create_player(1))
player2 = Player(create_player(2))


# --Play game--
# create game and play it
game = Game()
game.start_game()
