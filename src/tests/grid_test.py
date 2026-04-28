import unittest
import grid 
import pygame


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = grid.Grid(4,4,4)
        self.grid.grid = [     [grid.GridCell(0,0,48,1),grid.GridCell(1,0,48,2),grid.GridCell(2,0,48,2),grid.GridCell(3,0,48,1)] 
                              ,   [grid.GridCell(0,1,48,2),grid.GridCell(1,1,48,-1,ismine= True),grid.GridCell(2,1,48,-1,ismine=True),grid.GridCell(3,1,48,2)]   
                              ,   [grid.GridCell(0,2,48,2),grid.GridCell(1,2,48,-1,ismine= True),grid.GridCell(2,2,48,-1,ismine=True),grid.GridCell(3,2,48,2)]
                              ,   [grid.GridCell(0,3,48,1),grid.GridCell(1,3,48,2),grid.GridCell(2,3,48,2),grid.GridCell(3,3,48,1)]   ]
        self.grid.notgenerated = False
        self.cell = grid.GridCell(2,2,48,3)
        self.text = grid.Text(4,48)

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

    def testmo_get_cells_in_surroundings(self): 
        cells = self.grid.GetCellsInSurroundings(grid.GridCell(2,2,48,3))
        self.assertEqual(cells[0],grid.GridCell(1,1,48,-1,ismine= True))

    def test_get_flags_in_surroindings(self):
        self.grid.grid[0][0].updatecell(self.grid,self.grid.grid[0][0],3)
        self.assertEqual(self.grid.GetFlagsInSurroundings(self.grid.grid[1][1]),1)

    def test_info_works(self):
        self.assertEqual(self.grid.info("reset"),"reset with a 4 x 4 grid that had 4 mines, in a time of " )
        self.grid.won = True
        self.assertEqual(self.grid.info("reset"),"won with a 4 x 4 grid that had 4 mines, in a time of " )
        self.grid.won = False
        self.grid.lost = True
        self.assertEqual(self.grid.info("reset"),"lost with a 4 x 4 grid that had 4 mines, in a time of " )
        
    def test_left_click_on_zero_propogate_works(self):
        self.grid.grid = [     [grid.GridCell(0,0,48,0),grid.GridCell(1,0,48,1),grid.GridCell(2,0,48,1),grid.GridCell(3,0,48,1)] 
                              ,   [grid.GridCell(0,1,48,1),grid.GridCell(1,1,48,3),grid.GridCell(2,1,48,-1,ismine=True),grid.GridCell(3,1,48,2)]   
                              ,   [grid.GridCell(0,2,48,1),grid.GridCell(1,2,48,-1,ismine= True),grid.GridCell(2,2,48,-1,ismine=True),grid.GridCell(3,2,48,2)]
                              ,   [grid.GridCell(0,3,48,1),grid.GridCell(1,3,48,2),grid.GridCell(2,3,48,2),grid.GridCell(3,3,48,1)]   ]
        self.grid.grid[0][0].updatecell(self.grid,self.grid.grid[0][0],1)
        self.assertTrue(self.grid.grid[0][1].beenclickedleft)
        self.assertTrue(self.grid.grid[1][1].beenclickedleft)
        self.assertTrue(self.grid.grid[1][0].beenclickedleft)

    def test_left_click_on_flag_propogate_works(self):
        self.grid.grid[1][1].updatecell(self.grid,self.grid.grid[1][1],3)
        self.grid.grid[0][0].updatecell(self.grid,self.grid.grid[0][0],1)
        self.grid.grid[0][0].updatecell(self.grid,self.grid.grid[0][0],1)
        self.assertTrue(self.grid.grid[0][1].beenclickedleft)
        self.assertTrue(self.grid.grid[1][0].beenclickedleft)

    def test_losing_works(self):
        self.grid.UpdateClick((60,60),1,self.grid,self.text)
        self.assertTrue(self.grid.lost)
        self.assertEqual(self.text.display,"ono u lost :(")

    def test_winning_works(self):
        self.grid.UpdateClick((10,10),1,self.grid,self.text)
        self.grid.UpdateClick((60,10),1,self.grid,self.text)
        self.grid.UpdateClick((110,10),1,self.grid,self.text)
        self.grid.UpdateClick((160,10),1,self.grid,self.text)
        self.grid.UpdateClick((10,60),1,self.grid,self.text)
        self.grid.UpdateClick((10,110),1,self.grid,self.text)
        self.grid.UpdateClick((10,160),1,self.grid,self.text)
        self.grid.UpdateClick((160,60),1,self.grid,self.text)
        self.grid.UpdateClick((160,110),1,self.grid,self.text)
        self.grid.UpdateClick((160,160),1,self.grid,self.text)
        self.grid.UpdateClick((60,160),1,self.grid,self.text)
        self.grid.UpdateClick((110,160),1,self.grid,self.text)
        self.assertTrue(self.grid.won)
        self.assertEqual(self.text.display,"yay you win")