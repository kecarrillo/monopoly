from abc import ABCMeta, abstractmethod
from random import shuffle

from Monopoly.Card import Card
from Monopoly.ClassManager.Singleton import Singleton
from Monopoly.Deck_Chance import Deck_Chance
from Monopoly.Deck_Community import Deck_Community

@Singleton
class Deck(metaclass=ABCMeta):
    """
    This class represents the abstract Deck object.
    """

    @abstractmethod
    def __init__(self):
        """
        This method is the class contructor.
        """
        self.cards = []
        self.make_cards()
        self.deck_community = Deck_Community()
        self.deck_chance = Deck_Chance()
        self.sort_deck()
        self.shuffle_deck()

    def make_cards(self):
        """
        This method instances cards.

        :return: Instances of cards.
        :rtype: void
        """
        i = 0
        for item in self.cards_list:
            self.cards.append(Card(i, item[0], item[1], item[2], item[3],
                                   item[4]))

    def sort_deck(self):
        """
        This method sort cards in decks.

        :return: Sorted decks.
        :rtype: void
        """
        for card in self.cards:
            if card.group == "community":
                self.deck_community.community_cards.append(card)
                card.owner = self.deck_community.community_cards
            else:
                self.deck_chance.chance_cards.append(card)
                card.owner = self.deck_chance.chance_cards

    def shuffle_deck(self):
        """
        This method shuffles decks.

        :return: Shuffled deck.
        :rtype: void
        """
        shuffle(self.deck_community.community_cards)
        shuffle(self.deck_chance.chance_cards)
