import pygame
from gameObjects.gameObject import GameObject
from structurs.point import Point

class Bullet(GameObject):
    def __init__(self, position, direction, speed, damage):
        self._position = position
        self._direction = direction 
        self._speed = speed 
        self._damage = damage

    def Update(self, event, screen):
        pass

    def Draw(self, screen):
        pass

class Gun(GameObject):

    def __init__(self, position, angle, size):
        self._color = [0x00, 0x00, 0xff]
        self._position = position
        self._angle = angle
        self._size = size

    def Draw(self, screen):

        direction = Point.CreateDirection(self._angle)

        endLine = direction * (self._size - 2) + self._position

        pygame.draw.line(screen, self._color, self._position.GetArrInt(), endLine.GetArrInt())

    def Update(self, event, screen):
        pass

    def UpdateGun(self, position, angle, size):
        self._position = position
        self._angle = angle
        self._size = size

