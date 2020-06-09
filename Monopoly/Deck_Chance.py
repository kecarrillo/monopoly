from Monopoly.ClassManager.Singleton import Singleton
from Monopoly.Deck import Deck


@Singleton
class Deck_Chance(Deck):
    """
    This class represents the deck chance.
    """

    def __init__(self):
        """
        This method is the class contructor.
        """
        super().__init__()
        self.chance_cards = []
