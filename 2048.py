import random
import os
from grid import Grid

clear = lambda: os.system('cls')

if __name__ == '__main__':
    clear()
    print('Welcome to 2048')
    
    game = Grid([[2, 2, 2, 0], [2, 0, 2, 0], [0, 2, 2, 0], [0, 0, 2, 2]])
    print(game)

    # Main game logic
    while(True):
        game.slide('LEFT')
        print(game)
        break