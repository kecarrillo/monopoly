# Règles suivies: http://monopolyste.online.fr/regles.shtml
from Monopoly.Datas.Enum_pawn import Pawns
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
        if nb_pawn < 2 or nb_pawn > 6:
            raise PawnsNumberError(f"Nombre de pions incorrect, saisissez un "
                                   f"nombre de joueur compris entre 2 et 6.")
        else:
            self.nb_pawn = nb_pawn

        for item in Pawns:
            self.available_pawns.append(item.value)

        for i in range(nb_pawn):

            self.players.append(f'player_{i}')

            pawn = input("Choisissez un pion parmi ceux-ci:\n"
                         f'{self.available_pawns}.')
            if pawn not in self.available_pawns:
                # TODO: Exception class
                raise PawnFormError("La forme choisie est indisponible.")
            else:
                self.available_pawns.remove(pawn)
                self.players[i] = Pawn(money=self.start_money, name=pawn)
                self.pawns.append(pawn)

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
