# Règles suivies: http://monopolyste.online.fr/regles.shtml
from random import shuffle

from Monopoly.Bank import Bank
from Monopoly.Board import Board
from Monopoly.Datas.Enum_pawn import Pawns
from Monopoly.Exceptions.PawnFormError import PawnFormError
from Monopoly.Exceptions.PawnsNumberError import PawnsNumberError
from Monopoly.Pawn import Pawn


class Game:
    """
    This class represents a game of Monopoly.
    """

    def __init__(self):
        """
        This method is the constructor of the class.

        :return: Instance of Game.
        :rtype: string
        """
        self.available_pawns = []
        self.pawns = []
        self.nb_pawn = 0
        self.start_money = 150_000
        self.players = []
        print("Création du Monoploy terminée.")

    def __del__(self):
        """
        This method destruct this instance of Game.
        :return: Destroy the Game's instance.
        :rtype: void
        """
        print("Fin du Monopoly.")

    def start_game(self):
        """
        This method initialize the game.

        :return: Instances of Pawn, Board, Bank, Card.
        :rtype: void
        """
        nb_pawn = int(input("Indiquez le nombre de joueurs (max: 6) : "))
        if nb_pawn < 2 or nb_pawn > 7:
            raise PawnsNumberError("Nombre de pions incorrect, saisissez un "
                                   "nombre de joueur compris entre 2 et 6.")
        else:
            self.nb_pawn = nb_pawn

        for item in Pawns:
            self.available_pawns.append(item.value)

        for i in range(nb_pawn):

            self.players.append(f'player_{i}')

            pawn = input("Choisissez un pion parmi ceux-ci:\n"
                         f'{self.available_pawns}.')
            if pawn not in self.available_pawns:
                raise PawnFormError("La forme choisie est indisponible.")
            else:
                self.available_pawns.remove(pawn)
                self.players[i] = Pawn(money=self.start_money, name=pawn)
                self.players[i].position = 0
                self.pawns.append(pawn)

        if self.pawns is False:
            self.start_game()
        else:
            shuffle(self.pawns)
            print(f'Les pions avanceront dans cet ordre: {self.pawns}.')
            board = Board("board", 0)
            bank = Bank("bank", 10_000_000, 32, 12)

        # TODO: make a function to instance cards
        # if self.pawns is False:
        #     self.start_game()
        # else:
        #     card = Card(name, action_group, group, sentence, amount_1,
        #          amount_2=None)

    def make_cards(self, name, action_group, group, sentence, amount_1,
                 amount_2=None):
        """
        This method instances cards.

        :param name:
        :param action_group:
        :param group:
        :param sentence:
        :param amount_1:
        :param amount_2:
        :return:
        """



    # turn
    # pawn_number
    # phase
    #
    # random.shuffle(self.deck_chance)
    # random.shuffle(self.deck_community)
    #
    # def start_game(self):
    #     pass
    #
    # def end_game(self):
    #     pass
