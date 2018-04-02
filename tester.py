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

    def testGameOver(self):
        test = Grid([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        self.assertTrue(test.checkGameOver())

    def testWin(self):
        test = Grid([[2048, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertTrue(test.checkWin())

        test = Grid([[1024, 1024, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        test.slide('LEFT')
        self.assertTrue(test.checkWin())

    def testDimensions(self):
        test = Grid([[2, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0]])
        self.assertEqual(2, test.num_rows)
        self.assertEqual(6, test.num_cols)

        true = Grid([[0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 4]])
        test.slide('RIGHT')
        self.assertEqual(true, test)

    # def testBadParams(self):
    #     self.failUnlessRaises(AssertionError, Grid([1, 2, 3, 4]))

    def testUndo(self):
        test = Grid([[2, 2, 0, 0], [2, 0, 0, 0], [2, 4, 8, 16], [4, 4, 4, 4]])
        true = Grid([[2, 2, 0, 0], [2, 0, 0, 0], [2, 4, 8, 16], [4, 4, 4, 4]])
        test.slide('RIGHT')
        test.undo()
        self.assertEqual(test, true)

if __name__ == '__main__':
    os.system('cls')
    unittest.main()