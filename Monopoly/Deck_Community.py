from Monopoly.ClassManager.Singleton import Singleton
from Monopoly.Deck import Deck


@Singleton
class Deck_Community(Deck):
    """
    This class represents the deck community.
    """

    def __init__(self):
        """
        This method is the class contructor.
        """
        super().__init__()
        self.community_cards = []
