from Monopoly.Cell import Cell


class Ownership(Cell):
    """
    This class represents the ownership of the bank, the board and the pawn.
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

    def rent(self, pawn, dice_result):
        if pawn.position == 38:
            self.check_monopoly(self.group)
            amount = dice_result * 400
            return amount

    def check_monopoly(self, group):
        if 

    @staticmethod
    def water_company_rent(pawn, dice_1, dice_2):


    def electricity_company_rent(self):
        pass

    def train_station_rent(self):
        pass

    def buy_a_ownership(self):
        pass