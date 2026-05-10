import unittest
import grid 



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

    def test_not_generated_generates_a_grid(self):
        gride = grid.Grid(10,10,5,guess = "yes")
        gride.update_click((10,10),1,gride,self.text)
        if gride.notgenerated:
            self.assertEqual(0,1)
        else:
            self.assertEqual(0,0)

    def test_left_click_on_mine_loses(self):
        self.cell = grid.GridCell(2,2,48,-1,ismine=True)
        self.cell.updatecell(self.grid,self.cell,1)
        self.assertTrue(self.grid.lost)
    
    def test_get_mines_in_surroundings_works(self):
        self.assertEqual(self.grid.get_mines_in_surroundings((2,2)),3)

    def testmo_get_cells_in_surroundings(self): 
        cells = self.grid.get_cells_in_surroundings(grid.GridCell(2,2,48,3))
        self.assertEqual(cells[0],grid.GridCell(1,1,48,-1,ismine= True))

    def test_get_flags_in_surroindings(self):
        self.grid.grid[0][0].updatecell(self.grid,self.grid.grid[0][0],3)
        self.assertEqual(self.grid.get_flags_in_surroundings(self.grid.grid[1][1]),1)

    def test_get_unopened_cells_in_surroundings(self):
        self.grid.grid[0][0].updatecell(self.grid,self.grid.grid[0][0],1)
        self.grid.grid[0][1].updatecell(self.grid,self.grid.grid[0][1],1)
        self.grid.grid[1][1].updatecell(self.grid,self.grid.grid[1][1],3)
        self.grid.grid[2][1].updatecell(self.grid,self.grid.grid[2][1],3)
        self.assertEqual(self.grid.get_unopened_in_surroindings(self.grid.grid[1][0])[0],grid.GridCell(0,2,48,2))


    def test_info_works(self):
        self.assertEqual(self.grid.info("reset"),(4,4,4,3) )
        self.grid.won = True
        self.assertEqual(self.grid.info("reset"),(4,4,4,1))
        self.grid.won = False
        self.grid.lost = True
        self.assertEqual(self.grid.info("reset"),(4,4,4,2) )
        
    def test_left_click_on_zero_propogate_works(self):
        self.grid.grid = [     [grid.GridCell(0,0,48,0),grid.GridCell(1,0,48,1),grid.GridCell(2,0,48,1),grid.GridCell(3,0,48,1)] 
                              ,   [grid.GridCell(0,1,48,0),grid.GridCell(1,1,48,2),grid.GridCell(2,1,48,-1,ismine=True),grid.GridCell(3,1,48,2)]   
                              ,   [grid.GridCell(0,2,48,0),grid.GridCell(1,2,48,2),grid.GridCell(2,2,48,-1,ismine=True),grid.GridCell(3,2,48,2)]
                              ,   [grid.GridCell(0,3,48,0),grid.GridCell(1,3,48,1),grid.GridCell(2,3,48,1),grid.GridCell(3,3,48,1)]   ]
        self.grid.grid[0][0].updatecell(self.grid,self.grid.grid[0][0],1)
        self.assertTrue(self.grid.grid[0][1].beenclickedleft)
        self.assertTrue(self.grid.grid[1][1].beenclickedleft)
        self.assertTrue(self.grid.grid[1][0].beenclickedleft)

    def test_propagate_loss_works(self):
        self.grid.grid = [     [grid.GridCell(0,0,48,0),grid.GridCell(1,0,48,1),grid.GridCell(2,0,48,1),grid.GridCell(3,0,48,1)] 
                              ,   [grid.GridCell(0,1,48,0),grid.GridCell(1,1,48,2),grid.GridCell(2,1,48,-1,ismine=True),grid.GridCell(3,1,48,2)]   
                              ,   [grid.GridCell(0,2,48,0),grid.GridCell(1,2,48,2),grid.GridCell(2,2,48,-1,ismine=True),grid.GridCell(3,2,48,2)]
                              ,   [grid.GridCell(0,3,48,0),grid.GridCell(1,3,48,1),grid.GridCell(2,3,48,1),grid.GridCell(3,3,48,1)]   ]
        self.grid.grid[0][1].updatecell(self.grid,self.grid.grid[0][1],3)
        self.grid.grid[0][2].updatecell(self.grid,self.grid.grid[0][2],1)
        self.grid.grid[0][2].updatecell(self.grid,self.grid.grid[0][2],1)
        self.assertTrue(self.grid.lost)

    def test_left_click_on_flag_propogate_works(self):
        self.grid.grid[1][1].updatecell(self.grid,self.grid.grid[1][1],3)
        self.grid.grid[0][0].updatecell(self.grid,self.grid.grid[0][0],1)
        self.grid.grid[0][0].updatecell(self.grid,self.grid.grid[0][0],1)
        self.assertTrue(self.grid.grid[0][1].beenclickedleft)
        self.assertTrue(self.grid.grid[1][0].beenclickedleft)



    def test_losing_works(self):
        self.grid.update_click((60,60),1,self.grid,self.text)
        self.assertTrue(self.grid.lost)
        self.assertEqual(self.text.display,"ono u lost :(")

    def test_winning_works(self):
        self.grid.update_click((10,10),1,self.grid,self.text)
        self.grid.update_click((60,10),1,self.grid,self.text)
        self.grid.update_click((110,10),1,self.grid,self.text)
        self.grid.update_click((160,10),1,self.grid,self.text)
        self.grid.update_click((10,60),1,self.grid,self.text)
        self.grid.update_click((10,110),1,self.grid,self.text)
        self.grid.update_click((10,160),1,self.grid,self.text)
        self.grid.update_click((160,60),1,self.grid,self.text)
        self.grid.update_click((160,110),1,self.grid,self.text)
        self.grid.update_click((160,160),1,self.grid,self.text)
        self.grid.update_click((60,160),1,self.grid,self.text)
        self.grid.update_click((110,160),1,self.grid,self.text)
        self.assertTrue(self.grid.won)
        self.assertEqual(self.text.display,"yay you win")
