from abc import ABCMeta, abstractmethod

class Scene:
    __metaclass__ = ABCMeta

    def __init__(self):
        #key -> string(name event)
        #value Scene(next scene, opens if exec event)
        self._oldScreen
        self._nextScene = None
        self._scenes = {}
        self._gameObjects = []

    def BindSceneWithEvent(self, event, scene):
        self._scenes[event] = scene

    def GetNextScene(self):
        return (self._nextScene != None), self._nextScene

    def onEvent(self, event):
        if event in self._scenes:
            self._nextScene = self._scenes[event]
            pass
        else:
            print("undefined key({})".format(event))

    @abstractmethod
    def AddObject(self, obj):
        self._gameObjects.append(obj)
        return len(self._gameObjects)

    @abstractmethod
    def DeleteObject(self, idObject):
        self._gameObjects.remove(self._gameObjects[idObject])

    @abstractmethod
    def Update(self, screen, events):
        for obj in self._gameObjects:
            obj.Update(screen, events)

    @abstractmethod
    def Draw(self, screen):
        for obj in self._gameObjects:
            obj.Draw(screen)

    @abstractmethod
    def Enter(self):
        pass

    @abstractmethod
    def Leave(self):
        pass
