import pygame

class Gameloop:
    def __init__(self,grid,text,renderer,event_queue,file,clock):
        self.grid = grid
        self.text = text
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock
        self.file = file

    def start(self):

        while True:

            if self.eventshandler() is False:
                break

            self.renderer.rendergrid((self.clock.get_ticks())//1000)

            self.clock.tick(60)



    def eventshandler (self):
        for event in self.event_queue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if game is won or lost, write to file
                if self.grid.UpdateClick(event.pos,event.button,self.grid,self.text):
                    self.file.print(self.clock.get_ticks()//1000,self.grid.info())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # if game is reset before win or lose write to file
                    if not self.grid.written:
                        self.file.print(self.clock.get_ticks()//1000,self.grid.info("reset"))
                    self.grid.reset()
                    self.text.reset()
                    self.clock.reset()


            elif event.type == pygame.QUIT:
                return False
