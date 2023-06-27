# tic-tac-toe game

# --Imports----------------------------------------------------------------------------------------------------
import random
from tic_tac_toe_title import *


# --Title and Welcome------------------------------------------------------------------------------------------
# print title of game, create and print welcome message
print(title)
print(welcome)


# --Variables--------------------------------------------------------------------------------------------------
# create global variables
played_moves = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
# played_moves = {}
num_played = []

allow_yes_no = ['yes', 'y', 'no', 'n']
allow_x_o = ['x', 'o']
# combos for winning
win_combo = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['1','4','7'], ['2','5','8'], ['3','6','9'], ['1','5','9'], ['3','5','7']]
# create variables to keep track of player scores for all games played
player1_total = 0
player2_total = 0




# --Functions---------------------------------------------------------------------------------------------------
# create function to create a player -- using player input
def create_player(num):
    name = input('''Player {num}:
    -What is your name? '''.format(num = num))
    name = name.title()
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

    def make_move(self):
        # # array that is used to check if choice is a number 1-9 #--------can delete later-------------
        # num_options = [1, 2, 3, 4, 5, 6, 7, 8, 9] #--------can delete later-------------
        choice = input('{player}, pick a number: '.format(player = self.name))
        print('Played moves: ') #--------can delete later-------------
        print(played_moves) #--------can delete later-------------
        print('----------------------') #--------can delete later-------------
        # check whether choice is valid--is a num 1-9 and is a spot that hasn't already been played
        while int(choice) not in range(1,10) or choice in num_played:
            if choice in num_played:
                choice = input('That space has already been played. Please try again: ')
            else:
                choice = input('That is not a valid response. Please try again: ')
        # add move to num_played array--array that is used to check if spot has already been played
        num_played.append(choice)
        print(num_played) #--------can delete later-------------
        played_moves[choice] = self.symbol
        self.moves.append(choice)
        print(played_moves) #--------can delete later-------------
        print(self.moves) #--------can delete later-------------



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

    # # create funtion to check input is allowed number #--------can delete later-------------
    # def check_num(self, choice): #--------can delete later-------------
    #     check = choice in str(allow_num) #--------can delete later-------------
    #     while check == False: #--------can delete later-------------
    #         choice = input('That is not a valid response. Please try again: ') #--------can delete later-------------
    #         check = choice in str(allow_num) #--------can delete later-------------
    #     return choice #--------can delete later-------------


# create class --Game-------------------------------------------------------------------------------------------
class Game():
    def __init__(self):
        self.players = player1.name, player2.name
        self.player_obj = []
        self.start_player = ''
        self.last_player = ''
        self.first_game = True
        # self.dict = {'a':' ', 'b':' ', 'c':' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ', 'h':' ', 'i':' '}
        # self.dict_num = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

    # create a function to determine random play order and allow player going 2nd to pick their symbol
    def play_order_old(self):
    #     order = random.randint(1,2)
    #     if order == 1:
    #         player1.player = 1
    #         self.start_player = player1
    #         self.player_obj.append(player1)
    #         player2.player = 2
    #         self.player_obj.append(player2)
    #         print('{player}, you have been randomly selected to go first.\n'.format(player = player1.name))
    #         player2.pick_symbol()
    #     else:
    #         player1.player = 2
    #         self.start_player = player2
    #         self.player_obj.append(player2)
    #         player2.player = 1
    #         self.player_obj.append(player1)
    #         print('{player}, you have been randomly selected to go first.\n'.format(player = player2.name))
    #         player1.pick_symbol()
        pass

    def play_order(self):
        # if player1.total == 0 and player2.total == 0:
        if self.first_game:
            player1.player = random.randint(1,2)
        else:
            print('Player 1 is currently: ' + str(player1.player)) #--------can delete later-------------
            if player1.player == 4:
                player1.player = 2
            else:
                player1.player = 1
        print('Player 1 is player: ' + str(player1.player) + '\n') #--------can delete later-------------
        if player1.player == 1:
            self.start_player = player1
            player2.player = 2
            self.last_player = player2
        else:
            # player1.player = 2
            self.last_player = player1
            player2.player = 1
            self.start_player = player2

        if self.first_game:
            print('{player}, you have been randomly selected to go first.\n'.format(player = self.start_player.name))
        else:
            print('{player}, you lost the last game so you will go first.\n'.format(player = self.start_player.name))

        self.last_player.pick_symbol()

        self.player_obj.append(self.start_player)
        self.player_obj.append(self.last_player)

        #     self.player_obj.append(player2) #---comment again-----------


        #     self.player_obj.append(player1) #---comment again-----------
        #     print('{player}, you have been randomly selected to go first.\n'.format(player = player2.name))
        #     player1.pick_symbol()

        # if self.players.player == 1:
        #     self.start_player = self.players
        # self.start_player = self.players.player == 1
        # print(self.start_player)





        # if player1.player == 1:
        #     # player1.player = 1 #---defined but not used in old code-----
        #     self.start_player = player1 #---defined but not used in old code-----
        #     self.player_obj.append(player1) #---comment again-----------
        #     player2.player = 2 #---defined but not used in old code-----
        #     self.player_obj.append(player2) #---comment again-----------
        #     if self.first_game:
        #         print('{player}, you have been randomly selected to go first.\n'.format(player = player.name for player.player == 1))
        #     else:
        #         print('{player}, you lost the last game so you will go first.\n'.format(player = player1.name))
        #     player2.pick_symbol()
        # else:
        #     # player1.player = 2
        #     self.start_player = player2
        #     self.player_obj.append(player2) #---comment again-----------
        #     player2.player = 1
        #     self.player_obj.append(player1) #---comment again-----------
        #     print('{player}, you have been randomly selected to go first.\n'.format(player = player2.name))
        #     player1.pick_symbol()









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
    def new_game_old(self):
    #     self.player_obj = []
    #     player1.player = ''
    #     player2.player = ''
    #     player1.symbol = ''
    #     player2.symbol = ''
    #     self.play_order()
    #     self.dict = {'a':' ', 'b':' ', 'c':' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ', 'h':' ', 'i':' '}
    #     self.dict_num = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
    #     player1.moves = []
    #     player2.moves = []
        pass

    def new_game(self):
        self.player_obj = []
        # player1.player = ''
        # player2.player = ''
        player1.symbol = ''
        player2.symbol = ''
        self.play_order()
        # self.dict = {'a':' ', 'b':' ', 'c':' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ', 'h':' ', 'i':' '}
        # self.dict_num = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
        played_moves.update({'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '})
        num_played.clear()
        print(num_played)
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
            for player in self.player_obj: #---comment again-----------
            # for player in player: ## ---uncomment ---------------
                player.make_move()
                self.print_board()
                player.check_win()
                if player.check_win() == True:
                    i = 9
                    player.total += 1
                    print('\n{player}, you have won the game!\n'.format(player = player.name))
                    player.player = 4
                    break
                elif i == 8:
                    print('It looks like a tie.\n')
                    i = 9
                    break
                i += 1
        self.first_game = False
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


# --Players-----------------------------------------------------------------------------------------------------
# create players
player1 = Player(create_player(1))
player2 = Player(create_player(2))


# --Play game---------------------------------------------------------------------------------------------------
# create game and play it
game = Game()
game.start_game()
