from Monopoly.Owner import Owner
from Monopoly.ClassManager.Singleton import Singleton


@Singleton
class Board(Owner):
    """
    This class represents the board game (unique owner).
    """
    def __init__(self, name, money):
        """This method is the constructor of the class.

        :param name: Name of the board game.
        :type name: string
        :param money: Money possessed by the board game.
        :type money: integer
        """
        super().__init__(name, money)
        self.name = name
        self.cell_number = 40
        self.money = money
        self.pawn = 0
