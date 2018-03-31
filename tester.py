from grid import Grid
import os
import unittest

class TestStringMethods(unittest.TestCase):

    def testCreateGrid(self):
        true = [0, 2, 4, 2], [0, 2, 8, 16], [0, 0, 0, 0], [2048, 0, 0, 1]
        test = Grid(true)
        for r in range(4):
            for c in range(4):
                self.assertEqual(test.grid[r][c].val, true[r][c])

    def testArbitrarySize(self):
        true = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        test = Grid(true)
        for r in range(3):
            for c in range(3):
                self.assertEqual(test.grid[r][c].val, true[r][c])        

    def testSlide(self):
        test = Grid([[2, 2, 0, 0], [2, 0, 0, 0], [2, 4, 8, 16], [4, 4, 4, 4]])
        true = Grid([[0, 0, 0, 4], [0, 0, 0, 2], [2, 4, 8, 16], [0, 0, 8, 8]])
        test.slide('RIGHT')
        self.assertEqual(true, test)

        test = Grid([[2, 2, 0, 0], [2, 0, 0, 0], [2, 4, 8, 16], [4, 4, 4, 4]])
        true = Grid([[4, 0, 0, 0], [2, 0, 0, 0], [2, 4, 8, 16], [8, 8, 0, 0]])
        test.slide('LEFT')
        self.assertEqual(test, true)

        test = Grid([[2, 2, 0, 16], [2, 0, 0, 0], [2, 4, 8, 16], [4, 4, 4, 4]])
        true = Grid([[4, 2, 8, 32], [2, 8, 4, 4], [4, 0, 0,  0], [0, 0, 0, 0]])
        test.slide('UP')
        self.assertEqual(test, true)

        test = Grid([[2, 2, 0, 16], [2, 0, 0, 0], [2, 4, 8, 16], [4, 4, 4, 4]])
        true = Grid([[0, 0, 0, 0], [2, 0, 0, 0], [4, 2, 8, 32], [4, 8, 4, 4]])
        test.slide('DOWN')
        self.assertEqual(test, true)

        test = Grid([[4, 2, 2, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        true = Grid([[4, 4, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        test.slide('LEFT')
        self.assertEqual(true, test)

        test = Grid([[4, 2, 2, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        true = Grid([[0, 4, 4, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        test.slide('RIGHT')
        self.assertEqual(true, test)

if __name__ == '__main__':
    os.system('cls')
    unittest.main()