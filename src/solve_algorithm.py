import copy

class MineZone:
    """_mine zones with the amount of mines in the zone and list of cells in the zone_
    """
    def __init__(self,size,cells):
        """construcor

        Args:
            size (_int_): _amount of mines in zone_
            cells (_[GridCell]_): _list of gridcells_
        """
        self.size = size
        self.cells = cells
        self.cellcount = len(cells)


    def __eq__(self, other):
        if isinstance(other, MineZone):
            if ((self.size == other.size) and
                (self.cellcount == other.cellcount) and
                (self.cells == other.cells)):
                return True
        return False

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
    operatable_cells = get_operatable_cells(grid)


    while True:
        if step(grid,operatable_cells) is False:
            break
        operatable_cells = get_operatable_cells(grid)

    if grid.cellsleft == 0:
        return True

    return False

def get_operatable_cells(grid):
    """gets the cells that have unopened cells around themselves and aren't flagged and are open

    Args:
        grid (_Grid_): _grid that we get the cells from_

    Returns:
        _[Gridcell]_: _list of the cells_
    """
    operatable_cells = []
    for row in grid.grid:
        for cell in row:
            if ((not cell.isflagged) and cell.beenclickedleft
                 and len(grid.get_unopened_in_surroindings(cell))) > 0:
                operatable_cells.append(cell)
    return operatable_cells

def get_unopened_cells(grid):
    cells = []
    for row in grid.grid:
        for cell in row:
            if (not cell.isflagged) and (not cell.beenclickedleft):
                cells.append(cell)
    return cells


def step(grid,opercells): #change this to call specific solve funtions
    #and dont write them in the step function itself
    """_does one deduction on the grid_

    Args:
        grid (_Grid_): _grid to do the deduction on_
        oprecells (_[GridCell]_): _this we can deduce on_

    Returns:
        _Bool_: _True if we could make a deduction False if we couldnt_
    """
    if mark_mine_simple(grid,opercells):
        return True

    if open_cell_simple(grid,opercells):
        return True

    if open_cell_two(grid,opercells):
        return True

    if mark_mine_two(grid,opercells):
        return True

    if open_one_zone(grid):
        return True

    if basic_mine_count(grid):
        return True


    return False

def mark_mine_simple(grid,opercells):
    for cell in opercells:
        if len(grid.get_unopened_in_surroindings(cell)) + grid.get_flags_in_surroundings(cell) == cell.val:
            for cell in grid.get_unopened_in_surroindings(cell):
                cell.updatecell(grid,cell,3)
                return True
    return False


def open_cell_simple(grid,opercells):
    for cell in opercells:
        if grid.get_flags_in_surroundings(cell) == cell.val:
            for cell in grid.get_unopened_in_surroindings(cell):
                cell.updatecell(grid,cell,1)
                return True
    return False

def open_cell_two(grid,opercells):
    zones = generate_zones(grid)

    for cell in opercells:
        for zone in zones:
            mark = 0
            surround = grid.get_unopened_in_surroindings(cell)
            if (len(surround) > len(zone.cells)
                and (cell.val - grid.get_flags_in_surroundings(cell) == zone.size)):
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
def mark_mine_two(grid,opercells):
    zones = generate_zones(grid)

    for cell in opercells:
        for zone in zones:
            surround = grid.get_unopened_in_surroindings(cell)
            for zonecell in zone.cells:
                if zonecell in surround:
                    surround.remove(zonecell)
            if (len(surround) > 0 and
                (len(surround) == (cell.val - grid.get_flags_in_surroundings(cell) - zone.size))):
                for cell in surround:
                    cell.updatecell(grid,cell,3)
                return True
    return False
def open_one_zone(grid):
    zones = generate_zones(grid)

    for zone in zones:
        if zone.cellcount == 1 and zone.size == 1:
            zone.cells[0].updatecell(grid,zone.cells[0],1)
            return True
    return False
def basic_mine_count(grid):
    cells = get_unopened_cells(grid)
    if grid.minecount == 0:
        for cell in cells:
            cell.updatecell(grid,cell,1)
    
def generate_zones(grid):
    """generates zones on a grid

    Args:
        grid (_Grid_): _grid to generate the zones_

    Returns:
        _[MineZone]_: _list of zones_
    """
    zones = []
    cells = get_operatable_cells(grid)
    for cell in cells:
        surround = grid.get_unopened_in_surroindings(cell)
        zones.append(MineZone(cell.val - grid.get_flags_in_surroundings(cell) ,surround))

    for big in zones:
        for small in zones:
            mark = 0
            bigcell = copy.deepcopy(big.cells)
            if small.size < big.size:
                for cell in small.cells:
                    if cell in big.cells:
                        bigcell.remove(cell)
                        mark += 1
                if len(bigcell) > 0 and len(bigcell) == big.size - small.size and mark > 0:
                    new = MineZone(big.size - small.size, bigcell )
                    if new not in zones:
                        zones.append(new)
    return zones
