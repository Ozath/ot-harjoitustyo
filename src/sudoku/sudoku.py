# Code under refactoring and refinement. Should work. Sidelined due to working on
# GUI version.

import copy, sys

class Sudoku:

    def __init__(self, setup):
        self.initGrid = setup
        self.grid = {}
        self.resetGrid()
        self.moves = []

    def resetGrid(self):
        for row in range(1,9):
            for col in range(1,9):
                self.grid[(row,col)] = '0'
        x = 0
        row = 0
        while x < 81:
            for col in range(9):
                self.grid[(row,col)] = self.initGrid[x]
                x += 1
            row += 1

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
