import os
import pygame


name = os.path.dirname(__file__)
os.path.join(name,"Pictures", "mine.png")


mine = pygame.image.load(os.path.join(name,"Pictures", "mine.png"))
one = pygame.image.load(os.path.join(name,"Pictures", "one.png"))
two = pygame.image.load(os.path.join(name,"Pictures", "two.png"))
three = pygame.image.load(os.path.join(name,"Pictures", "three.png"))
four = pygame.image.load(os.path.join(name,"Pictures", "four.png"))
five = pygame.image.load(os.path.join(name,"Pictures", "five.png"))
six = pygame.image.load(os.path.join(name,"Pictures", "six.png"))
seven = pygame.image.load(os.path.join(name,"Pictures", "seven.png"))
eight = pygame.image.load(os.path.join(name,"Pictures", "eight.png"))
flag = pygame.image.load(os.path.join(name,"Pictures", "flag.png"))
gridim = pygame.image.load(os.path.join(name,"Pictures", "griddef.png"))
empty = pygame.image.load(os.path.join(name,"Pictures", "empty.png"))



class Renderer:
    def __init__(self,display,grid,text) :
        self.display = display
        self.grid = grid
        self.text = text



    def rendergrid(self,time):
        self.display.fill((255, 255, 255))
        for row in self.grid.grid:
            for cell in row:
                self.rendercell(cell,self.display)
        self.drawtext(self.text.display, self.text.displayplace ,self.display)
        self.drawmine(self.text.displaymine, self.text.displaymineplace ,self.display)
        self.drawtimer(time,(self.text.displayplace[0], self.text.displayplace[1] + 60), self.display)
        pygame.display.update()
    def rendercell(self,cell,display):

        if cell.isflagged:
            display.blit(flag, cell.area)

        elif not cell.beenclickedleft:
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

    def drawtext(self,text,place,display):
        screen = pygame.font.SysFont("Sans",25, True).render(text, True, (200, 0, 0))
        rect = pygame.Rect(place,(10,10))

        display.blit(screen,rect)

    def drawmine(self,text,place,display):
        screen = pygame.font.SysFont("Sans",25, True).render(text, True, (200, 0, 0))
        rect = pygame.Rect(place,(10,10))
        display.blit(screen,rect)

    def drawtimer(self,text,place,display):
        screen = pygame.font.SysFont("Sans",25, True).render(str(text), True, (200, 0, 0))
        rect = pygame.Rect(place,(10,10))
        display.blit(screen,rect)
