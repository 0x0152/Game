import pygame
import consts
import math
import numpy as np
from structurs.point import Point

def IsCollisionPoint(screen, point):
    color = screen.get_at((int(point.GetX()), int(point.GetY())))

    if color != consts.COLOR_BACKGROUND:
        return True

    return False

def IsCollisionPlayer(screen, position, angle, size, direction):
    x = y = 0.0

    size += 2
    arrPoint = np.linspace(0, np.pi * 2, 10)
    for i in arrPoint:
        if i <= np.pi:
            x = int(position.GetX() + int(math.sin(i) * size -1))
            y = int(position.GetY() + int(math.cos(i) * size -1))
        else:
            x = int(position.GetX() + int(math.sin(i) * size + -1))
            y = int(position.GetY() + int(math.cos(i) * size + -1))

        #screen.set_at((x, y), pygame.Color(0, 0, 255))
        point = Point(x, y)
        if IsOutGamePlace(point, size) == False and IsCollisionPoint(screen, point) == True:
            return True
       
    return False

def IsCollisionPlayerFourSide(screen, position, angle, size, direction):

    pointCollisionForward = position
    pointCollisionLeft = position
    pointCollisionRight = position
    pointCollisionDown = position

    #exclude coliseum with player's body
    #FORWORD
    size += 2
    direct = Point.CreateDirection(angle)
    pointCollisionForward = direct * (size + 1) + position
    #RIGHT
    newAngle = angle - 90
    direct = Point.CreateDirection(newAngle)
    pointCollisionRight = direct * size + position
    #LEFT
    newAngle = angle + 90
    direct = Point.CreateDirection(newAngle)
    pointCollisionLeft = direct * (size + 1) + position 
    #DOWN
    direct = Point.CreateDirection(angle)
    pointCollisionDown = position - direct * size

    #screen.set_at((int(pointCollisionForward.GetX()), int(pointCollisionForward.GetY())), pygame.Color(0, 255, 0))
    #screen.set_at((int(pointCollisionLeft.GetX()), int(pointCollisionLeft.GetY())), pygame.Color(0, 255, 255))
    #screen.set_at((int(pointCollisionRight.GetX()), int(pointCollisionRight.GetY())), pygame.Color(255, 255, 0))
    #screen.set_at((int(pointCollisionDown.GetX()), int(pointCollisionDown.GetY())), pygame.Color(0, 0, 255))

    if IsOutGamePlace(pointCollisionForward, size) == False and IsCollisionPoint(screen, pointCollisionForward) == True:
        print("w")
        return True 
    if IsOutGamePlace(pointCollisionRight, size) == False and IsCollisionPoint(screen, pointCollisionRight) == True:
        print("r")
        return True 
    if IsOutGamePlace(pointCollisionLeft, size) == False and IsCollisionPoint(screen, pointCollisionLeft) == True:
        print("l")
        return True 
    if IsOutGamePlace(pointCollisionDown, size) == False and IsCollisionPoint(screen, pointCollisionDown) == True:
        print("d")
        return True 

    return False

def IsOutGamePlace(position, size):
    radiusPlayer = size
    x = position.GetX()
    y = position.GetY()

    if x - radiusPlayer < 0 or y - radiusPlayer < 0 or \
       x + radiusPlayer > consts.SIZE_GAME_PLACE_X or \
       y + radiusPlayer > consts.SIZE_GAME_PLACE_Y:
           return True

    return False
