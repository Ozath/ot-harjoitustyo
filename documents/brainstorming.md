## Brainstorming

This is as a temporary document for brainstoring that serves as a placeholder for other not-finalized documents during the development process. Any relevant content will
be refined into the appropriate project documents as the project progresses. Add ideas here and then process and add them to the documentation.

### The whiteboard of random ideas

- Could store the unsolved and solved sudoku grids locally. This would enable an easy implementation of a hint feature that randomly fills in a square.
- To ensure that a sudoku puzzle is unique based on the initial values requires to have a sudoku generator implemented. This would really be a seperate feature as it can take some time to generate a grid.

### MVP

Code a minimum viable product to demonstrate basic idea and simple functionality of the project. Implement a simple ASCII based sudoku game for console. Has the following functionality:

- Draw ASCII user interface and puzzle grid. :heavy_check_mark:
- Generate a sudoku puzzle grid from a local file. :heavy_check_mark:
- Check sudoku puzzle is valid. :heavy_check_mark: 
- Allow player to make moves and terminate if puzzle is solved. :heavy_check_mark:
- Allow player to reset grid, undo moves, and exit program. :heavy_check_mark:

Additional refinements and features:

- Allow player to save current puzzle progress.
  + Implement as automatic functionality on exit if puzzle not solved. Save to [sudoku.txt](https://github.com/Ozath/ot-harjoitustyo/blob/master/data/sudoku.txt) file in [data](https://github.com/Ozath/ot-harjoitustyo/tree/master/data).
- Instead of reading a prebuilt sudoku puzzle from a file, generate a random sudoku puzzle on game start (e.g. (N)ew option).
  + Add some difficulty metric to the puzzle. This can be based on the amount of initial numbers given.
  + If Internet connection available download a puzzle from [https://sugoku.herokuapp.com/](https://sugoku.herokuapp.com/). This also enables fetching a puzzle based on difficulty level.
- Prevent player from making a move that breaks the constraints of the puzzle.

### GUI implementation using pygame library

A general idea for the layout of the UI is as seen at [https://sugoku.herokuapp.com/](https://sugoku.herokuapp.com/). A few notable features to consider that are not implemented in this sudoku game are:

- Prevent player from making moves that are not valid.

- Possibly enable moves only by mouse (add buttons for numbers and undo).

### Sudoku (src/sudoku)

- Allow player to select difficulty of the sudoku puzzle.

  + Add additional index in [sudoku.txt](https://github.com/Ozath/ot-harjoitustyo/blob/master/data/sudoku.txt) file in [data](https://github.com/Ozath/ot-harjoitustyo/tree/master/data) to rank the difficulty of the grid (e.g. 1=easy, 2=medium, 3=hard). This is a feature for the GUI version.

### Sudoku Solver (src/solver)

Find a solution to the sudoku grid.
- Find one solution or all possible solution (given puzzle might not be unique).

### Sudoku Editor

- Currently can do this by edition [sudoku.txt](https://github.com/Ozath/ot-harjoitustyo/blob/master/data/sudoku.txt) file in [data](https://github.com/Ozath/ot-harjoitustyo/tree/master/data) directory.
  + The file has 81 characters, where '.' is an empty space and '1' to '9' are numbers in the grid.

- Add editor functionality so that user can design their own puzzle.

| Tasks           | Functionality | Time taken | Current Status | Finished | 
| ---             | ---           | :-:        | :-:            | :-:      |
| implement MVP | |  5 h  | done | :heavy_check_mark:
| - test | | |
| Object Cache   | | > 5 hours  | in progress | [x] item1<br/>[ ] item2
| Object Cache   | | > 5 hours  | in progress | <ul><li>- [x] item1</li><li>- [ ] item2</li></ul>
| Object Cache   | | > 5 hours  | in progress | <ul><li>[x] item1</li><li>[ ] item2</li></ul>
