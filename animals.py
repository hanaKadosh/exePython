import abc
from abc import ABC, abstractmethod


class Animals(ABC):
    __name = ''

    def __init__(self):
        self.time = None

    def sleep(self, time=0):
        self.time = time
        print('sleep in houer :' + str(self.time))

    def makeSound(self, sound):
        self.sound = sound
        print(self.sound)

    @abc.abstractmethod
    def move(self):
        pass
