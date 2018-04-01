class Tile:
    val = 0

    def __init__(self, n=0):
        self.val = n

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__() 

    def __eq__(self, other):
        return self.val == other.val

    def setVal(self, n):
        """
        Changes the value of the tile
        :return: None
        """
        self.val = n