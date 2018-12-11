import math
import pygame
import consts
import random
from maps import map
from gameObjects import player
from scenes.scene import Scene

class TestScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self._players = []
        self._map = map.Map("img.png")
        pass

    def AddObject(self, object):
        pass

    def DeleteObject(self, idObject):
        pass

    def Update(self, screen, event):
        if event.type == pygame.KEYDOWN:
            self.onEvent("New")
        
        pass

    def Draw(self, screen):
        self._map.Draw(screen)

        for pl in self._players:
            pl.Update(screen)

    def Enter(self):
        self.BindSceneWithEvent("New", TestScene2())

        print("create scene 1")

        self._players = [player.Player(200, 200, 180)]

        for pl in range(0, 20):
            self._players.append(player.Player(random.randint(20, 780), random.randint(20, 480), random.randint(0, 360)))

        for pl in self._players:
            pl.Move(1, 10000)
            #pl.Move(random.randint(1, 4), 10000)
            #pl.Rotation(8100)

    def Leave(self):
        print("leave scene 1")
        pass

class TestScene2(Scene):
    def __init__(self):
        Scene.__init__(self)
        self._players = []
        pass

    def AddObject(self, object):
        pass

    def DeleteObject(self, idObject):
        pass

    def Update(self, screen, event):
        pass

    def Draw(self, screen):
        for pl in self._players:
            pl.Draw(screen)
        
        
        for pl in self._players:
            pl.Update(screen)

    def Enter(self):
        print("create scene 2")


    def Leave(self):
        print("leave scene 2")
        pass
