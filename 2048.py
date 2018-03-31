import random
import os
from copy import deepcopy
from grid import Grid

def convert(move):
    if move.lower() == 'w':
        return 'UP'
    elif move.lower() == 'a':
        return 'LEFT'
    elif move.lower() == 's':
        return 'DOWN'
    elif move.lower() == 'd':
        return 'RIGHT'

clear = lambda: os.system('cls')

if __name__ == '__main__':
    clear()
    print('Welcome to 2048')
    
    # game = Grid([[128,128,128,128], [128,128,128,128], [128,128,128,128], [128,128,128,128]])
    # game = Grid()
    game = Grid([[8, 4, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    # Main game logic
    while(True):
        clear()
        print('Score: {}'.format(game.score))
        print(game)

        # Get input from user and try move
        move = input('To play: \n    w: UP\n    a: LEFT\n    s: DOWN\n    d: RIGHT\n')
        if move.lower() == 'c':
            break
        game_old = deepcopy(game)
        game.slide(convert(move))

        # Check if move was made
        if game_old != game:
            game.addTile()
    print('Thanks for playing!')