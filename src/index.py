import sys
from sudoku.sudoku import Sudoku
from util.utility import Utility

fname = '../data/sudoku.txt'
url = 'https://sugoku.herokuapp.com/'

def main():
    io = Utility(fname, url)
    sudoku = Sudoku(io.init())
    while True:
        sudoku.display()
        if sudoku.checkSolved():
            print('Congratulations!\nPress (Y) to play another or any other key to exit.')
            c = input('>>').upper().strip()
            if c.startswith('N'):
                sudoku = Sudoku(io.new())
                sudoku.display()
            else:
                sys.exit()
        while True:
            print()
            print('Enter move (e.g. A1 2), (N)ew, (R)eset, (U)ndo, or (Q)uit.')
            c = input('>>').upper().strip()
            if len(c) > 0 and c[0] in ('N', 'R', 'U', 'Q'):
                break
            if len(c.split()) == 2:
                cell, n = c.split()
                if len(cell) != 2:
                    print('Invalid cell.')
                    sudoku.display()
                    continue
                col, row = cell
                if col not in list('ABCDEFGHI'):
                    print('\nInvalid column.')
                    sudoku.display()
                    continue
                if not row.isdecimal():
                    print('\nInvalid row.')
                    sudoku.display()
                    continue
                if not n.isdecimal():
                    print('\nInvalid number.')
                    sudoku.display()
                    continue
                else:
                    if not (1 <= int(n) <= 9):
                        print('\nInvalid number.')
                        sudoku.display()
                        continue
                break
            print('\nInvalid command.')
            sudoku.display()
        print()
        if c.startswith('N'):
            sudoku = Sudoku(io.new())
            continue
        if c.startswith('R'):
            sudoku.resetGrid()
            continue
        if c.startswith('U'):
            sudoku.undo()
            continue
        if c.startswith('Q'):
            io.save(sudoku.initGrid, fname)
            sys.exit()
        if sudoku.move(col, row, n) == False:
           print('Not empty cell.')

if __name__ == "__main__":
    main()
