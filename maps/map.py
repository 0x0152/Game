import pygame

class Map():
    def __init__(self, path):
        self._img = pygame.image.load(path)

    def Draw(self, screen):
        screen.blit(self._img, (0, 0))

        
