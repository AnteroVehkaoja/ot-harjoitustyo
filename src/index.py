import pygame
from gameloop import Gameloop
import render
import grid
from event_queue import EventQueue

CELL_SIZE = 48

HEIGHT = 7
WITDTH = 7
NUMBEROFMINES = 7
def main():

    display_height = HEIGHT * CELL_SIZE
    display_width = WITDTH * CELL_SIZE
    bottomtext = 100
    display2 = pygame.display.set_mode((display_width, display_height+bottomtext))

    pygame.display.set_caption("Minesweeper")

    gride = grid.Grid(HEIGHT,WITDTH,NUMBEROFMINES)

    text = grid.Text(HEIGHT,CELL_SIZE)

    renderer = render.Renderer(display2,gride,text)

    event_queue = EventQueue()

    gameloop = Gameloop(gride,text,renderer,event_queue,48)

    pygame.init()

    gameloop.start()


if __name__ == "__main__":
    main()
