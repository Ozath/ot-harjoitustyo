## Sudoku

Sudoku is a strategic puzzle game that is usually comprised of a 9x9-grid with numbers being pre-assigned to some squares. The goal is to fill in the empty squares with numbers ranging from one to nine. The constraint is that each unique number can only appear once in each row (horizontally), in each column (vertically), and in each of the nine blocks (3x3-grid). The relative difficulty of solving the sudoku is generally easier when more initial numbers are given.

<!-- ![Sudoku](./documents/images/sudoku.png) -->
<img src="./documents/images/sudoku.png" width="300" height="300" />

## Documentation

<!-- -Käyttöohje -->
- [Brainstorming](https://github.com/Ozath/ot-harjoitustyo/blob/master/documents/brainstorming.md)
 
- [Requirements](https://github.com/Ozath/ot-harjoitustyo/blob/master/documents/requirements.md)
<!-- -Arkkitehtuurikuvaus -->
<!-- -Testausdokumentti -->
- [Accounting of hours](https://github.com/Ozath/ot-harjoitustyo/blob/master/documents/accountingofhours.md)

## Installation

You will need to have python, pip, and poetry installed. Unless otherwise stated all commands are run from the root directory of the application. If you do not have Internet access in order to generate the sudoku puzzles you will need to install the dokusan package. This is because the program does not currently have a sudoku generator.

1. Set dependencies with the command:

```bash
poetry install
```
2. The **dokusan** package can be installed with the command:

```bash
pip install dokusan
```

## Console commands

### Running the program

The program can be run with the command:

```bash
poetry run invoke start
```

If poetry is not installed you can run the program from the **src** directory with the command:

```bash
python index.py
```

### Testing

Tests are run with the command:

```bash
poetry run invoke test
```

### Test coverage

A test coverage report can be generated with the command:

```bash
poetry run invoke coverage-report
```

A report is generated into the **htmlcov** directory.

### Pylint

The defined code inspections in the file [.pylintrc](./.pylintrc) can be executed with the command:

```bash
poetry run invoke lint
```
