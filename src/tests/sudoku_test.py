import unittest
from sudoku import Sudoku

class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.sudoku = Sudoku('....14....4....2....8.....5...4..89.4.68973...97..3...52.761..4...942.6.96..8.7.1')

    def test_number_added_to_empty_cell_succeeds(self):
        a = self.sudoku.move('A','5',1)
        self.assertFalse(a)

    def test_number_added_to_not_empty_cell_fails(self):
        a = self.sudoku.move('A','1',1)
        self.assertTrue(a)

# Code for reference
#
# def move(self, col, row, n):
#        x = 'ABCDEFGHI'.find(col)
#        y = int(row)-1
#        if self.initGrid[x+9*y] != '.':
#            return False
#        self.grid[(y,x)] = n
#        self.moves.append(copy.copy(self.grid))
#        return True
