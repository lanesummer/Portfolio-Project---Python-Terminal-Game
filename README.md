# Portfolio-Project---Python-Terminal-Game
Codecademy Python Portfolio Project - create a terminal game using python

For my Portfolio Project using Python, I decided to create a 2-Player Tic-Tac-Toe game.
The players decide how many games they play. A running score of games won is kept.

Who will be the Tic-Tac-Toe champion?



# 
* tic_tac_toe.py was my first attempt at this project.
* I decided to go back and look at ways to improve/refactor the code and change some of the functionality
* tic_tac_toe_version2.py is the updated version
* In addition to making the code more readable, a big change in the updated version is the method for determining who goes first.
  In the previous version, each new game the player going first was picked randomly. In the new version, if it is the first game,
  or the previous game ended in a tie, the player going first is picked randomly. Otherwise, the player who lost the previous game
  will go first in the next game.
* Both files import variables from tic_tac_toe_print_texts.py
