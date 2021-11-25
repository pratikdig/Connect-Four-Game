import numpy as np
import pygame
import sys
import math


CREAM= (255,81,81) # red green blue (rgb)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7
#change the board size, only change the value of it 
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    # it is used to create a box table of 6 rows and 7 coloumns matrix
    return board

def drop_piece(board,row,col,piece):
    board[row][col] = piece
#for inserting option can takes place in this

def is_valid_location(board,col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board [r][col] == 0:
            return r
        #if the row is zero the values are empty

def print_board(board):
    print(np.flip(board,0))
    #flip the axies from 0, to get player inserted option is go to downwards 


def winning_move(board,piece):
    #Check Horizontal Location To Win This Match
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True


    #Check Vertical Location To Win This Match
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True


    # Check Positive Sloed Diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    #for down side to upside direction



    #Check Negative Sloed Diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    #for upside to down side direction


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, CREAM, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
             pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()




#r means rows
#c means columns
#the is develop by Pratik Digraskar
print("Connect Four...!!!")
board = create_board()
print_board(board)
game_over = False
turn = 0 #new variable

#Start the pygame program setup of size and width of game
pygame.init()
SQUARESIZE = 100
width= COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)
RADIUS = int(SQUARESIZE/2 -5)
screen=pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()



while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #for the quit optiton can work 
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            # this function can see the moment of cursor
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED,(posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW,(posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
        



                
        if event.type == pygame.MOUSEBUTTONDOWN:  # mouse button can work
           # print(event.pos) # position of the mouse in pixel


            #player one for User Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                
                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,1)
                    #we can change the player option by removing 1 to another
                    if winning_move(board,1):
                        print("PLAYER 1 WINS...!!! CONGRATULATION...!!!")
                        game_over = True



            #player Two for User Input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,2)
                    if winning_move(board,2):
                        print("PLAYER 2 WINS...!!! CONGRATULATION...!!!")
                        game_over = True

            print_board(board)
            draw_board(board)
            turn += 1
            #for incrementing the value by 1
            turn = turn % 2
            #for the reminder and changing the turns

            if game_over:
                pygame.time.wait(1)
        
