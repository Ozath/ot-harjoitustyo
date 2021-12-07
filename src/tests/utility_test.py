import unittest
from util.utility import Utility

class TestUtility(unittest.TestCase):

    def setUp(self):
        self.io = Utility('sudoku.txt', 'https://sugoku.herokuapp.com/')
        self.puzzle = '000014000040000200008000005000400890406897300097003000520761004000942060960080701'

    def test_init_values(self):
        self.assertEqual(self.io.fname, 'sudoku.txt')
        self.assertEqual(self.io.url, 'https://sugoku.herokuapp.com/')

    def test_init_method_returns_proper_string_length(self):
        s = self.io.init()
        self.assertEqual(len(s), 81)

    def test_new_method_returns_proper_string_length(self):
        s = self.io.new()
        self.assertEqual(len(s), 81)

    def test_getDokusan_returns_proper_string_length(self):
        s = self.io.getDokusan()
        self.assertEqual(len(s), 81)

    def test_getPuzzleJSON_returns_proper_string_length(self):
        s = self.io.getPuzzleJSON(self.io.url)
        self.assertEqual(len(s), 81)

#    def test_getPuzzleJSON_returns_improper_string_length(self):
#        s = self.io.getPuzzleJSON('https://www.abcd123')

    def test_getRandDiff_returns_proper_value_for_id_1(self):
        s = self.io.getRandDiff(1)
        self.assertIn(s, {'board?difficulty=easy', 'board?difficulty=medium', 'board?difficulty=hard'})
        
    def test_getRandDiff_returns_proper_value_for_id_2(self):
        n = self.io.getRandDiff(2)
        self.assertTrue(200 <= n <= 400)

    def test_fileIO_write_and_read_works_properly(self):
        status = self.io.writeFile(self.puzzle, self.io.fname)
        self.assertTrue(status)
        s = self.io.readFile(self.io.fname)
        self.assertEqual(len(s), 81)
