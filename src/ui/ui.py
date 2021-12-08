# Just a demo for pygame window for sudoku game for the given puzzle grid below. 
# Under development.

import pygame

grid = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]

def move(win, position):
    """ I do nothing yet. Implement me.
    """
        
def main():   
    """ Create a pygame window with sudoku board. Has no functionality. Closes
        on mouse click.
    """
    pygame.init()
    win = pygame.display.set_mode((550, 550))
    pygame.display.set_caption("Sudoku")
    win.fill((255,255,255))
    font = pygame.font.SysFont("Segoe UI", 35)    
    for x in range(0,10):
        if(x % 3 == 0):
            pygame.draw.line(win, (0,0,0), (50+50*x,50), (50+50*x,500), 4)
            pygame.draw.line(win, (0,0,0), (50,50+50*x), (500,50+50*x), 4)
        pygame.draw.line(win, (0,0,0), (50+50*x,50), (50+50*x,500), 2)
        pygame.draw.line(win, (0,0,0), (50,50+50*x), (500,50+50*x), 2)
    pygame.display.update()   
    for x in range(0, len(grid[0])):
        for y in range(0, len(grid[0])):
            if (0 < grid[x][y] < 10):
                value = font.render(str(grid[x][y]), True, (1,1,1))
                win.blit(value, ((y+1)*50+15,(x+1)*50))
    pygame.display.update()     
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pygame.quit()
                return
   
if __name__=="__main__":
    main()
