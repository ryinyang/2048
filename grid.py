from random import randint, choice, choices
from tile import Tile
from copy import deepcopy
from gridStack import GridStack

class Grid:
    grid = [[]]
    stack = None
    score = 0
    num_rows = 0
    num_cols = 0

    def __init__(self, arrays=None, cols=4, rows=4):
        """
        Creates the Grid object

        :arrays: 2d array that will populate the grid
        :cols: number of columns in the grid
        :rows: number of rows in the grid
        :raises AssertionError: raises error when array is not rectangular
        """

        self.score = 0
        self.stack = GridStack()

        # Creates a random grid with 2 random tiles
        if not arrays:
            self.grid = [[Tile(0) for x in range(cols)] for y in range(rows)]
            self.addTile()
            self.addTile()

        # Create a predetermined grid
        else: 
            assert(isinstance(arrays[0], list)), 'Creating game with array failed. Must pass 2D array.'
            
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
            ret += '\n\n'
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
        """Returns True if there are no more moves to make, else False"""

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

        :direction: str representing where the tiles will slide
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
            # Loop through grid in opp dir and collect non-zero tiles
            for c in range(self.num_cols):
                shifted = []
                merged = False
                for r in range(self.num_rows):
                    slideTiles(r, c)

                # Copy over new column
                for i in range(self.num_rows - len(shifted)):
                    shifted.append(Tile(0))
                for i, new in enumerate(shifted):
                    self.grid[i][c] = new

        elif direction == 'RIGHT':
            # Loop through grid in opp dir and collect non-zero tiles
            for r in range(self.num_rows):
                shifted = []
                merged = False
                for c in range(self.num_cols-1, -1, -1):
                    slideTiles(r, c)

                # Copy over new row
                for i in range(self.num_cols - len(shifted)):
                    shifted.append(Tile(0))
                self.grid[r] = list(reversed(shifted))

        elif direction == 'DOWN':
            # Loop through grid in opp dir and collect non-zero tiles
            for c in range(self.num_cols):
                shifted = []
                merged = False
                for r in range(self.num_rows-1, -1, -1):
                    slideTiles(r, c)

                # Copy over new column
                for i in range(self.num_rows - len(shifted)):
                    shifted.append(Tile(0))
                for i, new in enumerate(reversed(shifted)):
                    self.grid[i][c] = new


        elif direction == 'LEFT':
            # Loop through grid in opp dir and collect non-zero tiles
            for r in range(self.num_rows):
                shifted = []
                merged = False
                for c in range(self.num_cols):
                    slideTiles(r, c)

                # Copy over new row
                for i in range(self.num_cols - len(shifted)):
                    shifted.append(Tile(0))
                self.grid[r] = list(shifted)

    def addTile(self):
        """
        Randomly adds a 2 or a 4 tile into an open space

        :return: None, adds tile to grid
        """

        loc = []  # Possible locations for new tiles
        nums = [2, 4]  # The values of tiles

        # Loop through grid and compile empty tiles
        for i, r in enumerate(self.grid):
            for j, c in enumerate(r):
                if c.val == 0:
                    loc.append((i,j))

        # Choose a location and add a random value
        coord = choice(loc)
        newVal = choices(nums, weights=[.9, .1], k=1)[0]
        self.grid[coord[0]][coord[1]].setVal(newVal)

        # Push the grid to stack for undo
        self.stack.push(deepcopy(self.grid))

    def checkWin(self):
        """
        Checks grid to see if there is a 2048 tile

        :return: True if there is a 2048 tile, else False
        """

        # Loop through all tiles and check for 2048
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if self.grid[r][c].val == 2048:
                    return True
        return False


    def undo(self):
        """
        Uses a stack to undo moves and reflects changes on the grid

        :return: None, grid itself is edited
        """
        if self.stack.top():
            self.grid = self.stack.pop()