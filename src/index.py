import requests,sys
from dokusan import generators
from sudoku.sudoku import Sudoku

fname = '../data/sudoku.txt'

# can add RNG to determine the difficulty level to be fetched
url = "https://sugoku.herokuapp.com/board?difficulty=easy"

def sudokuGenerator():
    """
    The dokusan package is a sudoku generator and solver. Currently
    used to generate a puzzle if there is no Internet access. Requires
    the dokusan package to be installed. For more information see
    https://pypi.org/project/dokusan/ and documentation.
    To install do command: pip install dokusan
    """
    return str(generators.random_sudoku(avg_rank=300))

def getJSON(url):
    """
    Fetch the json for a sudoku puzzle from sugoku.herokuapp.com and
    convert it into a text string.
    """
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f'Error occurred. Status code {resp.status_code}')
        return 0
    data = resp.json()['board']
    data = [x for y in data for x in y]
    data=''.join(map(str,data))
    return data

def fileReader(fname):
    try:
        f = open('fname', 'r')
    except IOError:
        print('IOError')
    else:
        with f:
            f1 = f.readline()
            if len(f1) != 81:
                print('File is not valid.')
                sys.exit()
            return f1

def fileWriter(fname, data):
    try:
        with open(fname, "w") as f:
            f.write(data)
    except IOError:
        print('IOError.')
    
def initialize(url):
    f = getJSON(url)
    if f == 0:
        f = sudokuGenerator()
    return f

def main():
    g = initialize(url)
    grid = Sudoku(g)
    while True:
        grid.display()
        if grid.checkSolved():
            print('Solved!')
            sys.exit()
        while True:
            print()
            print('Enter move (e.g. A1 2), (N)ew, (R)eset, (U)ndo, or (Q)uit.')
            c = input('>').upper().strip()
            if len(c) > 0 and c[0] in ('N', 'R', 'U', 'Q'):
                break
            if len(c.split()) == 2:
                cell, n = c.split()
                if len(cell) != 2:
                    print('Invalid cell.')
                    grid.display()
                    continue
                col, row = cell
                if col not in list('ABCDEFGHI'):
                    print('\nInvalid column.')
                    grid.display()
                    continue
                if not row.isdecimal():
                    print('\nInvalid row.')
                    grid.display()
                    continue
                if not n.isdecimal():
                    print('\nInvalid number.')
                    grid.display()
                    continue
                else:
                    if not (1 <= int(n) <= 9):
                        print('\nInvalid number.')
                        grid.display()
                        continue
                break
            grid.display()
            print('\nInvalid command.')
        print()
        if c.startswith('N'):
            g = initialize(url)
            grid = Sudoku(g)
            continue
        if c.startswith('R'):
            grid.resetGrid()
            continue
        if c.startswith('U'):
            grid.undo()
            continue
        if c.startswith('Q'):
            sys.exit()
        if grid.move(col, row, n) == False:
           print('Not empty cell.')

if __name__ == "__main__":
    main()
