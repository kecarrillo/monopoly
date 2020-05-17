import random

# from Monopoly.Bank import Bank
# from Monopoly.Card import Card
from Monopoly.Owner import Owner
from Monopoly.WIP.Phase import Phase
# from Monopoly.Auction import Auction


class Pawn(Owner):
    """
    This class represents the avatar of the players.
    """

    def __init__(self, name, money):
        """This method is the constructor of the class.

        :param form: Form of the pawn.
        :type form: string
        :return: create a pawn.
        :rtype: string
        """
        super().__init__(name, money)
        print(f'{self.form} créé.')
        self.form = name
        self.position = 0
        self.turn = 0
        self.money = money
        self.jail_time = 0
        self.free_card = 0
        self.double = 0
        self.debt = 0

    def __del__(self):
        """This method is the destructor of the class.

        :return: String
        :rtype: void
        """
        print(f"Suppression de {self.form}.")

    def salary(self):
        """
        Method to get salary.
        :return: void
        .. todo:: Adding money limits
        """
        # Bank.money = Bank.money - 20_000
        self.money = self.money + 20_000

    def roll_dice(self):  # Roll dices
        """This method rolls 2 dices.

        .. todo:: Phase encore d'actualité?
        :return: Roll dices.
        :rtype: void
        """
        dice_1 = random.randrange(1, 6)
        dice_2 = random.randrange(1, 6)
        if self.jail_time < 1:
            if dice_1 == dice_2:
                self.double += 1
                if self.double == 3:
                    self.go_to_jail()
                else:
                    self.position = self.position + dice_1 * 2
                    if self.position > 39:
                        self.salary()
                        self.position = self.position - 40
                    Phase.cell_phase(self.position)
                    self.roll_dice()
            else:
                self.position = self.position + dice_1 + dice_2
                if self.position > 39:
                    self.salary()
                    self.position = self.position - 40
                Phase.cell_phase(self.position)
        else:
            self.is_jailed(dice_1, dice_2)
            self.jail_time += 1
            self.turn += 1

    def get_money(self, amount):
        """This method allows the pawn to receive money.

        :param amount: Money to receipt.
        :type amount: integer
        :return: Receipt money.
        :rtype: void
        """
        self.money = self.money + amount

    def give_money(self, amount, owner):
        """This method allows the pawn to spend money.

        :param amount: Money to give.
        :type amount: integer
        :param owner: Owner of the payment.
        :type owner: Owner
        :return: Give money.
        :rtype: void
        """
        self.money = self.money - amount
        owner.money = owner.money + amount

    def go_to_jail(self):
        """This method is used when a pawn go to jail.

        :return: Buying ownership.
        :rtype: void
        """
        self.position = 10
        if self.free_card > 0:
            self.free_card -= 1
            self.turn += 1
        else:
            self.jail_time = 1
            self.turn += 1

    def freed_from_jail(self):
        """This method is used when the pawn is freed from jail.

        :return: ... .
        :rtype: void
        """
        self.jail_time = 0

    def is_jailed(self, dice_1, dice_2):
        """This method allows the pawn to make some action in jail.

        .. todo:: declarer la banque.
        :return: Buying ownership.
        :rtype: void
        """
        bank = ...
        if dice_1 == dice_2:
            self.position = self.position + dice_1 * 2
            self.jail_time = 0
            self.roll_dice()
        if self.give_money(5_000, bank):
            self.jail_time = 0
            self.roll_dice()

    def is_penniless(self, creditor, buildables, give_up=False):
        """This method is used when the money's pawn is below 0.

        :param creditor: The creditor of the pawn.
        :type creditor: Owner
        .. todo:: list n'est pas apprécié ici
        :param buildables: The Buildable of the player
        :type list
        :param give_up: If the pawn give up the game.
        :type give_up: boolean
        :return: Message.
        :rtype: string
        """
        amount = 0
        for buildable in buildables:
            if buildable.nb_hotel > 0:
                amount += (buildable.hotel_price / 2) + \
                          ((buildable.house_price / 2) * 4)
            if buildable.nb_house > 0:
                amount += (buildable.house_price / 2) * buildable.nb_house
            amount += buildable.mortgage_price
        amount += self.money
        if amount < 0:
            print(f'{self.form} est ruiné!')
            self.give_money(amount, creditor)
        elif give_up is True:
            print(f'{self.form} abandonne!')
            self.give_money(amount, creditor)
        else:
            print("Rien n'est joué!")

    def give_up(self, creditor, buildables):
        """This method is used when a player wants to give up the game.

        :return: End of the game for the player
        :rtype: string
        """
        self.is_penniless(creditor, buildables, True)

    def buy_ownership(self, ownership, owner):
        """This method allows the pawn to buy an ownership.

        :param owner: The owner of the ownership.
        :type owner: Owner
        :param ownership: The ownership.
        :type ownership: Ownership
        :return: Buying ownership.
        :rtype: void
        """
        amount = ownership.price
        self.give_money(amount, owner)
        ownership.owner = self.form

    def buy_house(self, color, buildable, owner):
        """This method allows the pawn to buy a house.

        :param owner: The bank.
        :type owner: Owner
        :param color: Color object which organize the ownerships.
        :type buildable: Color
        :param buildable: Ownership with a price.
        :type buildable: Buildable
        :return: Buying house.
        :rtype: void
        """
        if color.name is "colorless":
            print("Ce terrain ne peut pas possèder de maison!")
        else:
            if buildable.owner is not self.form:
                print("Vous devez être le propriétaire du terrain pour acheter"
                      " des maisons!")
            else:
                max_house = color.nb_house // color.nb_buildable
                if max_house == buildable.nb_house:
                    amount = buildable.house_price
                    self.give_money(amount, owner)
                    buildable.nb_house += 1
                elif max_house == 4:
                    print("Nombre maximal de maison atteinte!")
                else:
                    print("Le nombre de maison sur les terrains de même "
                          "couleurs doivent être identiques!")

    def buy_hotel(self, color, buildable, owner):
        """This method allows the pawn to buy a hotel.

        :param owner: The bank.
        :type owner: Owner
        :param color: Color object which organize the ownerships.
        :type buildable: Color
        :param buildable: Ownership with a price.
        :type buildable: Buildable
        :return: Buying hotel.
        :rtype: void
        """
        if buildable.owner is not self.form:
            print("Vous devez être le propriétaire du terrain pour acheter"
                  " un hotel!")
        else:
            max_house = color.nb_house // color.nb_buildable
            if max_house == 4 and buildable.nb_hotel < 1:
                amount = buildable.hotel_price
                self.give_money(amount, owner)
                buildable.nb_hotel += 1
                buildable.nb_house = 0
            elif max_house == 4 and buildable.nb_hotel > 0:
                print("Vous ne pouvez construire qu'un seul hotel par "
                      "terrain!")
            else:
                print("Vous ne possèdez pas le nombre de maisons requises!")

    def sell_hotel(self, buildable):
        """This method allows the pawn to sell a hotel he possess.

        :param buildable: Ownership with a price.
        :type buildable: Buildable
        :return: Selling hotel.
        :rtype: void
        """
        if buildable.owner is not self.form:
            print("Vous devez être le propriétaire du terrain pour vendre"
                  " un hotel!")
        else:
            if buildable.nb_hotel == 1:
                amount = (buildable.hotel_price / 2) + \
                         ((buildable.house_price / 2) * 4)
                self.get_money(amount)
                buildable.nb_hotel = 0
            else:
                print("Vous ne pouvez vendre que si vous possèdez un hotel!")

    def sell_house(self, color, buildable):
        """This method allows the pawn to sell a house he possess.

        :param color: Color object which organize the ownerships.
        :type buildable: Color
        :param buildable: Ownership with a price.
        :type buildable: Buildable
        :return: Selling house.
        :rtype: void
        """
        if buildable.owner is not self.form:
            print("Vous devez être le propriétaire du terrain pour vendre"
                  " des maisons!")
        else:
            max_house = color.nb_house // color.nb_buildable
            if max_house == buildable.nb_house:
                amount = buildable.house_price / 2
                self.get_money(amount)
                buildable.nb_house -= 1
            elif buildable.nb_house == 0:
                print("Nombre maximal de maison vendues atteinte pour ce "
                      "terrain!")
            else:
                print("Le nombre de maison sur les terrains de même "
                      "couleurs doivent être identiques!")

    def make_mortgage(self, ownership):
        """This method is used to make mortgage.

        It permits the pawn to mortgage his ownership and to contract a debt.

        :param ownership: The ownership of the pawn.
        :type ownership: Ownership
        :return: Make the mortgage.
        :rtype: void
        """
        amount = ownership.mortgage_price
        self.get_money(amount)
        ownership.is_mortgaged = True
        self.debt += amount

    def refund_mortgage(self, ownership, owner):
        """This method is used for the refund of mortgage.

        It permits the pawn to catch back his ownership and be free of a debt.

        :param ownership: The ownership of the pawn.
        :type ownership: Ownership
        :param owner: The bank.
        :type owner: Owner
        :return: Refund the mortgage.
        :rtype: void
        """
        amount = ownership.mortgage_price + ownership.mortgage_price * 0.1
        self.give_money(amount, owner)
        ownership.is_mortgaged = False
        self.debt -= ownership.mortgage_price

    def draw_card(self, deck, retry=False):
        """This method allows the pawn to draw a card.

        .. todo:: Vérifier méthode action()

        :param deck: Instance of Card.
        :type deck: Card
        :param retry: When you choose to draw a card instead of paying.
        :type retry: boolean
        :return: Action of the drawn card.
        :rtype: void
        """
        community_fund_cells = [2, 17, 33]
        if self.position in community_fund_cells and retry is False:
            draw_card = deck.community_fund_cards.pop(0)
            draw_card.action()
            if draw_card.name is not "free_card":
                deck.community_fund_cards.append(draw_card)
            else:
                draw_card.owner = self.form
                self.free_card += 1
        elif self.position in community_fund_cells and retry is True:
            draw_card = deck.chance_cards.pop(0)
            draw_card.action()
            if draw_card.name is not "free_card":
                deck.chance_cards.append(draw_card)
            else:
                draw_card.owner = self.form
                self.free_card += 1
        else:
            draw_card = deck.chance_cards.pop(0)
            draw_card.action()
            if draw_card.name is not "free_card":
                deck.chance_cards.append(draw_card)
            else:
                draw_card.owner = self.form
                self.free_card += 1

    def auction_sale(self, possession):
        """This method allows the pawn to create an auction sale.
        .. todo:: Faire l'itération d'objet
        :param possession: The possession of the pawn.
        :type possession: Object
        :return: Alert.
        :rtype: string
        """
        if possession is not None:
            if possession.owner == self.form:
                print(f"{self.form} vend {possession} au plus offrant!")
            else:
                print("Vous devez être propriétaire du bien pour le mettre "
                      "aux enchères!")
        else:
            print("Une enchère doit mettre en jeu une possession!")

    def auction_bid(self, amount, possession):
        """ This method allows the pawn to make a bid in an auction sale.
        ... todo:: compléter la classe
        :param amount:
        :param possession:
        :return:
        """
        print(f"{self.form} enchérit à {amount}F pour {possession}!")
