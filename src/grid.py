import pygame



class GridCell:
    def __init__(self,xpos,ypos,gridsize,val,ismine = False,beenclicked = False):
        self.x = xpos
        self.y = ypos
        self.val = val
        self.ismine = ismine
        self.beenclickedleft = beenclicked
        self.size = gridsize
        self.area = pygame.Rect(self.x * self.size,self.y * self.size, 48 , 48)



    def updatecell(self,cell,input):
        if input == 1 and cell.ismine:
            cell.val = -1
            print("worked")
        elif input == 1:
            cell.beenclickedleft = True


# no creation function yet this is a hard coded default testlevel
class Grid:
    def __init__(self,grid = [[GridCell(0,0,48,1),GridCell(1,0,48,2),GridCell(2,0,48,-2)],[GridCell(0,1,48,1),GridCell(1,1,48,1),GridCell(2,1,48,1)],[GridCell(0,2,48,-1),GridCell(1,2,48,1),GridCell(2,2,48,4)]]):
        self.grid = grid


