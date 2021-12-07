import unittest
from sudoku.sudoku import Sudoku

class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.sudoku = Sudoku('000014000040000200008000005000400890406897300097003000520761004000942060960080701')

    def test_number_added_to_empty_cell_succeeds(self):
        move = self.sudoku.move('A','5',1)
        self.assertFalse(move)

    def test_number_added_to_not_empty_cell_fails(self):
        move = self.sudoku.move('A','1',1)
        self.assertTrue(move)

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
