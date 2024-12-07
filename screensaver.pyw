import pygame
import numpy as np
import time
import random

#windpos
x = 1200
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.display.set_caption("Conway's Game of Life")


COLOR_BG = (10, 10, 10)
COLOR_GRID = (10, 10, 10)
COLOR_DIE_NEXT = (10, 10, 10)
COLOR_ALIVE_NEXT = (255, 255, 255)
SCREEN_X = 6
SCREEN_Y = 6
SCREEN_SIZE = 5

def update(screen, cells, size, with_progress=False):

    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1: row+2, col-1: col+2]) - cells[row, col]
        color = COLOR_BG if cells [row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2<= alive<= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X*SCREEN_SIZE*10, SCREEN_Y*SCREEN_SIZE*10))

    cells = np.zeros((SCREEN_X*SCREEN_SIZE, SCREEN_X*SCREEN_SIZE))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update
                if event.key == pygame.K_RETURN:
                    running = False
                    cells = np.zeros((SCREEN_X*SCREEN_SIZE, SCREEN_Y*SCREEN_SIZE))
                    update(screen, cells, 10)
                    pygame.display.update()
                if event.key == pygame.K_r: 
                    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
                    #running = False
                    for row, col in np.ndindex(cells.shape):
                        #rng = np.random.default_rng(5)
                        #rng.random()
                        #print (rng)
                        rng = random.randint(0, 5)
                        if rng == 5:
                            running = False
                            cells[row, col] = 1
                            update(screen, cells, 10)
                            running = True
                            pygame.display.update() 
                if event.key == pygame.K_d:
                    cells = np.zeros((cells.shape[0], cells.shape[1]))
                    row = (SCREEN_Y*SCREEN_SIZE)/2
                    col = (SCREEN_X*SCREEN_SIZE)/2
                    row = int(row)
                    col = int(col)
                    (cells[row-1: row+1, col]) = 1
                    row = (SCREEN_Y*SCREEN_SIZE)/2 +1
                    col = (SCREEN_X*SCREEN_SIZE)/2 +1
                    row = int(row)
                    col = int(col)
                    (cells[row-1: row+1, col]) = 1
                    row = (SCREEN_Y*SCREEN_SIZE)/2 +2
                    col = (SCREEN_X*SCREEN_SIZE)/2 +2
                    row = int(row)
                    col = int(col)
                    (cells[row-1: row+1, col]) = 1
                    row = (SCREEN_Y*SCREEN_SIZE)/2
                    col = (SCREEN_X*SCREEN_SIZE)/2 -1
                    row = int(row)
                    col = int(col)
                    (cells[row-1, col]) = 1

                    update(screen, cells, SCREEN_SIZE)
                    running = True
                    pygame.display.update()

                if event.key == pygame.K_t:
                    cells = np.zeros((cells.shape[0], cells.shape[1]))

                    row = (SCREEN_Y*SCREEN_SIZE)/2
                    col = (SCREEN_X*SCREEN_SIZE)/2
                    row = int(row)
                    col = int(col)
                    (cells[row-1: row+2, col]) = 1
                    row = (SCREEN_Y*SCREEN_SIZE)/2 -3
                    col = (SCREEN_X*SCREEN_SIZE)/2
                    row = int(row)
                    col = int(col)
                    (cells[row, col-1: col+2]) = 1

                    update(screen, cells, SCREEN_SIZE)
                    running = True
                    pygame.display.update()

                if event.key == pygame.K_p:
                    cells = np.zeros((cells.shape[0], cells.shape[1]))
                    
                    col = (SCREEN_X*SCREEN_SIZE)/2
                    row = (SCREEN_Y*SCREEN_SIZE)/2
                    row = int(row)
                    col = int(col)
                    (cells[row-1: row+2, col-1: col+2]) = 1
                    row = (SCREEN_Y*SCREEN_SIZE)/2 +1
                    col =  (SCREEN_X*SCREEN_SIZE)/2 +1
                    row = int(row)
                    col = int(col)
                    (cells[row-1: row+2, col-1]) = 0

                    update(screen, cells, SCREEN_SIZE)
                    running = True
                    pygame.display.update()

                if event.key == pygame.K_h:
                    cells = np.zeros((cells.shape[0], cells.shape[1]))
                    
                    row = (SCREEN_Y*SCREEN_SIZE)/2
                    col = (SCREEN_X*SCREEN_SIZE)/2
                    row = int(row)
                    col = int(col)
                    (cells[row-1: row+2, col-1: col+2]) = 1
                    row = (SCREEN_Y*SCREEN_SIZE)/2 +2
                    col = (SCREEN_X*SCREEN_SIZE)/2 +2
                    row = int(row)
                    col = int(col)
                    (cells[row-1, col-1]) = 0
                    row = (SCREEN_Y*SCREEN_SIZE)/2 +1
                    col = (SCREEN_X*SCREEN_SIZE)/2 +2
                    row = int(row)
                    col = int(col)
                    (cells[row-1, col-1]) = 0
                    row = (SCREEN_Y*SCREEN_SIZE)/2 +2
                    col = (SCREEN_X*SCREEN_SIZE)/2
                    row = int(row)
                    col = int(col)
                    (cells[row-1, col-1]) = 0
                    row = (SCREEN_Y*SCREEN_SIZE)/2
                    col = (SCREEN_X*SCREEN_SIZE)/2
                    row = int(row)
                    col = int(col)
                    (cells[row-1, col-1]) = 0

                    update(screen, cells, SCREEN_SIZE)
                    running = True
                    pygame.display.update()
                if event.key == pygame.K_m:
                    cells = np.zeros((6*SCREEN_SIZE, 8*SCREEN_SIZE))
                    rng = random.randint(0, 3)

                    #diagon
                    if rng == 3:
                        row = 15
                        col = 15
                        (cells[row-1: row+1, col]) = 1
                        row = 16
                        col = 16
                        (cells[row-1: row+1, col]) = 1
                        row = 17
                        col = 17
                        (cells[row-1: row+1, col]) = 1
                        row = 15
                        col = 14
                        (cells[row-1, col]) = 1

                    #thunderbird
                    if rng == 2:
                        row = 15
                        col = 15
                        (cells[row-1: row+2, col]) = 1
                        row = 12
                        col = 15
                        (cells[row, col-1: col+2]) = 1

                    #pi
                    if rng == 1:
                        row = 15
                        col = 15
                        (cells[row-1: row+2, col-1: col+2]) = 1
                        row = 16
                        col = 16
                        (cells[row-1: row+2, col-1]) = 0
                    #hepton
                    if rng == 0:
                        row = 15
                        col = 15
                        (cells[row-1: row+2, col-1: col+2]) = 1
                        row = 17
                        col = 17
                        (cells[row-1, col-1]) = 0
                        row = 16
                        col = 17
                        (cells[row-1, col-1]) = 0
                        row = 17
                        col = 15
                        (cells[row-1, col-1]) = 0
                        row = 15
                        col = 15
                        (cells[row-1, col-1]) = 0
                    update(screen, cells, 10)
                    running = True
                    pygame.display.update()      
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()
        
        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

            time.sleep(0.1)

if __name__ == '__main__':
    main()