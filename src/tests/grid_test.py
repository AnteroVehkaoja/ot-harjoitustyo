import unittest
import grid 
import pygame


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = grid.Grid(4,4,4)
        self.grid.grid = [     [grid.GridCell(0,0,48,1),grid.GridCell(1,0,48,1),grid.GridCell(2,0,48,1),grid.GridCell(3,0,48,1)] 
                              ,   [grid.GridCell(0,1,48,1),grid.GridCell(1,1,48,-1,ismine= True),grid.GridCell(2,1,48,-1,ismine=True),grid.GridCell(3,1,48,1)]   
                              ,   [grid.GridCell(0,2,48,1),grid.GridCell(1,2,48,-1,ismine= True),grid.GridCell(2,2,48,-1,ismine=True),grid.GridCell(3,2,48,1)]
                              ,   [grid.GridCell(0,3,48,1),grid.GridCell(1,3,48,1),grid.GridCell(2,3,48,1),grid.GridCell(3,3,48,1)]   ]
        self.cell = grid.GridCell(2,2,48,3)

    def test_updatecell_works_on_right_click(self):
        self.cell.updatecell(self.grid,self.cell,3)
        self.assertTrue(self.cell.isflagged) #rightclick makes flagged
        self.cell.updatecell(self.grid,self.cell,3)
        self.assertFalse(self.cell.isflagged) # rightclick again unflags
        self.cell.updatecell(self.grid,self.cell,1) #leftclick
        self.cell.updatecell(self.grid,self.cell,3) #followed by right
        self.assertFalse(self.cell.isflagged) #doesnt flag

    def test_left_click_on_mine_loses(self):
        self.cell = grid.GridCell(2,2,48,-1,ismine=True)
        self.cell.updatecell(self.grid,self.cell,1)
        self.assertTrue(self.grid.lost)
    
    def test_get_mines_in_surroundings_works(self):
        self.assertEqual(self.grid.GetMinesInSurroundings((2,2)),3)

    def testmo_get_cells_in_surroundings(self): #make an equals inctace for gridcell at some point
        cells = self.grid.GetCellsInSurroundings(grid.GridCell(2,2,48,3))
        self.assertEqual(cells[0].x,1)
        self.assertEqual(cells[1].ismine,True)
        self.assertEqual(cells[2].ismine,False)