from .basic_func import *
import pygame

class Figgs():
    
    def __init__(self,color,x_pos,y_pos):   

        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def show_moves(self, screen, up_num, down_num , right_num, left_num, right_up_diag_num, left_up_diag_num, right_down_diag_num, left_down_diag_num, G_right_up, G_left_up, G_right_down, G_left_down):

        moves = pygame.image.load('dark_blue.png')
        x = 81.5
        y = 81.5

        if G_right_up:

            if self.x_pos + x <700 and self.y_pos - 2*y > 60:

                current = matrix(self.x_pos+x,self.y_pos-2*y)

                a=dic_used[current]

                if a[0]=='unused':

                    screen.blit(moves,(self.x_pos + x, self.y_pos-2*y))
            


        if G_left_up:

            if self.x_pos - x > 60 and self.y_pos - 2*y > 60:
                
                current = matrix(self.x_pos-x,self.y_pos-2*y)

                a=dic_used[current]

                if a[0]=='unused':

                    screen.blit(moves,(self.x_pos - x, self.y_pos-2*y))

        if G_right_down:

            if self.x_pos + x <700 and self.y_pos + 2*y <680:

                current = matrix(self.x_pos+x,self.y_pos+2*y)

                a=dic_used[current]

                if a[0]=='unused':

                    screen.blit(moves,(self.x_pos + x, self.y_pos+2*y))

        if G_left_down:

            if self.x_pos - x > 60 and self.y_pos + 2*y <680:

                current = matrix(self.x_pos-x,self.y_pos+2*y)

                a=dic_used[current]

                if a[0]=='unused':

                    screen.blit(moves,(self.x_pos - x, self.y_pos +2*y))


        for i in range(1,up_num+1):

            if self.y_pos - i*y < 60:
                break

            current = matrix(self.x_pos,self.y_pos-i*y)

            if current==None:
                break

            a=dic_used[current]

            if a[0]=='used':
                break

            screen.blit(moves,(self.x_pos, self.y_pos - i*y))

        for i in range(1,down_num+1):
            
            if self.y_pos + i*y > 700:
                break

            current = matrix(self.x_pos,self.y_pos+i*y)

            if current==None:
                break

            a=dic_used[current]

            if a[0]=='used':
                break

            screen.blit(moves,(self.x_pos, self.y_pos + i*y))

        for i in range(1,left_num+1):
            
            if self.x_pos - i*x < 60:
                break

            current = matrix(self.x_pos-i*x,self.y_pos)

            if current==None:
                break

            a=dic_used[current]

            if a[0]=='used':
                break

            screen.blit(moves,(self.x_pos - i*x, self.y_pos))

        for i in range(1,right_num+1):
            
            if self.x_pos + i*x > 680:
                break

            current = matrix(self.x_pos+i*x,self.y_pos)

            if current==None:
                break

            a=dic_used[current]

            if a[0]=='used':
                break

            screen.blit(moves,(self.x_pos + i*x, self.y_pos))

        for i in range(1,right_up_diag_num+1):
            
            if self.y_pos - i*y < 60 or self.x_pos + i*x >700 :
                break

            current = matrix(self.x_pos+i*x,self.y_pos-i*y)

            if current==None:
                break

            a=dic_used[current]

            if a[0]=='used':
                break

            screen.blit(moves,(self.x_pos + i*x, self.y_pos - i*y))

        for i in range(1,right_down_diag_num+1):
        
            if self.y_pos + i*y > 700 or self.x_pos + i*x >700 :
                break

            current = matrix(self.x_pos+i*x,self.y_pos+i*y)

            if current==None:
                break

            a=dic_used[current]

            if a[0]=='used':
                break

            screen.blit(moves,(self.x_pos + i*x, self.y_pos + i*y))

        for i in range(1,left_up_diag_num+1):
            
            if self.y_pos - i*y < 60 or self.x_pos - i*x < 60 :
                break

            current = matrix(self.x_pos-i*x,self.y_pos-i*y)

            if current==None:
                break

            a=dic_used[current]

            if a[0]=='used':
                break

            screen.blit(moves,(self.x_pos - i*x, self.y_pos - i*y))

        for i in range(1,left_down_diag_num+1):
        
            if self.y_pos + i*y > 700 or self.x_pos - i*x < 60 :
                break

            current = matrix(self.x_pos-i*x,self.y_pos+i*y)

            if current==None:
                break

            a=dic_used[current]

            if a[0]=='used':
                break

            screen.blit(moves,(self.x_pos - i*x, self.y_pos + i*y))

class Pawn(Figgs):

    def __init__(self, color, x_pos, y_pos):

        super().__init__(color, x_pos, y_pos)

    def show_moves(self, screen):
        
        if self.color == "W":
            return super().show_moves(screen, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        
        if self.color == "B":
            return super().show_moves(screen, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class Bishop(Figgs):

    def __init__(self, color, x_pos, y_pos):

        super().__init__(color, x_pos, y_pos)

    def show_moves(self, screen):

        return super().show_moves(screen, 0, 0, 0, 0, 16, 16, 16, 16, 0, 0, 0, 0)

class Knight(Figgs):

    def __init__(self, color, x_pos, y_pos):

        super().__init__(color, x_pos, y_pos)

    def show_moves(self, screen):

        return super().show_moves(screen, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1)

class Rook(Figgs):

    def __init__(self, color, x_pos, y_pos):

        super().__init__(color, x_pos, y_pos)

    def show_moves(self, screen):

        return super().show_moves(screen, 8,8,8,8,0,0,0,0,0,0,0,0)

class King(Figgs):

    def __init__(self, color, x_pos, y_pos):

        super().__init__(color, x_pos, y_pos)

    def show_moves(self, screen):

        return super().show_moves(screen, 1,1,1,1,1,1,1,1,0,0,0,0)

class Queen(Figgs):

    def __init__(self, color, x_pos, y_pos):

        super().__init__(color, x_pos, y_pos)

    def show_moves(self, screen):

        return super().show_moves(screen,8,8,8,8,16,16,16,16,0,0,0,0)
        

