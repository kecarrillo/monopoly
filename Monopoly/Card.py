# Create a Card class which contains actions launched
# when a pawn draws a community or chance card
import random
from monopoly.Monopoly.Pawn import Pawn
from Monopoly.Game import Game


class Card:
    """
        This class represents the card of chance and community cards.
    """

    # Constructor
    def __init__(self, name, action_group, group, sentence, amount_1, amount_2):
        """

        :param name:
        :param action_group:
        :param group: It represents the Chance and Community group cards
        :param sentence:
        :param amount_1:
        :param amount_2:
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
        random.shuffle(self.deck_chance)
        random.shuffle(self.deck_community)

    # Sort cards
    def sorting_card(self):
        """This method sort cards into community and luck pack.

        :return:
        :rtype: void
        """
        if self.group == "chance":
            self.deck_chance.append(self)
            self.owner = self.deck_chance
        else:
            self.deck_community.append(self)
            self.owner = self.deck_community

    def action(self, action_group, amount_1, amount_2, owner, pawn):
        """This method will determine the action to process depending on Game call

        :param pawn:
        :param owner:
        :param action_group:
        :param amount_1:
        :param amount_2:
        :return:
        :rtype: void
        """
        if action_group == "bill":
            self.pay_bill(amount_1, owner)
        elif action_group == "back":
            self.move_back()
        elif action_group == "forward":
            self.move_forward()
        elif action_group == "costs":
            self.repair()
        elif action_group == "jail":
            self.go_to_jail(pawn)
        elif action_group == "releasing":
            self.receive_free_card(pawn)
        elif action_group == "earnings":
            self.get_money()
        elif action_group == "choice":
            self.draw_chance(pawn)
        elif action_group == "birthday":
            self.anniversary(pawn)

    def pay_bill(self, pawn, amount_1):
        """ This method will pay bill from the pawn to Board or Bank

        :param pawn:
        :param amount_1:
        :param owner: Board or Bank
        :return: Give money
        """
        pawn.give_money(amount_1, Game.bank)

    def move_back(self):
        pass

    def move_forward(self):
        pass

    @staticmethod
    def receive_free_card(pawn):
        pass

    @staticmethod
    def go_to_jail(pawn):
        """ This method sends the player in jail

        :param pawn:
        :return:
        """
        pawn.go_to_jail()

    @staticmethod
    def anniversary(pawn):
        """ This method forces party players to give a gift

        :param pawn: The pawn who celebrates his birthday
        :return:
        """
        anniversary_amount = 30
        money_gift = 0
        for pawn in Game:
            money_gift += pawn.give_money(anniversary_amount)
        pawn.get_money(money_gift)

    def draw_chance(self, pawn):
        """ This method allows the pawn to choose to draw a card in Chance deck

        :param pawn:
        :return:
        """
        pawn.draw_card(self.deck_chance)

    @staticmethod
    def repair(pawn):
        """ This method will calculate the cost of repairing depending of the number of house and hotel, the pawn owns

        :param pawn:
        :return:
        """
        cost = 0
        for real_estate in pawn.ownership:
            if real_estate.nb_house > 0:
                cost += real_estate.nb_house * 600
            if real_estate.nb_hotel > 0:
                cost += real_estate.nb_hotel * 1500
        cost
        pawn.give_money(cost, Game.board)

