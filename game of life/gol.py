import pygame
import sys
import random
import time

resolution = 3/5

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = int(resolution * SCREEN_HEIGHT)
COLS = 50
ROWS = int(resolution * COLS)
CELL_DIM = SCREEN_WIDTH // ROWS



front_grid = [[0] * ROWS for _ in range(COLS)]
back_grid = [[0] * ROWS for _ in range(COLS)]

pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT , SCREEN_WIDTH ))
pygame.display.set_caption("Conway's Game of Life")


clock = pygame.time.Clock()

def drawGrid():
    screen.fill("black")
    for col in range(COLS):
        for row in range(ROWS):
            if front_grid[col][row] == 1:
                pygame.draw.rect(screen, "white", pygame.Rect(col * CELL_DIM, row * CELL_DIM, CELL_DIM * 0.7, CELL_DIM * 0.7))
    pygame.display.flip()

def isAlive(col, row):
    nbors = 0
    curr = front_grid[col][row]
    for i in range(col - 1, col + 2):
        for j in range(row - 1, row + 2):
        # Skip counting the current cell itself
            if i != col or j != row:
                nbors += front_grid[i % COLS][j % ROWS]
    if curr == 0 and nbors == 3:
        return 1
    elif curr == 1 and (nbors == 2 or nbors == 3):
        return 1
    elif curr == 1 and (nbors < 2 or nbors > 3):
        return 0
    else:
        return curr



def load_next_gen():
    for col in range(COLS):
        for row in range(ROWS):
            back_grid[col][row] = isAlive(col, row)
    for col in range(COLS):
        for row in range(ROWS):
            front_grid[col][row] = back_grid[col][row] 


def Gen():
    for col in range(COLS):
        for row in range(ROWS):
            front_grid[col][row] = random.choice([0,1])
    # front_grid[5][6] = 1
    # front_grid[6][7] = 1
    # front_grid[7][5] = 1
    # front_grid[7][6] = 1
    # front_grid[7][7] = 1

def main():
    Gen()
    running = True
    paused = False
    while running:
        clock.tick(10)  # Adjust the speed of the simulation by changing the tick rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = bool(1 - paused)
                    break
        if (not paused):
            drawGrid()
            load_next_gen()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
 