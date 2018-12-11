from abc import ABCMeta, abstractmethod

class GameObject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def Update(self, event, screen):
        pass

    @abstractmethod
    def Draw(self, screen):
        pass
