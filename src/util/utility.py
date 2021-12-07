import requests, sys
from dokusan import generators
from random import randint
from random import seed

class Utility:
    """
    This is a utility module that supplies fileIO, JSON fetch, RNG seed, and generates
    a random sudoku puzzle string.
    """

    def __init__(self, fname, url):
        self.fname = fname
        self.url = url

    def init(self):
        """
        Initialize sudoku puzzle grid on start.
        """
        s = self.readFile(self.fname)
        if (len(s) == 81):
            return s
        return self.new()

    def new(self):
        """
        Generate a new sudoku puzzle grid.
        """
        s = self.getPuzzleJSON(self.url)
        if (len(s) == 81):
            return s
        return self.getDokusan()

    def save(self, puzzle, fname):
        """
        Save sudoku puzzle grid if not solved on exit.
        """
        self.writeFile(puzzle, fname)

    def getDokusan(self):
        """
        The dokusan package is a sudoku generator and solver. Currently
        used to generate a puzzle if there is no Internet access. Requires
        the dokusan package to be installed. For more information see
        https://pypi.org/project/dokusan/ and documentation.
        To install type: pip install dokusan
        """
        return str(generators.random_sudoku(avg_rank=self.getRandDiff(2)))

    def getPuzzleJSON(self, url):
        """
        Fetch the json for a premade sudoku puzzle from sugoku.herokuapp.com 
        and convert it into a text string.
        """
        data = ""
        url = url + self.getRandDiff(1)
        try:
            resp = requests.get(url)
        except requests.exceptions.RequestException as e:
            pass
        if resp.status_code == 200:
            data = resp.json()['board']
            data = [x for y in data for x in y]
            data = ''.join(map(str, data))
        return data

    def getRandDiff(self, id):
        """
        Select a random difficulty for the sudoku puzzle.
        For the dokusan library the range of difficulty is 150-350.
        For sugoku.herokuapp.com the difficulty levels are easy, medium, and 
        hard; these will be selected with weighting 6:3:1.
            :id: 1 - sugoku.herokuapp.com, 2 - dokusan
        """
        s = "board?difficulty="
        seed()
        value = randint(200, 400)
        if id != 1:
            return value
        if value < 322:
            s = s + "easy"
        elif value > 380:
            s = s + "hard"
        else:
            s = s + "medium"
        return s

    def writeFile(self, puzzle, fname):
        """
        Write the current unsolved sudoku puzzle to the file 
        'src/data/sudoku.txt' on exit.
        """
        status = False
        try:
            f = open(fname, 'w', encoding = 'utf-8')
        except Exception as err:
            print(f'Unexpected error: writing {fname}')
            sys.exit(1)
        else:
            with f:
                f.write(puzzle)
                status = True
        return status

    def readFile(self, fname):
        """
        Read the current unsolved sudoku puzzle from the file 
        'src/data/sudoku.txt' on start.
        """
        s = ""
        try:
            f = open(fname, 'r', encoding = 'utf-8')
        except FileNotFoundError:
            pass
        except OSError:
            print(f'OS error: opening {fname}')
            sys.exit(1)
        except Exception as err:
            print(f"Unexpected error: opening {fname}")
            sys.exit(1)
        else:
            with f:
                s = f.readline(81)
        finally:
            return s

