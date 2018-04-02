import random
import os
from copy import deepcopy
from grid import Grid
from gridStack import GridStack

def convert(move):
    if move.lower() == 'w':
        return 'UP'
    elif move.lower() == 'a':
        return 'LEFT'
    elif move.lower() == 's':
        return 'DOWN'
    elif move.lower() == 'd':
        return 'RIGHT'

def restart():
    clear()
    game = Grid()
    print('Score: {}'.format(game.score))
    print(game)

clear = lambda: os.system('cls')

if __name__ == '__main__':
    num_row = 4
    num_col = 4

    clear()
    print('Welcome to 2048')

    custom = input('Would you like a custom grid size? (y/n)')

    if custom.lower() == 'y':
        num_row = int(input('Enter number of rows: '))
        num_col = int(input('Enter number of cols: '))

    game = Grid(rows=num_row, cols=num_col)
    stack = GridStack()
    win = False

    # Main game logic
    while(True):
        clear()
        print('Score: {}'.format(game.score))
        print(game)

        # Check for game over
        if game.checkGameOver():
            print('Game Over! Your score was {}\n'.format(game.score))
            replay = input('Play again? (y/n)')
            if replay.lower() == 'y':
                restart()
            else:
                break

        # Check for win condition
        if game.checkWin() and not win:
            print('You Win! Your score was {}\n'.format(game.score))
            cont = input('Continue? (y/n)')
            if cont.lower() == 'y':
                win = True
            else:
                replay = input('Play again? (y/n)')
                if replay.lower() == 'y':
                    restart()
                else:
                    break


        # Get input from user and try move
        move = input('To play: \n    w: UP\tc: QUIT\n    a: LEFT\tu: UNDO\n    s: DOWN\n    d: RIGHT\n')
        if move.lower() == 'c':
            break

        # Undo
        if move.lower() == 'u':
            game.undo()
            continue

        stack.push(deepcopy(game))
        game.slide(convert(move))

        # Only add tile when tiles moved
        if stack.top() != game:
            game.addTile()


    print('Thanks for playing!')