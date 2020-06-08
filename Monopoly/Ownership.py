from Monopoly.Buildable import Buildable
from Monopoly.Cell import Cell


class Ownership(Cell):
    """This class represents the ownership of the bank, the board and the pawn.
    """

    def __init__(self, name, position, color, price, mortgage_price, group):
        """This method is the constructor of the class.

        :param name: Name of the ownership.
        :param position: Position of the ownership on the board.
        :param color: Color of the ownership.
        :param price: Price of the ownership.
        :param mortgage_price: If mortgaged, how many will it give to the pawn.
        :param group: Group of the ownership.
        """
        super().__init__(position, name, group)
        self.color = color
        self.price = price
        self.mortgage_price = mortgage_price
        self.red_group = {}
        self.yellow_group = {}
        self.green_group = {}
        self.dark_blue_group = {}
        self.pink_group = {}
        self.orange_group = {}
        self.brown_group = {}
        self.light_blue_group = {}
        self.train_station_group = {}
        self.company_group = {}
        self.sort_group()
        self.groups = {"red": self.red_group,
                       "yellow": self.yellow_group,
                       "light_blue": self.light_blue_group,
                       "dark_blue": self.dark_blue_group,
                       "pink": self.pink_group,
                       "orange": self.orange_group,
                       "brown": self.brown_group,
                       "green": self.green_group,
                       "train_station": self.train_station_group,
                       "company": self.company_group}

    def sort_group(self):
        """Method to organize the ownership by group.

        :return: group of ownerships.
        :rtype: dict
        """
        if self.group == "red":
            self.red_group[self.name] = self.owner
        elif self.group == "yellow":
            self.yellow_group[self.name] = self.owner
        elif self.group == "green":
            self.green_group[self.name] = self.owner
        elif self.group == "dark_blue":
            self.dark_blue_group[self.name] = self.owner
        elif self.group == "pink":
            self.pink_group[self.name] = self.owner
        elif self.group == "orange":
            self.orange_group[self.name] = self.owner
        elif self.group == "brown":
            self.brown_group[self.name] = self.owner
        elif self.group == "light_blue":
            self.light_blue_group[self.name] = self.owner
        elif self.group == "train_station":
            self.train_station_group[self.name] = self.owner
        else:
            self.company_group[self.name] = self.owner

    def rent(self, pawn, dice_result):
        """This method return the amount of rent to pay.

        :param pawn: Pawn which arrive at the position.
        :type pawn: Pawn
        :param dice_result: Result of the dices.
        :type dice_result: integer
        :return: Amount to pay.
        :rtype: integer
        """
        # Companies
        if pawn.position == 38 or pawn.position == 13:
            monopoly = self.check_monopoly()
            amount = dice_result * 400
            if monopoly is True:
                amount *= 1_000
                return amount
        # Train stations
        elif pawn.position in [5, 15, 25, 35]:
            color_owners = self.groups[self.group].values()
            if len(color_owners) == color_owners.count(self.owner):
                amount = 20_000
                return amount
            elif color_owners.count(self.owner) == 3:
                amount = 15_000
                return amount
            elif color_owners.count(self.owner) == 2:
                amount = 10_000
                return amount
            else:
                amount = 5_000
                return amount
        # Buildables
        else:
            monopoly = self.check_monopoly()
            if monopoly is True:
                Buildable.complex_rent(self.name)
            else:
                Buildable.simple_empty_rent(self.name)

    def check_monopoly(self):
        """Method to check if a pawn has a color's monopoly.

        :return: Check if a pawn has a monopoly of the group.
        :rtype: boolean
        """
        color_owners = self.groups[self.group].values()
        if len(color_owners) == color_owners.count(self.owner):
            return True
        else:
            return False
