import pygame as py
import numpy as np
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255, 255, 255)
def create_board():
	board = np.zeros((6,7))
	return board
board = create_board()
def print_board(board):
    for i in range(6):
        print(board[i])
    print("******************************")
def draw_board(board):
	for c in range(7):
		for r in range(6):
			py.draw.rect(screen, BLUE, (c*100, r*100+100, 100, 100))
			py.draw.circle(screen, WHITE, (int(c*100+50), int(r*100+150)), 45)
def update(col,board,top_position,turn):
    if(top_position[col] == 50):
        return turn,board
    row=top_position[col] // 100 -1
    if(turn %2==0):
        py.draw.circle(screen, RED, (int(col * 100 + 50), top_position[col]), 45)
        board[row][col]=1
    else:
        print("row", int(col * 100 + 50) // 700)
        print("column", col)
        py.draw.circle(screen, YELLOW, (int(col * 100 + 50), top_position[col]), 45)
        board[row][col] = 2
    top_position[col] = top_position[col] - 100
    turn = turn + 1
    return turn,board
def check_full(board):
    if(np.any(board == 0)):
        return
    else:check_wining(board)
def check_wining(board):
    red=0
    yellow=0
    for i in range(len(board)):
        row=board[i]
        for k in range(4):
            if(row[k]== row[k+1] == row[k+2] == row[k+3]):
                if(row[k]==1):
                    red=red+1
                elif(row[k]==2):
                    yellow=yellow+1
    transpose=np.transpose(board)
    for i in range(len(transpose)):
        column=transpose[i]
        for k in range(3):
            if(column[k]== column[k+1] == column[k+2] == column[k+3]):
                if(column[k]==1):
                    red=red+1
                elif(column[k]==2):
                    yellow=yellow+1
    for i in range(3):
        for j in range(4):
            if (board[i][j] == board[i + 1][j+1] == board[i + 2][j+2] == board[i + 3][j+3]):
                if (board[i][j] == 1):
                    red = red + 1
                elif (board[i][j] == 2):
                    yellow = yellow + 1
    for i in range(3, 6):
        for j in range(4):
            if (board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2] == board[i - 3][j + 3]):
                if (board[i][j] == 1):
                    red = red + 1
                elif (board[i][j] == 2):
                    yellow = yellow + 1
    print("win red",red)
    print("win yellow",yellow)


game_over = False
turn = 0
py.init()
screen = py.display.set_mode((700, 700))
screen.fill(WHITE)
draw_board(board)
py.display.set_caption("Connect Four")
running = True
top_position=[650]*7
font = py.font.Font('freesansbold.ttf', 32)
text1 = font.render('Red Turn', True,RED,WHITE)
text1_rect = text1.get_rect(center=(700 // 2, 25))
text2 = font.render('Yellow Turn', True,YELLOW,WHITE)
text2_rect = text2.get_rect(center=(700 // 2, 25))
text1_rect.center = (700 // 2, 25 )
text2_rect.center = (700 // 2, 25 )
screen.blit(text1, text1_rect)
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            col = posx // 100
            turn,board=update(col,board,top_position,turn)
            print_board(board)
            if (turn % 2 == 0):
                py.draw.rect(screen, WHITE, text2_rect)
                screen.blit(text1, text1_rect)
            else:
                screen.blit(text2, text2_rect)
            check_full(board)
    py.display.update()
