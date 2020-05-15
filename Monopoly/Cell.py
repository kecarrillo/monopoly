from Monopoly.Game import Game


class Cell:
    """
    This class represents the cells from the board game.
    """
    def __init__(self, position, name, group):
        """This method is the constructor of the class.

        :param position: Position of the cell on the board.
        :type position: integer
        :param name: Name of the cell.
        :type name: string
        :param group: Group of the cell: buildable, chance, community,
        train station, company, cop, free park, other.
        :type group: string
        """
        self.position = position
        self.name = name
        self.owner = Game.board
        self.group = group

    @staticmethod
    def pay_a_rent(pawn, ownership):
        """This method make a pawn pay for a rent.

        :param pawn: Instance of Pawn which is on the position.
        :type pawn: Pawn
        :param ownership: Instance of Ownership which lay on the position.
        :type ownership: Ownership
        :return: The rent is paid to the owner.
        :rtype: void
        """
        if ownership.is_mortgaged is False and ownership.owner != pawn.form:
            pawn.give_money(ownership.rent(), ownership.owner)
        elif ownership.owner == Game.board:
            pawn.buy_ownership()
        else:
            pass

    @staticmethod
    def luxury_tax_rent(pawn):
        """This method applies the action when the pawn is on the cell
        "luxury tax".

        :param pawn: Instance of Pawn which is on the cell.
        :type pawn: Pawn
        :return: Pay the bank.
        :rtype: void
        """
        pawn.give_money(10_000, Game.bank)

    @staticmethod
    def income_tax_rent(pawn):
        """This method applies the action when the pawn is on the cell
        "Income tax".

        :param pawn: Instance of Pawn which is on the cell.
        :type pawn: Pawn
        :return: Pay the bank.
        :rtype: void
        """
        pawn.give_money(20_000, Game.bank)

    @staticmethod
    def free_park(pawn):
        """This method applies the action when the pawn is on the cell
        "Free park".

        :param pawn: Instance of Pawn which is on the cell.
        :type pawn: Pawn
        :return: The pawn earn the money of the board.
        :rtype: void
        """
        pawn.get_money(Game.board.money)

    @staticmethod
    def cop_cell(pawn):
        """This method applies the action when the pawn is on the cell
        "Go to jail".

        :param pawn: Instance of Pawn which is on the cell.
        :type pawn: Pawn
        :return: Send the pawn to jail.
        :rtype: void
        """
        pawn.go_to_jail()
