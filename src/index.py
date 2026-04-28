import pygame
from gameloop import Gameloop
import render
import grid
from event_queue import EventQueue
import timer
import file
from config import HEIGHT , CELL_SIZE, WITDTH, NUMBEROFMINES, GEN_GRID



def main():

    display_height = HEIGHT * CELL_SIZE
    display_width = WITDTH * CELL_SIZE
    bottomtext = 100
    display2 = pygame.display.set_mode((display_width, display_height+bottomtext))

    pygame.display.set_caption("Minesweeper")

    gride = grid.Grid(HEIGHT,WITDTH,NUMBEROFMINES,GEN_GRID)

    text = grid.Text(HEIGHT,CELL_SIZE)

    writee = file.Write()

    renderer = render.Renderer(display2,gride,text)

    event_queue = EventQueue()

    clock = timer.Clock()

    gameloop = Gameloop(gride,text,renderer,event_queue,writee,clock)

    pygame.init()

    gameloop.start()


if __name__ == "__main__":
    main()
