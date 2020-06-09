"""
This class creates chance and community cards
"""
from Monopoly.Game import Game


class Card:
    """
        This class represents the card of chance and community cards.
    """

    # Constructor
    def __init__(self, name, action_group, group, sentence, amount_1,
                 amount_2=None):
        """

        :param name: Name of the card.
        :type name: string
        :param action_group: Action when chance or community card is drown.
        :type action_group: string
        :param group: It is chance or community deck.
        :type group: string
        :param sentence: The rule of the card.
        :type sentence: string
        :param amount_1: First variable of the rule.
        :type amount_1: integer
        :param amount_2: Second variable of the rule.
        :type amount_2: integer
        """
        self.name = name
        self.action_group = action_group
        self.group = group
        self.sentence = sentence
        self.amount_1 = amount_1
        self.amount_2 = amount_2
        self.deck_community = []
        self.deck_chance = []
        self.sorting_card()

        # Sort cards

    def sorting_card(self):
        """This method sort cards into community and luck pack.

        :return: Sort cards in the right deck.
        :rtype: void
        """
        if self.group == "chance":
            self.deck_chance.append(self)
            self.owner = self.deck_chance
        else:
            self.deck_community.append(self)
            self.owner = self.deck_community

    def action(self, action_group, amount_1, owner, pawn, amount_2=None):
        """This method will determine the action to process depending on Game
        call.

        :param pawn: The current player.
        :type pawn: Pawn
        :param owner: The "receiver" of the payment.
        :type owner: Owner
        :param action_group: The type of actions.
        :type action_group: string
        :param amount_1: First variable of the rule's card.
        :type amount_1: integer
        :param amount_2: Second variable of the rule's card (default = None).
        :type amount_2: integer
        :return: Defines the rules action.
        :rtype: void
        """
        if action_group == "bill":
            self.pay_bill(amount_1, owner)
        elif action_group == "back":
            self.move_back()
        elif action_group == "forward":
            self.move_forward()
        elif action_group == "repair":
            self.repair(pawn, amount_1, amount_2, owner)
        elif action_group == "jail":
            self.go_to_jail(pawn)
        elif action_group == "free":
            self.receive_free_card(pawn)
        elif action_group == "earnings":
            self.get_money()
        elif action_group == "choice":
            self.draw_chance(pawn, amount_1, owner)
        elif action_group == "birthday":
            self.anniversary(pawn, Game.pawns, amount_1)

    def pay_bill(self, amount_1, pawn, owner):
        """ This method will pay bill from the pawn to Board or Bank

        :param pawn: The current player.
        :type pawn: Pawn
        :param amount_1: The amount of the bill.
        :type amount_1: integer
        :param owner: Board or Bank.
        :type owner: Owner
        :return: Give money
        :rtype: void
        """
        pawn.give_money(amount_1, owner)

    def move_back(self, pawn, amount_1):
        """
        This method makes the pawn move back on the board.
        :param pawn: The current player.
        :type pawn: Pawn
        :param amount_1: Number of cases to move back.
        :type amount_1: integer
        :return: Makes the pawn move back on the board.
        :rtype: void
        """
        if pawn.position >= amount_1:
            pawn.position = pawn.position - amount_1
        else:
            pawn.position = pawn.position + (39 - amount_1)

    def move_forward(self, pawn, amount_1):
        """
        This method makes the pawn move forward on the board.
        :param pawn: The current player.
        :type pawn: Pawn
        :param amount_1: Number of cases to move forward.
        :type amount_1: integer
        :return: Makes the pawn move forward on the board.
        :rtype: void
        """
        if pawn.position + amount_1 <= 39:
            pawn.position = pawn.position + amount_1
        else:
            pawn.position = (pawn.position + amount_1) - 39

    def receive_free_card(self, pawn):
        """
        This method gives a free card to deliver from jail to a pawn.
        :param self: The drown free card.
        :type self: Card
        :param pawn: The current player.
        :type pawn: Pawn
        :return: Change the owner of the free card
        :rtype: void
        """
        self.owner = pawn.form

    @staticmethod
    def go_to_jail(pawn):
        """ This method sends the pawn in jail.

        :param pawn: The current player.
        :type pawn: Pawn
        :return: Calls the method "go_to_jail()" from Pawn
        .. seealso:: Pawn.go_to_jail()
        """
        pawn.go_to_jail()

    @staticmethod
    def anniversary(pawn, pawns, amount_1):
        """ This method forces party players to give a gift.

        :param pawns: List of pawns in game.
        :type pawns: List
        :param amount_1: Amount to give to the pawn who draws this card.
        :type amount_1: integer
        :param pawn: The pawn who celebrates his birthday.
        :type pawn: Pawn
        :return: Pays the pawn who draws this card.
        :rtype: void
        """
        for element in pawns:
            if element is not pawn:
                element.give_money(amount_1)

    def draw_chance(self, pawn, amount_1, owner):
        """ This method allows the pawn to choose to draw a card in Chance deck.


        :param pawn: The pawn who chooses to draw another card in Chance desk.
        :type pawn: Pawn
        :param amount_1: The amount of the rule.
        :type amount_1: integer
        :param owner: where goes the money.
        :type owner: Owner
        :return: The pawn draws a chance card or pay the bill.
        """
        choice = input("1: Payer la facture.\n2: Tirer une carte chance.")
        if choice == "1":
            pawn.give_money(amount_1, owner)
        else:
            pawn.draw_card(self.deck_chance)

    @staticmethod
    def repair(pawn, amount_1, amount_2, owner):
        """ This method will calculate the cost of repairing depending of the number of houses and hotels, the pawn
        owns.

        :param pawn: The pawn .
        :type pawn: Pawn
        :param amount_1: The cost by house.
        :type amount_1: integer
        :param amount_2: The cost by hotel.
        :type amount_2: integer
        :param owner: The one who receives the amount of repairing.
        :type owner: Owner
        :return: Makes the pawn pay the bill.
        :rtype: void
        """
        cost = 0
        for real_estate in pawn.ownership:
            if real_estate.nb_house > 0:
                cost += real_estate.nb_house * amount_1
            if real_estate.nb_hotel > 0:
                cost += amount_2
        pawn.give_money(cost, owner)
