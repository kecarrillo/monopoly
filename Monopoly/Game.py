# Règles suivies: http://monopolyste.online.fr/regles.shtml
from Monopoly.Datas.Enum_pawn import Pawns
from Monopoly.Exceptions.PawnsNumberError import PawnsNumberError


class Game:

    def __init__(self):
        self.available_pawns = []
        self.pawns = []
        self.nb_pawn = 0
        print("Création du Monoploy terminée.")

    def __del__(self):
        print("Fin du Monopoly.")

    def start_game(self):
        nb_pawn = int(input("Indiquez le nombre de joueurs (max: 6) : "))
        if nb_pawn < 2 or nb_pawn > 6:
            raise PawnsNumberError(f"Nombre de pions incorrect, saisissez un "
                                   f"nombre de joueur compris entre 2 et 6.")
        else:
            self.nb_pawn = nb_pawn

        for item in Pawns:
            self.available_pawns.append(item.name)

        for item in range(nb_pawn):


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
