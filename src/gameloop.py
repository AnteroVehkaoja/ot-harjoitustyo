import pygame

class Gameloop:
    def __init__(self,grid,text,renderer,event_queue,cell_size):
        self.grid = grid
        self.text = text
        self.renderer = renderer
        self.event_queue = event_queue
        self.cell_size = cell_size
        self._clock = pygame.time.Clock()

    def start(self):

        while True:

            if self.eventshandler() is False:
                break

            self.renderer.rendergrid()

            self._clock.tick(30)



    def eventshandler (self):
        for event in self.event_queue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.grid.UpdateClick(event.pos,event.button,self.grid,self.text)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.grid.reset()
                    self.text.reset()


            elif event.type == pygame.QUIT:
                return False
