import math
import consts
import random
from structurs.point import Point

class Rotation:
    def __init__(self, angle, speed):
        self._angle = angle 
        self._remainingAngle = abs(self._angle)
        self._speed = speed
    
    #angle this rotated
    def Rotation(self, angle):

        speedRotation = 0.5 * self._speed
        if self._remainingAngle > 0:
            angle -= speedRotation 
            self._remainingAngle -= speedRotation

        return angle 


class Moving:
    def __init__(self, direction, distance, speed):
        self._direction = direction
        self._distance = distance 
        self._remainingDistation = self._distance
        self._speed = speed

    def GetDirection(self):
        return self._direction
    
    #position this move, angle 
    def Moving(self, position, angle):
        newPosition = position

        self._speed = 0.5 * consts.SPEED_ANIMATION_PLAYER_MOVING
        if self._remainingDistation > 0:
            self._remainingDistation -= self._speed 

        #FORWORD
        if self._direction == consts.Direction.DIRECTION_FORWARD:
            direct = Point.CreateDirection(angle)
            newPosition += direct * self._speed 
        #RIGHT
        elif self._direction == consts.Direction.DIRECTION_RIGHT:
            newAngle = angle - 90
            direct = Point.CreateDirection(newAngle)
            newPosition = position + (direct * self._speed)
        #LEFT
        elif self._direction == consts.Direction.DIRECTION_LEFT:
            newAngle = angle + 90
            direct = Point.CreateDirection(newAngle)
            newPosition = position + (direct * self._speed)
        #DOWN
        elif self._direction == consts.Direction.DIRECTION_DOWN:
            direct = Point.CreateDirection(-angle)
            newPosition -= direct * self._speed 
        #NONE
        else:
            pass

        return newPosition
