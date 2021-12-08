import unittest
from util.utility import Utility

class TestUtility(unittest.TestCase):

    def setUp(self):
        self.io = Utility('sudoku.txt', 'https://sugoku.herokuapp.com/')
        self.puzzle = '000014000040000200008000005000400890406897300097003000520761004000942060960080701'

    def test_init_values(self):
        self.assertEqual(self.io.fname, 'sudoku.txt')
        self.assertEqual(self.io.url, 'https://sugoku.herokuapp.com/')

    def test_init_puzzle_method_returns_proper_saved_string_length(self):        
        puzzle_string = self.io.init_puzzle()
        self.assertEqual(len(puzzle_string), 81)

    def test_init_puzzle_method_returns_proper_new_string_length(self):
        self.io.fname = ""
        puzzle_string = self.io.init_puzzle()
        self.assertEqual(len(puzzle_string), 81)

    def test_new_puzzle_method_returns_proper_json_string_length(self):
        puzzle_string = self.io.new_puzzle()
        self.assertEqual(len(puzzle_string), 81)

    def test_new_puzzle_method_returns_proper_dokusan_string_length(self):
        self.io.url = 'httpx://invalid/url'
        self.io.fname = ""
        puzzle_string = self.io.init_puzzle()
        self.assertEqual(len(puzzle_string), 81)

    def test_save_puzzle_method_returns_true_when_puzzle_is_saved(self):
        puzzle_string = self.io.save_puzzle(self.puzzle, self.io.fname)
        self.assertTrue(puzzle_string)

    def test_get_dokusan_returns_proper_string_length(self):
        puzzle_string = self.io.get_dokusan()
        self.assertEqual(len(puzzle_string), 81)

    def test_get_puzzle_json_returns_proper_string_length(self):
        puzzle_string = self.io.get_puzzle_json(self.io.url)
        self.assertEqual(len(puzzle_string), 81)

    def test_get_puzzle_json_returns_improper_string_length(self):
        puzzle_string = self.io.get_puzzle_json('http://httpbin.org/user-agent')
        self.assertNotEqual(len(puzzle_string), 81)
        puzzle_string = self.io.get_puzzle_json('http://httpbin.org/status/404')
        self.assertNotEqual(len(puzzle_string), 81)
        puzzle_string = self.io.get_puzzle_json('httpx://invalid/url')
        self.assertNotEqual(len(puzzle_string), 81)

    def test_get_rand_diff_returns_proper_value_for_library_id_1(self):
        self.io.seed_value = 1
        puzzle_string = self.io.get_rand_diff(1)
        self.assertEqual(puzzle_string, 'board?difficulty=easy')
        self.io.seed_value = 0
        puzzle_string = self.io.get_rand_diff(1)
        self.assertEqual(puzzle_string, 'board?difficulty=medium') 
        self.io.seed_value = 178
        puzzle_string = self.io.get_rand_diff(1)
        self.assertEqual(puzzle_string, 'board?difficulty=hard')
        
    def test_get_rand_diff_returns_proper_values_from_ranges_for_library_id_2(self):
        self.io.seed_value = 1
        diff_value = self.io.get_rand_diff(2)
        self.assertTrue(200 <= diff_value <= 320)
        self.io.seed_value = 19
        diff_value = self.io.get_rand_diff(2)
        self.assertTrue(321 <= diff_value <= 380)
        self.io.seed_value = 20
        diff_value = self.io.get_rand_diff(2)
        self.assertTrue(381 <= diff_value)

    def test_file_io_write_and_read_properly_output_values(self):
        status = self.io.write_file(self.puzzle, self.io.fname)
        self.assertTrue(status)
        puzzle_string = self.io.read_file(self.io.fname)
        self.assertEqual(len(puzzle_string), 81)

    def test_file_write_exceptions(self):
        with self.assertRaises(FileNotFoundError) as sys:
            self.io.write_file(self.puzzle, '<>:"/?* ')

    def test_file_read_exceptions(self):
        with self.assertRaises(IsADirectoryError) as sys:
            self.io.read_file('/')
