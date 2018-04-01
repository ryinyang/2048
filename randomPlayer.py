import os
import time
from copy import deepcopy
from grid import Grid
from random import choice

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
    clear()
    print('Welcome to 2048')
    trials = []
    
    for i in range(1):
        game = Grid(rows=10, cols=10)
        win = False
        num_moves = 0

        # Main game logic
        while(True):
            clear()
            print('Trial: {}\nScore: {}    Number of Moves: {}'.format(i, game.score, num_moves))
            print(game)

            # Check for game over
            if game.checkGameOver():
                # print('Game Over! Your score was {}\n'.format(game.score))
                break

            # Check for 2048
            # if game.checkWin():
            #     break

            # Randomize a move
            game_old = deepcopy(game)
            game.slide(choice(['UP', 'DOWN', 'LEFT', 'RIGHT']))

            # Only add tile when tiles moved
            if game_old != game:
                game.addTile()
                num_moves += 1

            # time.sleep(.1)

        print('Thanks for playing!')
        print('Number of moves: {}'.format(num_moves))
        trials.append((num_moves, game.score))

    print(trials)
    print('Average number of moves: {}'.format(sum([i[0] for i in trials])/len(trials)))
    print('Average score: {}'.format(sum([i[1] for i in trials])/len(trials)))