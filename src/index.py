# Refactoring in process.

import sys
from sudoku.sudoku import Sudoku
from util.utility import Utility

fname = '../data/sudoku.txt'
url = 'https://sugoku.herokuapp.com/'

def main():
    io = Utility(fname, url)
    sudoku = Sudoku(io.init_puzzle())
    while True:
        if sudoku.checkSolved():
            print('Congratulations!\nPress (Y) to play another or any other key to exit.')
            c = input('>>').upper().strip()
            if c.startswith('N'):
                sudoku = Sudoku(io.new_puzzle())
                sudoku.display()
            else:
                sys.exit(1)
        while True:
            sudoku.display()
            print()
            print('Enter move (e.g. A1 2), (N)ew, (R)eset, (U)ndo, or (Q)uit.')
            c = input('>>').upper().strip()
            if len(c) > 0 and c[0] in ('N', 'R', 'U', 'Q'):
                break
            if len(c.split()) == 2:
                cell, n = c.split()
                if len(cell) != 2:
                    print('Invalid cell.')
                    continue
                col, row = cell
                if col not in list('ABCDEFGHI'):
                    print('\nInvalid column.')
                    continue
                if not row.isdecimal():
                    print('\nInvalid row.')
                    continue
                if not n.isdecimal():
                    print('\nInvalid number.')
                    continue
                else:
                    if not (1 <= int(n) <= 9):
                        print('\nInvalid number.')
                        continue
                break
            print('\nInvalid command.')
        print()
        if c.startswith('N'):
            sudoku = Sudoku(io.new_puzzle())
            continue
        if c.startswith('R'):
            sudoku.resetGrid()
            continue
        if c.startswith('U'):
            sudoku.undo()
            continue
        if c.startswith('Q'):
            io.save_puzzle(sudoku.initGrid, fname)
            sys.exit()
        if sudoku.move(col, row, n) == False:
           print('Not initial empty cell.')

if __name__ == "__main__":
    main()
