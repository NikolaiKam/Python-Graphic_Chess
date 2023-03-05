import pygame

from Functions.matrix_def import *
from Functions.objects import *
from Functions.basic_func import *

def find_move(figgType,screen,x_moves,y_moves):
    
    if figgType=='pawn':

        Pawn("W",x_moves,y_moves).show_moves(screen)

    if figgType=='bishop':
        
        Bishop("W",x_moves,y_moves).show_moves(screen)

    if figgType=='knight':
        
        Knight("W",x_moves,y_moves).show_moves(screen)

    if figgType=='rook':
        
        Rook("W",x_moves,y_moves).show_moves(screen)

    if figgType=='queen':
        
        Queen("W",x_moves,y_moves).show_moves(screen)

    if figgType=='king':
        
        King("W",x_moves,y_moves).show_moves(screen)

#Initialize pygame

pygame.init()

#The screen 

screen = pygame.display.set_mode((800,800))

#Background

background = pygame.image.load('chess_board.jpg')

#Pawns B&W

pawn_black = pygame.image.load('pawn_black.png')
pawn_white = pygame.image.load('pawn_white.png')

#Rooks B&W

rook_black = pygame.image.load('rook_black.png')
rook_white = pygame.image.load('rook_white.png')

#Knights B&W

knight_black = pygame.image.load('knight_black.png')
knight_white = pygame.image.load('knight_white.png')

#Bishops B&W

bishop_black = pygame.image.load('bishop_black.png')
bishop_white = pygame.image.load('bishop_white.png')

#Queens B&W

queen_black = pygame.image.load('queen_black.png')
queen_white = pygame.image.load('queen_white.png')

#Kings B&W

king_black = pygame.image.load('king_black.png')
king_white = pygame.image.load('king_white.png')

#Photo for possible movies

movies = pygame.image.load('dark_blue.png')

#Start the screen 

running = True

cell_current = ''

x_current,y_current = 0,0

x_moves,y_moves = 0,0

while running:
    
    #Showing the background

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        # Get x and y coordinates 

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_current,y_current = pygame.mouse.get_pos()

            print(x_current,y_current)

            if x_current>60 and x_current<700 and y_current>60 and y_current<700:
                        
                cell_current = matrix(x_current,y_current)

                x_moves,y_moves = dic_moves[cell_current]
    

    #Screen blit the pawns

    screen.blit(pawn_black,(80,165))
    screen.blit(pawn_black,(162,165))
    screen.blit(pawn_black,(244,165))
    screen.blit(pawn_black,(326,165))
    screen.blit(pawn_black,(408,165))
    screen.blit(pawn_black,(490,165))
    screen.blit(pawn_black,(572,165))
    screen.blit(pawn_black,(654,165))

    screen.blit(pawn_white,(80,570))
    screen.blit(pawn_white,(162,570))
    screen.blit(pawn_white,(244,570))
    screen.blit(pawn_white,(326,570))
    screen.blit(pawn_white,(408,570))
    screen.blit(pawn_white,(490,570))
    screen.blit(pawn_white,(572,570))
    screen.blit(pawn_white,(654,570))

    #Screen blit the rooks

    screen.blit(rook_black,(80,85))
    screen.blit(rook_black,(654,85))

    screen.blit(rook_white,(80,655))
    screen.blit(rook_white,(654,655))

    #Screen blit the knights

    screen.blit(knight_black,(162,85))
    screen.blit(knight_black,(572,85))

    screen.blit(knight_white,(162,655))
    screen.blit(knight_white,(572,655))

    #Screen blit the bishops

    screen.blit(bishop_black,(244,85))
    screen.blit(bishop_black,(490,85))

    screen.blit(bishop_white,(244,655))
    screen.blit(bishop_white,(490,655))

    #Screen blit the queens

    screen.blit(queen_black,(326,85))

    screen.blit(queen_white,(326,655))

    #Screen blite kings

    screen.blit(king_black,(409,85))

    screen.blit(king_white,(409,655))

    #Screen blit available movies

    if x_moves!=0 and y_moves!=0:
        
        figg = show_figg_type(x_moves,y_moves)
        color = show_figg_color(x_moves,y_moves)
        #print(figg,color)
        find_moves(figg,color,screen,x_moves,y_moves)

    # x = 81.5
    # y = 81.5

    pygame.display.update()