from datetime import datetime
import random
import sys
import requests
from dokusan import generators

class Utility:
    """
    This is a utility module that supplies fileIO, JSON fetch, RNG seed, and generates
    a random premade sudoku puzzle string from external sources.
    """

    def __init__(self, fname, url):
        self.fname = fname
        self.url = url
        self.seed_value = datetime.now()

    def init_puzzle(self):
        """
        Initialize sudoku puzzle grid on start.
        """
        puzzle_string = self.read_file(self.fname)
        if len(puzzle_string) == 81:
            return puzzle_string
        return self.new_puzzle()

    def new_puzzle(self):
        """
        Generate a new sudoku puzzle grid.
        """
        self.seed_value = datetime.now()
        puzzle_string = self.get_puzzle_json(self.url)
        if len(puzzle_string) == 81:
            return puzzle_string
        return self.get_dokusan()

    def save_puzzle(self, puzzle, fname):
        """
        Save sudoku puzzle grid if not solved on exit.
        """
        return self.write_file(puzzle, fname)

    def get_dokusan(self):
        """
        The dokusan package is a sudoku generator and solver. Currently
        used to generate a puzzle if there is no Internet access. Requires
        the dokusan package to be installed. For more information see
        https://pypi.org/project/dokusan/ and documentation.
        """
        return str(generators.random_sudoku(avg_rank=self.get_rand_diff(2)))

    def get_puzzle_json(self, url):
        """
        Fetch the json for a premade sudoku puzzle from sugoku.herokuapp.com
        and convert it into a text string.
        """
        data = ""
        url = url + self.get_rand_diff(1)
        try:
            resp = requests.get(url)
        except requests.exceptions.RequestException:
            return data
        if resp.status_code == 200:
            data = resp.json()['board']
            data = [x for y in data for x in y]
            data = ''.join(map(str, data))
        return data

    def get_rand_diff(self, library_id):
        """
        Select a random difficulty for the sudoku puzzle.
        For the dokusan library the range of difficulty selected is 200-400.
        For sugoku.herokuapp.com the difficulty levels are easy, medium, and
        hard; these will be selected with weighting 6:3:1.
            :library_id: 1 - sugoku.herokuapp.com, 2 - dokusan
        """
        diff_string = "board?difficulty="
        random.seed(self.seed_value)
        diff_value = random.randint(200, 400)
        if library_id != 1:
            return diff_value
        return diff_string + ' '.join(random.choices(['easy','medium','hard'], weights=[60,30,10]))

    def write_file(self, puzzle, fname):
        """
        Write the current unsolved sudoku puzzle to the file
        'src/data/sudoku.txt' on exit.
        """
        status = False
        try:
            file = open(fname, 'w', encoding = 'utf-8')
#        except Exception:
        except ValueError:
            print(f'Unexpected error: writing {fname}')
            sys.exit(1)
        else:
            with file:
                file.write(puzzle)
                status = True
        return status

    def read_file(self, fname):
        """
        Read the current unsolved sudoku puzzle from the file
        'src/data/sudoku.txt' on start.
        """
        puzzle_string = ""
        try:
            file = open(fname, 'r', encoding = 'utf-8')
        except FileNotFoundError:
            pass
        else:
            with file:
                puzzle_string = file.readline(81)
        return puzzle_string
