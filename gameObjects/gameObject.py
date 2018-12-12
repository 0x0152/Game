from abc import ABCMeta, abstractmethod

class GameObject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def Update(self, screen, events):
        pass

    @abstractmethod
    def Draw(self, screen):
        pass
