import pygame
import os

mine = pygame.image.load("src/Pictures/mine.png")
one = pygame.image.load("src/Pictures/one.png")
two = pygame.image.load("src/Pictures/two.png")
three = pygame.image.load("src/Pictures/three.png")
four = pygame.image.load("src/Pictures/four.png")
five = pygame.image.load("src/Pictures/five.png")
six = pygame.image.load("src/Pictures/six.png")
seven = pygame.image.load("src/Pictures/seven.png")
eight = pygame.image.load("src/Pictures/eight.png")
flag = pygame.image.load("src/Pictures/flag.png")
gridim = pygame.image.load("src/Pictures/griddef.png")
empty = pygame.image.load("src/Pictures/empty.png")



class Renderer:
    def __init__(self,display,grid) :
        self.display = display
        self.grid = grid



    def rendergrid(self):
        for row in self.grid.grid:
            for cell in row:
                self.rendercell(cell,self.display)
        pygame.display.update()


    def rendercell(self,cell,display):

        if not cell.beenclickedleft:
            self.drawempty(cell,display)
        
        elif cell.val == -1 :
            display.blit(mine, cell.area)
        elif cell.val == 0:
            display.blit(empty, cell.area)
        elif cell.val == 1:
            display.blit(one, cell.area)
        elif cell.val == 2:
            display.blit(two, cell.area)
        elif cell.val == 3:
            display.blit(three, cell.area)
        elif cell.val == 4:
            display.blit(four, cell.area)
        elif cell.val == 5:
            display.blit(five, cell.area)
        elif cell.val == 6:
            display.blit(six, cell.area)
        elif cell.val == 7:
            display.blit(seven, cell.area)
        elif cell.val == 8:
            display.blit(eight, cell.area)
        elif cell.val == -2:
            display.blit(gridim, cell.area)

    def drawempty(self,cell,display):
        display.blit(gridim, cell.area)