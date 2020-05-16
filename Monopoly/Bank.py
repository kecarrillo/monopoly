from Monopoly.Owner import Owner
from Monopoly.ClassManager.Singleton import Singleton


@Singleton
class Bank(Owner):
    def __init__(self):
        self.money = ...
        self.nb_house = ...
        self.nb_hotel = ...
