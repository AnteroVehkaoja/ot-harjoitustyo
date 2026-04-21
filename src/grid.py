import random
import pygame


class GridCell:
    def __init__(self,xpos,ypos,gridsize,val,ismine = False,beenclicked = False):
        self.x = xpos
        self.y = ypos
        self.val = val
        self.ismine = ismine
        self.beenclickedleft = beenclicked
        self.isflagged = False
        self.size = gridsize
        self.area = pygame.Rect(self.x * self.size,self.y * self.size, 48 , 48)



    def updatecell(self,grid,cell,input):
        if input == 1 and cell.isflagged: #if input is left click and its a flag dont register input
            pass
        elif input == 1 and cell.ismine: # leftclick and mine operation
            cell.val = -1 #
            cell.beenclickedleft = True
            grid.lost = True
        elif input == 1 and (not cell.beenclickedleft): # other leftclick operation
            if cell.val == 0:
                cell.beenclickedleft = True # this means the render will draw the val not empty
                self.propogate(grid,cell,input) # if value is zero click all cells around it
            cell.beenclickedleft = True
            grid.cellsleft -= 1 # to count how many cells are left
        #leftclick while open to maybe open all cells around it
        elif input == 1 and (cell.beenclickedleft) and cell.val != 0:
            if cell.val == grid.GetFlagsInSurroundings(cell):
                self.propogate(grid,cell,input)
        elif input == 3 and cell.beenclickedleft is False: #flag operation
            if cell.isflagged is False:
                cell.isflagged = True
                grid.minecount -= 1
            else:
                cell.isflagged = False
                grid.minecount += 1

    def propogate(self,grid,cell,input):
        cells = grid.GetCellsInSurroundings(cell)
        for gridcell in cells:
            if gridcell.val == 0:
                self.updatecell(grid,gridcell,input)
            # if val isnt zero handle normal left click operation
            # since no more propogation is needed
            if gridcell.beenclickedleft is False and (gridcell.isflagged == False):
                if gridcell.ismine:
                    gridcell.val = -1 #
                    gridcell.beenclickedleft = True
                    grid.lost = True
                gridcell.beenclickedleft = True
                grid.cellsleft -= 1

class Text:
    def __init__(self,height,size,mine="0"):
        self.display = "Playing"
        self.displaymine = mine
        self.size = size
        self.height = height
        self.displayplace = (10, self.height * self.size + 10 )
        self.displaymineplace = (10, self.height * self.size + 30)

    def reset(self):
        self.display = "Playing"

    def update(self,result,text):
        if result == "won":
            self.display = text
        elif result =="lost":
            self.display = text
        elif result == "wrong":
            self.display = text

    def updatemine(self,count):
        self.displaymine = str(count)


# the grid is setup in a way that intially there is an empty grid,
# and when a square is pressed it will run Actualgrid, which will
# generate mines in places that arent in or around that square. Then
# it will genrate a new grid (list of rows) with the mines in place
# then for every cell in that grid it will get the amount of mines
# in its surroundings and change its value to that.

class Grid:
    def __init__(self,height,width,mines):
        self.notgenerated = True
        self.lost = False
        self.won = False
        self.written = False
        self.height = height
        self.width = width
        self.mines = mines
        self.cellsleft = self.height * self.width - self.mines
        self.minecount = mines
        self.grid = self.CreateEmpty()


    def CreateEmpty(self): # empty grid for presentation at the start
        grid = []
        for row in range (self.height):
            row2 = []
            for cell in range (self.width):
                row2.append(GridCell(cell,row,48,1))
            grid.append(row2)

        return grid


        #function gameloop calls when a click happens
    def UpdateClick(self,pos,button,grid,text):
        if self.notgenerated:
            self.notgenerated = False
            self.grid = self.ActualGrid(pos,text)
        #collision detection
        for row in self.grid:
            for cell in row:
                if cell.area.collidepoint(pos):
                    cell.updatecell(grid,cell,button)

        if self.cellsleft == 0 and (not self.lost):
            self.won = True
        if self.won:
            text.update("won" , "yay you win")
            if not self.written:
                self.written = True
                return True
        elif self.lost:
            text.update("lost", "ono u lost :(")
            if not self.written:
                self.written = True
                return True
        text.updatemine(grid.minecount)

    def reset(self):
        self.notgenerated = True
        self.lost = False
        self.won = False
        self.written = False
        self.cellsleft = self.height * self.width - self.mines
        self.grid = self.CreateEmpty()
        self.minecount = self.mines

    def info(self,write = "no"):
        if write == "reset" and (not(self.won or self.lost)):
            return f"reset with a {self.width} x {self.height} grid that had {self.mines} mines, in a time of "
        elif self.won:
            return f"won with a {self.width} x {self.height} grid that had {self.mines} mines, in a time of "
        elif self.lost:
            return f"lost with a {self.width} x {self.height} grid that had {self.mines} mines, in a time of "

    def ActualGrid(self, positionraw,text):
        position = self.positiondecoder(positionraw) # will get form (xpos,ypos)
        mines = self.MakeMinePos(position,text) # position argument to tell where not to put mines
        grid = []
        for row in range (self.height):
            row2 = []
            for cell in range (self.width):
                if (cell,row) in mines:
                    row2.append(GridCell(cell,row,48,-1,ismine=True))
                else:
                    row2.append(GridCell(cell,row,48,0))
            grid.append(row2)

        self.grid = grid
        for row in grid:
            for cell in row:
                cell.val = self.GetMinesInSurroundings((cell.x,cell.y))
        return grid


    #combine the main part into one and these ones should just parse that result
    def GetMinesInSurroundings(self,pos):
        count = 0
        for row in range(-1,2):
            for cell in range(-1,2):
                if( ( (pos[0] + cell) >= 0 and (pos[0] + cell) < self.width ) and
                  (  (pos[1] + row) >= 0 and (pos[1] + row) < self.height ) and
                 ( not( (cell == 0) and (row == 0))  ) ):
                    if self.grid[pos[1] + row][pos[0] + cell].ismine:
                        count += 1
        return count


    def GetFlagsInSurroundings(self,gridcell):
        count = 0
        for row in range(-1,2):
            for cell in range(-1,2):
                if ( ( (gridcell.x + cell) >= 0 and (gridcell.x + cell) < self.width ) and
                    (  (gridcell.y + row) >= 0 and (gridcell.y + row) < self.height ) and
                    ( not( (cell == 0) and (row == 0))  ) ):
                    if self.grid[gridcell.y + row][gridcell.x + cell].isflagged:
                        count += 1
        return count


    def GetCellsInSurroundings(self,gridcell):
        cells = []
        for row in range(-1,2):
            for cell in range(-1,2):
                if ( ( (gridcell.x + cell) >= 0 and (gridcell.x + cell) < self.width ) and
                    (  (gridcell.y + row) >= 0 and (gridcell.y + row) < self.height ) and
                    ( not( (cell == 0) and (row == 0))  ) ):
                    cells.append(self.grid[gridcell.y + row][gridcell.x + cell])
        return cells

    def MakeMinePos(self,position,text): #(xpos,ypos)
        possiblepositions = []
        for row in range(self.height):
            for cell in range(self.width):
                if ( cell in (position[0] - 2, position[0] - 1, position[0]) and
                    (row in (position[1] - 2, position[1] - 1, position[1])) ):
                    pass
                else:
                    possiblepositions.append((cell,row))
        if len(possiblepositions) < self.mines:
            text.update("wrong","change .env file to have more space or less mines")
            return []
        return random.sample(possiblepositions, self.mines)


# remember to change this when you add draw non board elements on the top or the left
    def positiondecoder(self,positionraw):
        return ((positionraw[0]//48 + 1),(positionraw[1]//48 + 1))
