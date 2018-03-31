from random import randint, choice
from tile import Tile

class Grid:
    grid = [[]]
    score = 0

    def __init__(self, arrays=None):
        self.score = 0
        # Creates a random grid with 2 random tiles
        if not arrays:
            print('Creating random grid')
            self.grid = [[Tile(0) for x in range(4)] for y in range(4)]
            self.addTile()
            self.addTile()

        # Create a predetermined grid
        if arrays: 
            self.grid = []
            for r in arrays:
                row = []
                for num in r:
                    row.append(Tile(num))
                self.grid.append(row)

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
        return ret

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        for r in range(4):
            for c in range(4):
                if self.grid[r][c] != other.grid[r][c]:
                    return False
        return True

    def checkGameOver(self):
        """
        Returns True if there are no more moves to make, else False
        """
        pass

    def slide(self, direction):
        """
        Slides all the tiles in the direction of the key press
        :return: None
        """
        if direction == 'UP':
            for c in range(4):
                shifted = []
                merged = False
                for r in range(4):
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

                # Copy over new column
                for i in range(4 - len(shifted)):
                    shifted.append(Tile(0))
                for i, new in enumerate(shifted):
                    self.grid[i][c] = new

        elif direction == 'RIGHT':
            for r in range(4):
                shifted = []
                merged = False
                for c in range(3, -1, -1):
                    currTile = self.grid[r][c]
                    if currTile.val != 0:
                        if len(shifted) > 0:
                            # Merge similar tiles
                            if shifted[-1].val == currTile.val and not merged:
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

                # Copy over new row
                for i in range(4 - len(shifted)):
                    shifted.append(Tile(0))
                self.grid[r] = list(reversed(shifted))

        elif direction == 'DOWN':
            for c in range(4):
                shifted = []
                merged = False
                for r in range(3, -1, -1):
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
                            merged = False
                            shifted.append(currTile)

                # Copy over new column
                for i in range(4 - len(shifted)):
                    shifted.append(Tile(0))
                for i, new in enumerate(reversed(shifted)):
                    self.grid[i][c] = new


        elif direction == 'LEFT':
            for r in range(4):
                shifted = []
                merged = False
                for c in range(4):
                    currTile = self.grid[r][c]
                    if currTile.val != 0:
                        if len(shifted) > 0:
                            # Merge similar tiles
                            if shifted[-1].val == currTile.val and not merged:
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

                # Copy over new row
                for i in range(4 - len(shifted), -1, -1):
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
        pass