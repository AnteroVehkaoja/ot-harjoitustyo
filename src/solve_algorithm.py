
class MineZone:
    """_mine zones with the amount of mines in zone and list of cells in the zone_
    """
    def __init__(self,size,cells):
        """construcor

        Args:
            size (_int_): _amount of mines in zone_
            cells (_[GridCell]_): _list of gridcells_
        """
        self.size = size
        self.cells = cells





#remember you had an original here for testing
def solve(grid,pos):
    """_solves a specific grid_

    Args:
        grid (_Grid_): _Grid being solved_
        pos (_(int,int)_): _where first click was raw input from top left_

    Returns:
        _Bool_: _True if can be solved False if cant_
    """
    for row in grid.grid:
        for cell in row:
            if cell.area.collidepoint(pos):
                cell.updatecell(grid,cell,1)
    OperatableCells = GetOperatableCells(grid)


    while True:
        if step(grid,OperatableCells) is False:
            break
        OperatableCells = GetOperatableCells(grid)

    if grid.cellsleft == 0:
        return True

    return False

def GetOperatableCells(grid):
    """gets the cells that have unopened cells around it and isnt flagged and is open

    Args:
        grid (_Grid_): _grid that we get the cells from_

    Returns:
        _[Gridcell]_: _list of the cells_
    """
    OperatableCells = []
    for row in grid.grid:
        for cell in row:
            if ((not cell.isflagged) and cell.beenclickedleft
                 and len(grid.GetUnopenedInSurroindings(cell))) > 0:
                OperatableCells.append(cell)
    return OperatableCells

def step(grid,oprecells): #change this to call specific solve funtions
    #and dont write them in the step function itself
    """_does one deduction on the grid_

    Args:
        grid (_Grid_): _grid to do the deduction on_
        oprecells (_[GridCell]_): _this we can deduce on_

    Returns:
        _Bool_: _True if we could make a deduction False if we couldnt_
    """
    for cell in oprecells:
        if len(grid.GetUnopenedInSurroindings(cell)) + grid.GetFlagsInSurroundings(cell) == cell.val:
            for cell in grid.GetUnopenedInSurroindings(cell):
                cell.updatecell(grid,cell,3)
                return True

    for cell in oprecells:
        if grid.GetFlagsInSurroundings(cell) == cell.val:
            for cell in grid.GetUnopenedInSurroindings(cell):
                cell.updatecell(grid,cell,1)
                return True

    zones = GenerateZones(grid)

    for cell in oprecells:
        for zone in zones:
            mark = 0
            surround = grid.GetUnopenedInSurroindings(cell)
            if (len(surround) > len(zone.cells)
                and (cell.val - grid.GetFlagsInSurroundings(cell) == zone.size)):
                for zonecell in zone.cells:
                    if zonecell in surround:
                        surround.remove(zonecell)
                    else:
                        mark = 1
                if mark == 0:
                    for cell in surround:
                        cell.updatecell(grid,cell,1)
                    return True

    return False

def GenerateZones(grid):
    """generates zones on a grid

    Args:
        grid (_Grid_): _grid to generate the zones_

    Returns:
        _[MineZone]_: _list of zones_
    """
    zones = []
    cells = GetOperatableCells(grid)
    for cell in cells:
        surround = grid.GetUnopenedInSurroindings(cell)
        zones.append(MineZone(cell.val - grid.GetFlagsInSurroundings(cell) ,surround))
    return zones
