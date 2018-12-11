from abc import ABCMeta, abstractmethod

class Scene:
    __metaclass__ = ABCMeta

    def __init__(self):
        #key -> string(name event)
        #value Scene(next scene, opens if exec event)
        self._nextScene = None
        self._scenes = {}

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
    def AddObject(self, object):
        pass

    @abstractmethod
    def DeleteObject(self, idObject):
        pass

    @abstractmethod
    def Update(self, event, screen):
        pass

    @abstractmethod
    def Draw(self, screen):
        pass

    @abstractmethod
    def Enter(self):
        pass

    @abstractmethod
    def Leave(self):
        pass
