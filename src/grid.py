import random
import copy
import pygame
from solve_algorithm import solve

class GridCell:
    """
    class that represents a cell in the minesweeper grid
    """
    def __init__(self,xpos,ypos,gridsize,val,ismine = False,beenclicked = False):
        """_summary_

        Args:
            xpos (_int_): x position from 0 to whatever is theth
            ypos (_int_): _same as above_
            gridsize (_int_): _size of the images of the grid_
            val (_int_): _the val of the cell ie mine,0,1,2,ect_
            ismine (bool): _ismine_. Defaults to False.
            beenclicked (bool): _has it been leftcliked_. Defaults to False.
        """
        self.x = xpos
        self.y = ypos
        self.val = val
        self.ismine = ismine
        self.beenclickedleft = beenclicked
        self.isflagged = False
        self.size = gridsize
        self.area = pygame.Rect(self.x * self.size,self.y * self.size, 48 , 48)



    def updatecell(self,grid,cell,input):
        """_called to update a cell based on input_

        Args:
            grid (_Grid_): _grid that the cell is part of_
            cell (_GridCell_): _itself_
            input (_int_): _1 for left 3 for rightclick_
        """
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
        """_called to update cells around a cell_

        Args:
            grid (_Grid_): _grid that cell is apart of_
            cell (_Cell_): _itself_
            input (_int_): _1 or 3 for left and rightclick _
        """
        cells = grid.GetCellsInSurroundings(cell)
        for gridcell in cells:
            if gridcell.val == 0:
                self.updatecell(grid,gridcell,input)
            # if val isnt zero handle normal left click operation
            # since no more propogation is needed
            if gridcell.beenclickedleft is False and (gridcell.isflagged is False):
                if gridcell.ismine:
                    gridcell.val = -1 #
                    gridcell.beenclickedleft = True
                    grid.lost = True
                gridcell.beenclickedleft = True
                grid.cellsleft -= 1

    def __eq__(self, other):
        if isinstance(other, GridCell):
            if ((self.x == other.x) and
               (self.y == other.y) and
               (self.val == other.val) and
               (self.ismine == other.ismine) and
               (self.beenclickedleft == other.beenclickedleft)):
                return True
        return False

class Text:
    """_class that stores text elements_
    """
    def __init__(self,height,size,mine="0"):
        """_constructor for text_

        Args:
            height (_int_): _height of the grid in number of cells_
            size (_int_): _size of the cells in px_
            mine (str, ): _amount of mines left_. Defaults to "0".
        """
        self.display = "Playing"
        self.displaymine = mine
        self.size = size
        self.height = height
        self.displayplace = (10, self.height * self.size + 10 )
        self.displaymineplace = (10, self.height * self.size + 30)

    def reset(self):
        self.display = "Playing"

    def update(self,result,text):
        """_updates text based on result_

        Args:
            result (_str_): _won,lost,wrong will change the text_
            text (_str_): _will change the text to this_
        """
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
    """_class that represents the entire grid_
    """
    def __init__(self,height,width,mines,guess = "no"):
        """_constructor of grid class_

        Args:
            height (_int_): _height of grid in cells_
            width (_int_): _width of grid in cells_
            mines (_int_): _amount of mines_
            guess (str): _decides if a guess free board is generated_. Defaults to "no".
        """
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
        self.guess = guess

    def CreateEmpty(self): # empty grid for presentation at the start
        grid = []
        for row in range (self.height):
            row2 = []
            for cell in range (self.width):
                row2.append(GridCell(cell,row,48,1))
            grid.append(row2)

        return grid


    def UpdateClick(self,pos,button,grid,text):
        """_gameloop calls this on a click_

        Args:
            pos (_(int,int)_): _raw position of click from top left (x,y)_
            button (_int_): _1 for left 3 for right_
            grid (_Grid_): _grid that click is operating on_
            text (_Text_): _Text that clikc is operating on_

        Returns:
            _bool_: _True if text changes_
        """
        if self.notgenerated:
            self.notgenerated = False
            if self.guess == "yes": # try 1k times to find a solvable board
                x = 0
                while x < 1000:
                    self.grid = self.ActualGrid(pos,text)
                    copye = copy.deepcopy(self)
                    if solve(copye,pos):
                        break
                    x += 1
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
        """_get info from the grid for writing result_

        Args:
            write (str): _if its reset it will write that_. Defaults to "no".

        Returns:
            _str_: _part of what to write as the result_
        """
        if write == "reset" and (not(self.won or self.lost)):
            return f"reset with a {self.width} x {self.height} grid that had {self.mines} mines, in a time of "
        if self.won:
            return f"won with a {self.width} x {self.height} grid that had {self.mines} mines, in a time of "
        if self.lost:
            return f"lost with a {self.width} x {self.height} grid that had {self.mines} mines, in a time of "

    def ActualGrid(self, positionraw,text):
        """_generates the non empty grid_

        Args:
            positionraw (_(int,int)_): _raw position of click from top left (x,y)_
            text (_Text_): _text class object for the grid_

        Returns:
            _[[Gridcell]]_: _list of rows of gridcell type objects_
        """
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

        return self.grid

    def GetMinesInSurroundings(self,pos):
        """_get how many mines surround a pos_

        Args:
            pos (_(int,int)_): _position of cell in grid_

        Returns:
            _int_: _how many mines_
        """
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
        cells = self.GetCellsInSurroundings(gridcell)
        for cell in cells:
            if cell.isflagged:
                count += 1
        return count

    def GetUnopenedInSurroindings(self,gridcell):
        ans = []
        cells = self.GetCellsInSurroundings(gridcell)
        for cell in cells:
            if (not cell.beenclickedleft) and (not cell.isflagged):
                ans.append(cell)
        return ans

    def GetCellsInSurroundings(self,gridcell):
        """_gets a list of the 3/5/8 gridcell type objects around a cell_

        Args:
            gridcell (_Gridcell_): _a cell_

        Returns:
            _[Gridcell]_: _a list of gridcell objects around the argument_
        """
        cells = []
        for row in range(-1,2):
            for cell in range(-1,2):
                if ( ( (gridcell.x + cell) >= 0 and (gridcell.x + cell) < self.width ) and
                    (  (gridcell.y + row) >= 0 and (gridcell.y + row) < self.height ) and
                    ( not( (cell == 0) and (row == 0))  ) ):
                    cells.append(self.grid[gridcell.y + row][gridcell.x + cell])
        return cells

    def MakeMinePos(self,position,text): #(xpos,ypos)
        """_generate mine positions around a spot so that that spot or its surrounding cells dont have mines_

        Args:
            position (_(int,int)_): _popsition of where not to put mines_
            text (_Tect_): _text type object of the grid_

        Returns:
            _type_: _description_
        """
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
        """_get the index position from raw coordinates_

        Args:
            positionraw (_(int,int)_): _raw position_

        Returns:
            _(int,int)_: _index position_
        """
        return ((positionraw[0]//48 + 1),(positionraw[1]//48 + 1))
