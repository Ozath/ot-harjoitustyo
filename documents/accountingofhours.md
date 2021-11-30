# Accounting of Project hours

| date   | time | tasks/functionality |
| :-:    | :-:  | --- |
| 15.11. | 2    | pygame library familiarization |
| 16.11. | 2    | initial requirements specification |
| 19.11. | 3    | coding (GUI pygame) |
| 22.11. | 5    | coding (console version) for MVP |
| 27.11. | 4    | pygame library research |
| 29.11. | 1    | update requirements specification |
| 30.11. | 3    | coding MVP refinement |
|        | 2    | design GUI |
| total  | 22 h | | 

### Week 3

Coded an initial MVP sudoku ASCII version for command prompt to fullfil the requirements for given deadline. Will further test it to refine functionality and explore better design decisions and needs. Will update this document further in near future. Currently program will initiate and produce a sudoku game grid from a saved file. The player can solve the sudoku. If validly solved this ends the game. The player can also reset the grid at any time, backtrack their moves, or quit the program. The game was tested to work on melkki(at)cs.helsinki.fi.

### Week 4

Refined MVP slightly. Automatic sudoku puzzle generation from [https://sugoku.herokuapp.com/](https://sugoku.herokuapp.com/) website. If no Internet connection is available the application will instead generate a puzzle using the [dokusan](https://pypi.org/project/dokusan/) module. Option to generate new puzzle at any time. Fixed a minor bug. Still to do: refactoring code and writing unit tests. Implemented a basic GUI with pygame with no functionality other than launching a window and drawing game grid with a sudoku puzzle. Will refine documentation as the overall design becomes more apparent as to what features to implement. ASCII version was tested on melkki and windows. The GUI only on windows.

&nbsp;
## Progress tracker

| Tasks           | Functionality | Current Status | Finished | 
| ---             | ---           | :-:            | :-:      |
| implement MVP   |               | done           | :heavy_check_mark:
| refine MVP      | sudoku generator              | in progress    | |
| | save puzzle state on exit | in progress | |
| start GUI       |               | in progress    | |
