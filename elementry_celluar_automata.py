from math import *
import pygame
import sys
import time
import random
 
RULE = 182  # limit = 2^8  --> 286
# try 90, 60 , 110 , 22 , 18 ,50 ,161 ,

#https://mathworld.wolfram.com/ElementaryCellularAutomaton.html

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 900
CELLS_IN_ROW = 200


screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption(f"RULE : {RULE}")

clock = pygame.time.Clock()
screen.fill("black")


def drawRow(row,y):
    # y = SCREEN_HEIGHT - y
    cell_dim = floor(SCREEN_WIDTH /CELLS_IN_ROW/2)
    for i in range(CELLS_IN_ROW):
        x = floor(i / CELLS_IN_ROW * SCREEN_WIDTH) 
        if row[i] == 1:
            pygame.draw.rect(screen,"white",pygame.Rect(x,y,cell_dim,cell_dim))
        # time.sleep(0.0001)
    pygame.display.flip()

def decToBin(dec):
    bin = []
    for i in range(8):
        bin.append(dec % 2)
        dec //= 2
    return bin

def load_next_gen(curr_row,gen_hash):
    next_row = []
    for i in range(CELLS_IN_ROW):
        curr_state = 0
        if i != 0 :
            curr_state += curr_row[i-1] * 100
        curr_state +=  curr_row[i] * 10
        if i != CELLS_IN_ROW - 1 :
            curr_state += curr_row[i+1]

        next_row.append(gen_hash[curr_state])          
    return next_row

def main():
    curr_row = [0 for x in range(CELLS_IN_ROW)]
    curr_row[floor(CELLS_IN_ROW/2)] = 1
    pygame.init()
    cell_dim = floor(SCREEN_WIDTH / CELLS_IN_ROW ) - 1 
    bin = decToBin(RULE)
    gen_hash = {
        0: bin[0],
        1: bin[1],
        10: bin[2],
        11: bin[3],
        100: bin[4],
        101: bin[5],
        110: bin[6],
        111: bin[7]
    }
    y = 10
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:      #exit when 'x' icon is pressed
                return
        while( y < SCREEN_HEIGHT):
            y += cell_dim
            drawRow(curr_row,y)
            pygame.display.flip()
            curr_row = load_next_gen(curr_row,gen_hash)
        # time.sleep(1)
        # running = False


main()
pygame.quit()
sys.exit()
