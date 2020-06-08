from abc import ABCMeta, abstractmethod


class Owner(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, name, money):
        self.name = name
        self.money = money
