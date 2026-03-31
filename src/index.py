import pygame 
from gameloop import Gameloop
import render
import grid 
from event_queue import EventQueue


CELL_SIZE = 48

def main():

    height = 3
    width = 3


    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display2 = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Minesweeper")
   
    gride = grid.Grid()
    
    renderer = render.Renderer(display2,gride)

    event_queue = EventQueue()

    gameloop = Gameloop(gride,renderer,event_queue,48)
   
    pygame.init()
  
    gameloop.start()
  

if __name__ == "__main__":
    main()