# Règles suivies: http://monopolyste.online.fr/regles.shtml
from random import shuffle

from Monopoly.Bank import Bank
from Monopoly.Board import Board
from Monopoly.Datas.Enum_pawn import Pawns
from Monopoly.Datas.Data_cards import cards_list
from Monopoly.Deck import Deck
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
        self.cards_list = cards_list
        self.cards = []
        self.board = None
        self.bank = None
        self.deck = None
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
            self.board = Board("board", 0)
            self.bank = Bank("bank", 10_000_000, 32, 12)
            self.deck = Deck()

        self.turn()

    def end_game(self):
        self.__del__()

    def turn(self):
        """
        This method represents a turn.

        :return: A turn.
        :rtype: list
        """
        current_pawn = self.pawns.pop[0]
        self.phases(current_pawn)
        self.pawns.append(current_pawn)

    def phases(self, current_pawn):
        """
        This method represents game phases.

        :param current_pawn: Current pawn.
        :type current_pawn: Pawn
        :return: Game phases.
        :rtype: void
        """
        if len(self.pawns) == 1:
            self.end_game()
        current_pawn.roll_dice()
        self.board.launch_cell_actions(current_pawn, current_pawn.position)
        self.availbale_actions(current_pawn)


    def availbale_actions(self, current_pawn):
        """
        This method allows the pawn to make actions.

        :param current_pawn: Current pawn.
        :type current_pawn: Pawn
        :return: Actions of pawn.
        :rtype: void
        """
        choice = input("Quelle action souhaitez vous effectuer?\n"
                       "(1) Passer\n(2) Enchères\n(3) Acheter des maisons\n"
                       "(4) Acheter un hotel")
        if choice not in range(1,5):
            print("Erreur de saisie, veuillez choir un nombre entre 1 et 4.")
            self.availbale_actions(current_pawn)
        elif choice == 1:
            print(f'{current_pawn} a terminé son tour, c\'est au tour de '
                  f'{self.pawns[1]}.')
        elif choice == 2:
            current_pawn.auction_sale()
            self.availbale_actions(current_pawn)
        elif choice == 3:
            current_pawn.buy_house()
            self.availbale_actions(current_pawn)
        elif choice == 4:
            current_pawn.buy_hotel()
            self.availbale_actions(current_pawn)
