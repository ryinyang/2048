from random import randint, choice
from tile import Tile
from copy import deepcopy

class Grid:
    grid = [[]]
    score = 0
    num_rows = 0
    num_cols = 0

    def __init__(self, arrays=None, cols=4, rows=4):
        self.score = 0
        # Creates a random grid with 2 random tiles
        if not arrays:
            self.grid = [[Tile(0) for x in range(cols)] for y in range(rows)]
            self.num_rows = rows
            self.num_cols = cols
            self.addTile()
            self.addTile()

        # Create a predetermined grid
        if arrays: 

            self.grid = []
            width = len(arrays[0])
            for r in arrays:
                assert(width == len(r)), 'Rows must have same lengths'
                row = []
                width = len(r)
                for num in r:
                    row.append(Tile(num))
                self.grid.append(row)
            self.num_rows = len(self.grid)
            self.num_cols = len(self.grid[0])

    def __str__(self):
        ret = ''
        for row in self.grid:
            for t in row:
                if t.val != 0:
                    ret += '{: ^6}'.format(str(t.val))
                else:
                    ret += '{: ^6}'.format('_')
                # ret += str(t.val) + ' '
            ret += '\n\n'
        # ret += 'Grid is {} by {}\n'.format(self.num_rows, self.num_cols)
        return ret

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if self.grid[r][c] != other.grid[r][c]:
                    return False
        return True

    def checkGameOver(self):
        """
        Returns True if there are no more moves to make, else False
        """
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        counter = 0

        # Try all moves and count non-moves
        for direction in directions:
            test_grid = deepcopy(self)
            test_grid.slide(direction)
            if test_grid == self:
                counter += 1

        return counter == 4

    def slide(self, direction):
        """
        Slides all the tiles in the direction of the key press
        :return: None
        """

        def slideTiles(r, c):
            """Helper function to slide the tiles and merge. Helps reduce redundant code"""
            global merged
            currTile = self.grid[r][c]
            if currTile.val != 0:
                if len(shifted) > 0:
                    if shifted[-1] == currTile and not merged:
                        merged = True
                        shifted.pop()
                        shifted.append(Tile(currTile.val*2))
                        self.score += currTile.val * 2
                    else:
                        shifted.append(currTile)
                        merged = False
                else:
                    shifted.append(currTile)
                    merged = False

        if direction == 'UP':
            for c in range(self.num_cols):
                shifted = []
                merged = False
                for r in range(self.num_rows):
                    slideTiles(r, c)

                # Copy over new column
                for i in range(self.num_cols - len(shifted)):
                    shifted.append(Tile(0))
                for i, new in enumerate(shifted):
                    self.grid[i][c] = new

        elif direction == 'RIGHT':
            for r in range(self.num_rows):
                shifted = []
                merged = False
                for c in range(3, -1, -1):
                    slideTiles(r, c)

                # Copy over new row
                for i in range(self.num_rows - len(shifted)):
                    shifted.append(Tile(0))
                self.grid[r] = list(reversed(shifted))

        elif direction == 'DOWN':
            for c in range(self.num_cols):
                shifted = []
                merged = False
                for r in range(3, -1, -1):
                    slideTiles(r, c)

                # Copy over new column
                for i in range(self.num_cols - len(shifted)):
                    shifted.append(Tile(0))
                for i, new in enumerate(reversed(shifted)):
                    self.grid[i][c] = new


        elif direction == 'LEFT':
            for r in range(self.num_rows):
                shifted = []
                merged = False
                for c in range(self.num_cols):
                    slideTiles(r, c)

                # Copy over new row
                for i in range(self.num_rows - len(shifted)):
                    shifted.append(Tile(0))
                self.grid[r] = list(shifted)

    def addTile(self,num=None, x=None, y=None):
        """
        Randomly adds a 2 or a 4 tile into an open space
        :return: None
        """
        if x == None or y == None or num == None:
            loc = []
            nums = [2, 4]

            # Loop through grid and compile empty tiles
            for i, r in enumerate(self.grid):
                for j, c in enumerate(r):
                    if c.val == 0:
                        loc.append((i,j))

            # Choose a location and add a random value
            coord = choice(loc)
            self.grid[coord[0]][coord[1]].setVal(choice(nums))

    def checkWin():
        """
        Checks grid to see if there is a 2048 tile.
        :return: True if there is, else False
        """

        # Loop through all tiles and check for 2048
        for r in range(4):
            for c in range(4):
                if self.grid.val == 2048:
                    return True
        return False