# tic-tac-toe game title and welcome

# create block letters to create the title
tic_tac = '''
 TTTTT  IIIII   CCC          TTTTT    A     CCC
   T      I    C   C           T     A A   C   C
   T      I    C      *****    T    A   A  C
   T      I    C      *****    T    AAAAA  C
   T      I    C               T    A   A  C
   T      I    C   C           T    A   A  C   C
   T    IIIII   CCC            T    A   A   CCC
  '''
toe = '''
              TTTTT   OOO   EEEEE
                T    O   O  E
                T    O   O  E
                T    O   O  EEE
                T    O   O  E
                T    O   O  E
                T     OOO   EEEEE
'''
title_line = '''
*************************************************
'''
title = title_line + tic_tac + toe + title_line

# create welcome message
welcome = '''             Welcome to Tic-Tac-Toe!

*************************************************

Before the game can begin, I need to know who will be playing
'''

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
