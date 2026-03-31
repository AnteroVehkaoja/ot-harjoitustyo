import pygame

class Gameloop:
    def __init__(self,grid,renderer,event_queue,cell_size): 
        self.grid = grid
        self.renderer = renderer
        self.event_queue = event_queue
        self.cell_size = cell_size
        self._clock = pygame.time.Clock()
    
    def start(self):
        
        while True:

            if self.eventshandler() == False:
                break

            self.renderer.rendergrid()

            self._clock.tick(30)

           

    def eventshandler (self):
        for event in self.event_queue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for row in self.grid.grid:
                    for cell in row:
                        if cell.area.collidepoint(event.pos):
                            cell.updatecell(cell , event.button)



        
        
            elif event.type == pygame.QUIT:
                    return False