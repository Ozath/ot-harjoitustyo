# Specification of requirements

### Purpose of the application

The application is a sudoku strategy game that the user can play.

### User interface

The user interface for the applciation will comprise of one GUI window that will contain the gameboard, window menu items, and likely some textual components. The below picture is a placeholder for the gameboard. The image on the left being the initial board, with the image on the right being a solved board.

<img src="./kuvat/sudoku.jpg" width="600" height="300" />

### Functionality

- Try to make the games UI entirely usable by a mouse.
- If required then add menu items that enable the user to interact with the application. 
  - The menu items should probably have hotkeys. 
- The sudoku grid will have initial values that can not be altered.
- The user can select a vacant cell and insert a number value in the range (1-9).
- The user can select an initial sudoku grid to solve.
  - Initially use pre-built grids with rated difficulty from external sources (saved locally).
  - The grids difficulty level should be selectable by the user.
- The user can save his current progress and resume the game at a later time.

### Further development ideas

- Expand functionality of the sudoku grids difficulty level.
  - Use a randomly generated grid by the application (AI).
  - Integrate to use live fetched grids from external sources.
- Auto-checker for game grid.
  - Entering an invalid number into a cell can alert the player immediately.
