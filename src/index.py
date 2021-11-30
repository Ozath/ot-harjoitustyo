import sys
from sudoku import Sudoku

def main():
    f = open('../data/sudoku.txt', 'r')
    grid = Sudoku(f.read(81))
    while True:
        grid.display()
        if grid.checkSolved():
            print('Solved!')
            sys.exit()
        while True:
            print()
            print('Enter move (e.g. A1 2), (R)eset, (U)ndo, or (Q)uit.')
            c = input('>').upper().strip()
            if len(c) > 0 and c[0] in ('R', 'U', 'Q'):
                break
            if len(c.split()) == 2:
                cell, n = c.split()
                if len(cell) != 2:
                    continue
                col, row = cell
                if col not in list('ABCDEFGHI'):
                    grid.display()
                    print('\nInvalid column.')
                    continue
                if not row.isdecimal() or not (1 <= int(row) <=9):
                    grid.display()
                    print('\nInvalid row.')
                    continue
                if not (1 <= int(n) <= 9):
                    grid.display()
                    print('\nInvalid number.')
                    continue
                break
        print()
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
