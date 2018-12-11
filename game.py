import math
import pygame
from scenes.testScene import TestScene
from gameObjects import player
import consts


class Game:

    def __init__(self):
        self._currentScene = TestScene()

    def Start(self):
        pygame.init()
        self._currentScene.Enter()

        screen = pygame.display.set_mode([consts.SIZE_GAME_PLACE_X, consts.SIZE_GAME_PLACE_Y])
        screen.fill(consts.COLOR_BACKGROUND)

        pygame.display.set_caption(consts.CAPTION_WINDOW)
        clock = pygame.time.Clock()

        done = False
        while done == False:
            
            self._currentScene.Draw(screen)

            for event in pygame.event.get():

                self._currentScene.Update(screen, event)

                if event.type == pygame.QUIT:
                    done = True

            pygame.display.flip()
            clock.tick(60)
            screen.fill(consts.COLOR_BACKGROUND)
            
            isSwitchScene, nextScene = self._currentScene.GetNextScene()

            if isSwitchScene:
                self._currentScene.Leave()
                self._currentScene = nextScene
                self._currentScene.Enter()


        self._currentScene.Leave()

        pygame.quit()

