from .basic_func import *
from .objects import *

def show_figg_type(x,y):

    current = matrix(x,y)

    figg_type = dic_used[current]

    return figg_type[1]

def show_figg_color(x,y):
    
    current = matrix(x,y)

    figg_type = dic_used[current]

    return figg_type[2]

def find_moves(figgType,color,screen,x,y):
    
    if figgType=='pawn':

        if color=='W':
            Pawn('W',x,y).show_moves(screen)
        
        if color=='B':
            Pawn('B',x,y).show_moves(screen)


    if figgType=='king':
        King('W',x,y).show_moves(screen)
    
    if figgType=='queen':
        Queen('W',x,y).show_moves(screen)

    if figgType=='bishop':
        Bishop('W',x,y).show_moves(screen)

    if figgType=='knight':
        Knight('W',x,y).show_moves(screen)

    if figgType=='rook':
        Rook('W',x,y).show_moves(screen)
