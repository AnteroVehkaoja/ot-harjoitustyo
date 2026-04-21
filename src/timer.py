import pygame



class Clock:
    def __init__(self):
        self.base = 0
        self.clock = pygame.time.Clock()

    def tick(self, fps):
        self.clock.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks() - self.base

    def reset(self):
        self.base = pygame.time.get_ticks()
