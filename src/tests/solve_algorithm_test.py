import unittest
import grid 
import solve_algorithm


class TestAlgorithm(unittest.TestCase):
    def test_board_one_solvable(self):
        self.grid = grid.Grid(5,5,9)
        self.grid.grid = [     [grid.GridCell(0,0,48,-1,ismine=True),grid.GridCell(1,0,48,2),grid.GridCell(2,0,48,-1,ismine=True),grid.GridCell(3,0,48,1),grid.GridCell(4,0,48,0)] 
                              ,   [grid.GridCell(0,1,48,2),grid.GridCell(1,1,48,3),grid.GridCell(2,1,48,1),grid.GridCell(3,1,48,2),grid.GridCell(4,1,48,1)]   
                              ,   [grid.GridCell(0,2,48,-1,ismine=True),grid.GridCell(1,2,48,2),grid.GridCell(2,2,48,0),grid.GridCell(3,2,48,2),grid.GridCell(4,1,48,-1,ismine=True)]
                              ,   [grid.GridCell(0,3,48,-1,ismine=True),grid.GridCell(1,3,48,4),grid.GridCell(2,3,48,1),grid.GridCell(3,3,48,4),grid.GridCell(4,3,48,-1,ismine=True)]   
                              ,   [grid.GridCell(0,4,48,-1,ismine= True),grid.GridCell(1,4,48,3),grid.GridCell(2,4,48,-1,ismine=True),grid.GridCell(3,4,48,3),grid.GridCell(4,4,48,-1,ismine=True)]   ]
        self.assertTrue(solve_algorithm.solve(self.grid,(110,110)))
    
    def test_basic_minecount(self):
        self.grid = grid.Grid(5,5,4)
        self.grid.grid = [     [grid.GridCell(0,0,48,0),grid.GridCell(1,0,48,0),grid.GridCell(2,0,48,0),grid.GridCell(3,0,48,0),grid.GridCell(4,0,48,0)] 
                              ,   [grid.GridCell(0,1,48,0),grid.GridCell(1,1,48,1),grid.GridCell(2,1,48,1),grid.GridCell(3,1,48,1),grid.GridCell(4,1,48,0)]   
                              ,   [grid.GridCell(0,2,48,0),grid.GridCell(1,2,48,1),grid.GridCell(2,2,48,-1,ismine=True),grid.GridCell(3,2,48,3),grid.GridCell(4,1,48,2)]
                              ,   [grid.GridCell(0,3,48,0),grid.GridCell(1,3,48,1),grid.GridCell(2,3,48,3),grid.GridCell(3,3,48,-1,ismine=True),grid.GridCell(4,3,48,-1,ismine=True)]   
                              ,   [grid.GridCell(0,4,48,0),grid.GridCell(1,4,48,0),grid.GridCell(2,4,48,2),grid.GridCell(3,4,48,-1,ismine=True),grid.GridCell(4,4,48,3)]   ]
        self.assertTrue(solve_algorithm.solve(self.grid,(10,10)))
    