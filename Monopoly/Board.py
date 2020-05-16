from Monopoly.Owner import Owner
from Monopoly.ClassManager.Singleton import Singleton


@Singleton
class Board(Owner):
    cell_number = 40
    money = 0
    pawn = 0
