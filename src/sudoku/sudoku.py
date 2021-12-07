import copy, sys

class Sudoku:

    def __init__(self, setup):
        self.initGrid = setup
        self.grid = {}
        self.resetGrid()
        self.moves = []

    def resetGrid(self):
        for row in range(1,10):
            for col in range(1,10):
                self.grid[(row,col)] = '0'
        x = 0
        col = 0
        while x < 81:
            for row in range(9):
                self.grid[(row,col)] = self.initGrid[x]
                x += 1
            col += 1

    def move(self, col, row, n):
        x = 'ABCDEFGHI'.find(col)
        y = int(row)-1
        if self.initGrid[x+9*y] != '0':
            return False
        self.grid[(y,x)] = n
        self.moves.append(copy.copy(self.grid))
        return True

    def undo(self):
        if self.moves == []:
            return
        self.moves.pop()
        if self.moves == []:
            self.resetGrid()
        else:
            self.grid = copy.copy(self.moves[-1])

    def display(self):
        print()
        print('  A B C  D E F  G H I')
        for row in range(9):
          for col in range(9):
              if col == 0:
                  print(str(row + 1) + ' ', end='')
              print(self.grid[(row,col)] + ' ', end='')
              if col == 2 or col == 5:
                  print(' ', end='')
          print()
          if row == 2 or row == 5:
              print(' ')
    """
    def display_console(self):
        if self.checkSolved():
            print('Congratulations!\nPress (Y) to play another or any other key to exit.')
            c = input('>>').upper().strip()
            if c.startswith('Y'):
                sudoku = Sudoku(io.init())
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
                    self.display()
                    continue
                col, row = cell
                if col not in list('ABCDEFGHI'):
                    print('\nInvalid column.')
                    self.display()
                    continue
                if not row.isdecimal():
                    print('\nInvalid row.')
                    self.display()
                    continue
                if not n.isdecimal():
                    print('\nInvalid number.')
                    self.display()
                    continue
                else:
                    if not (1 <= int(n) <= 9):
                        print('\nInvalid number.')
                        self.display()
                        continue
                break
            print('\nInvalid command.')
            self.display()
        print()
        if c.startswith('N'):
            sudoku = Sudoku(io.init())
            continue
        if c.startswith('R'):
            sudoku.resetGrid()
            continue
        if c.startswith('U'):
            sudoku.undo()
            continue
        if c.startswith('Q'):
            sys.exit()
        if sudoku.move(col, row, n) == False:
           print('Not empty cell.')
    """

    def allNumbers(self, n):
        return sorted(n) == list('123456789')

    def checkSolved(self):
        for row in range(9):
            rowNum = []
            for x in range(9):
                num = self.grid[(x, row)]
                rowNum.append(num)
            if not self.allNumbers(rowNum):
                return False
        for col in range(9):
            colNum = []
            for x in range(9):
                num = self.grid[(col,x)]
                colNum.append(num)
            if not self.allNumbers(colNum):
                return False
        for row in (0,3,6):
            for col in (0,3,6):
                boxNums = []
                for x in range(3):
                    for y in range(3):
                        num = self.grid[(row+x,col+y)]
                        boxNum.append(n)
                if not self.allNumbers(boxNums):
                    return False
        return True
