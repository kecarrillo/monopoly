from Monopoly.Owner import Owner
from Monopoly.ClassManager.Singleton import Singleton

from monopoly.Monopoly import Card, Game
from monopoly.Monopoly.datas import enum_buidable


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

    def launch_cell_actions(self, pawn, owner, rent, card):
        """
        This method launches different actions due to pawn position on the board.

        :param card: Instance of Card.
        :type card: Card
        :param pawn: The current position of the pawn.
        :type pawn: Pawn
        :param owner: The owner of the cell.
        :type owner: Owner
        :param rent: From the class rent we obtain the rent of the owned cell
        :type rent: Rent
        :return: Actions launched due to pawn position
        :rtype: void
        """
        community_cells = [2, 17, 33]
        chance_cells = [7, 22, 36]
        special_cells = [0, 10]
        free_park_cell = 20
        jail_cell = 30

        # For community_cells
        if pawn.position in community_cells:
            pawn.draw_card(card.deck_community)
        # For chance_cells
        elif pawn.position in chance_cells:
            pawn.draw_card(card.deck_chance)
        # For tax cell
        elif pawn.position == 4:
            pawn.give_money(20_000, owner)
        # For income cell
        elif pawn.position == 38:
            pawn.give_money(10_000, owner)
        # For special_cells
        elif pawn.position in special_cells:
            pass
        # For free_park_cells
        elif pawn.position in free_park_cell:
            self.give_money(self.money, pawn)
        # For jail_cells
        elif pawn.position in jail_cell:
            pawn.go_to_jail()
        # For ownership_cells
        else:
            for _ in enum_buidable:
                if owner is self.name:
                    pawn.buy_ownership()
                else:
                    rent(pawn, pawn.dice_result)
