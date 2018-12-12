import math 
import consts
import pygame
import copy
import animation
import collision
import structurs.point
from gameObjects.gameObject import GameObject
from enum import Enum
from gameObjects import gun 
from structurs.point import Point

def FloatToInt(point):
    if len(point) == 2:
        return [int(point[0]), int(point[1])]
    else:
        return point

class Player(GameObject):

    def __init__(self, x, y, angle):
        self._position = Point(x, y)

        self._color = consts.COLOR_PLAYER
        self._size = consts.SIZE_PLAYER 

        #Radians
        self._angle = angle

        self._moving = animation.Moving(consts.Direction.DIRECTION_NONE, 0, 0)
        self._rotation = animation.Rotation(0, 0)

        self._gun = gun.Gun(self._position, self._angle, self._size)

    def Rotation(self, angle):
        self._rotation = animation.Rotation(angle, consts.SPEED_ANIMATION_PLAYER_ROTATION)

    def Move(self, direction, duration):
        self._moving = animation.Moving(direction, duration, consts.SPEED_ANIMATION_PLAYER_MOVING)
    
    def Update(self, screen, events):
        self._angle = self._rotation.Rotation(self._angle)
        oldPosition = copy.deepcopy(self._position)
        self._position = self._moving.Moving(copy.deepcopy(oldPosition), self._angle)
        self._gun.UpdateGun(self._position, self._angle, self._size)

        if collision.IsOutGamePlace(copy.deepcopy(self._position), self._size) == True or \
           collision.IsCollisionPlayer(screen, copy.deepcopy(self._position), self._angle, self._size, self._moving.GetDirection()) == True:
            self._position = oldPosition 
            
        self._gun.UpdateGun(self._position, self._angle, self._size)
    def Draw(self, screen):

        pygame.draw.circle(screen, self._color, self._position.GetArrInt(), self._size)
        self._gun.Draw(screen)

        pass
