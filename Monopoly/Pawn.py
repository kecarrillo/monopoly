import random

# from Monopoly.Bank import Bank
from Monopoly.WIP.Phase import Phase


class Pawn:

    def __init__(self, form):
        '''This method is the constructor of the class.

        :param form: Form of the pawn.
        :type form: string
        :return: create a pawn.
        :rtype: string
        '''
        print(f'{self.form} créé.')
        self.form = form
        self.position = 0
        self.turn = 0
        self.money = 150_000
        self.jail_time = 0
        self.free_card = 0
        self.double = 0
        self.debt = 0

    def __del__(self):
        '''This method is the destructor of the class.

        :return: String
        :rtype: void
        '''
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
        '''This method rolls 2 dices.

        :return: Roll dices.
        :rtype: void
        '''
        dice_1 = random.randrange(6)
        dice_2 = random.randrange(6)
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
            self.is_jailed()
            self.jail_time += 1
            self.turn += 1

    def get_money(self, amount):
        '''This method allows the pawn to receive money.

        :param amount: Money to receipt.
        :type amount: integer
        :return: Receipt money.
        :rtype: void
        '''
        self.money = self.money + amount

    def give_money(self, amount, owner):
        '''This method allows the pawn to spend money.

        :param amount: Money to give.
        :type amount: integer
        :param owner: Owner of the payment.
        :type owner: Owner
        :return: Give money.
        :rtype: void
        '''
        self.money = self.money - amount
        owner.money = owner.money + amount

    def go_to_jail(self, card):
        '''This method is used when a pawn go to jail.

        :return: Buying ownership.
        :rtype: void
        '''
        self.position = 10
        if self.free_card > 0:
            self.free_card -= 1
            self.turn += 1
        else:
            self.jail_time = 1
            self.turn += 1

    def freed_from_jail(self):
        '''This method is used when the pawn is freed from jail.

        :return: ... .
        :rtype: void
        '''
        self.jail_time = 0

    def is_jailed(self, owner, dice_1, dice_2):
        '''This method allows the pawn to make some action in jail.

        :return: Buying ownership.
        :rtype: void
        '''
        if dice_1 == dice_2:
            self.position = self.position + dice_1 * 2
            self.jail_time = 0
            self.roll_dice()
        if self.give_money(5_000, owner):
            self.jail_time = 0
            self.roll_dice()

    def is_penniless(self, creditor, rentals, give_up=False):
        '''This method is used when the money's pawn is below 0.

        :param creditor: The creditor of the pawn.
        :type creditor: Owner
        :param rentals: The Rental of the player
        :type list
        :return: Message.
        :rtype: string
        '''
        amount = 0
        for rental in rentals:
            if rental.nb_hotel > 0:
                amount += (rental.hotel_price / 2) + \
                          ((rental.house_price / 2) * 4)
            if rental.nb_house > 0:
                amount += (rental.house_price / 2) * rental.nb_house
            amount += rental.mortgage_price
        amount += self.money
        if amount < 0:
            print(f'{self.form} est ruiné!')
            self.give_money(amount, creditor)
        elif give_up is True:
            print(f'{self.form} abandonne!')
            self.give_money(amount, creditor)
        else:
            print("Rien n'est joué!")

    def give_up(self, creditor, rentals):
        '''This method is used when a player wants to give up the game.

        :return: End of the game for the player
        :rtype: string
        '''
        self.is_penniless(creditor, rentals, True)

    def buy_ownership(self, ownership, owner):
        '''This method allows the pawn to buy an ownership.

        :param owner: The owner of the ownership.
        :type owner: Owner
        :param ownership: The ownership.
        :type ownership: Ownership
        :return: Buying ownership.
        :rtype: void
        '''
        amount = ownership.price
        self.give_money(amount, owner)
        ownership.owner = self.form

    def buy_house(self, color, rental, owner):
        '''This method allows the pawn to buy a house.

        :param owner: The bank.
        :type owner: Owner
        :param color: Color object which organize the ownerships.
        :type rental: Color
        :param rental: Ownership with a price.
        :type rental: Rental
        :return: Buying house.
        :rtype: void
        '''
        if color.name is "colorless":
            print("Ce terrain ne peut pas possèder de maison!")
        else:
            if rental.owner is not self.form:
                print("Vous devez être le propriétaire du terrain pour acheter"
                      " des maisons!")
            else:
                max_house = color.nb_house // color.nb_rental
                if max_house == rental.nb_house:
                    amount = rental.house_price
                    self.give_money(amount, owner)
                    rental.nb_house += 1
                elif max_house == 4:
                    print("Nombre maximal de maison atteinte!")
                else:
                    print("Le nombre de maison sur les terrains de même "
                          "couleurs doivent être identiques!")

    def buy_hotel(self, color, rental, owner):
        '''This method allows the pawn to buy a hotel.

        :param owner: The bank.
        :type owner: Owner
        :param color: Color object which organize the ownerships.
        :type rental: Color
        :param rental: Ownership with a price.
        :type rental: Rental
        :return: Buying hotel.
        :rtype: void
        '''
        if rental.owner is not self.form:
            print("Vous devez être le propriétaire du terrain pour acheter"
                   " un hotel!")
        else:
            max_house = color.nb_house // color.nb_rental
            if max_house == 4 and rental.nb_hotel < 1:
                amount = rental.hotel_price
                self.give_money(amount, owner)
                rental.nb_hotel += 1
                rental.nb_house = 0
            elif max_house == 4 and rental.nb_hotel > 0:
                print("Vous ne pouvez construire qu'un seul hotel par "
                      "terrain!")
            else:
                print("Vous ne possèdez pas le nombre de maisons requises!")

    def sell_hotel(self, color, rental):
        '''This method allows the pawn to sell a hotel he possess.

        :param color: Color object which organize the ownerships.
        :type rental: Color
        :param rental: Ownership with a price.
        :type rental: Rental
        :return: Selling hotel.
        :rtype: void
        '''
        if rental.owner is not self.form:
            print("Vous devez être le propriétaire du terrain pour vendre"
                   " un hotel!")
        else:
            max_house = color.nb_house // color.nb_rental
            if rental.nb_hotel == 1:
                amount = (rental.hotel_price / 2) + \
                         ((rental.house_price / 2) * 4)
                self.get_money(amount)
                rental.nb_hotel = 0
            else:
                print("Vous ne pouvez vendre que si vous possèdez un hotel!")

    def sell_house(self, color, rental):
        '''This method allows the pawn to sell a house he possess.

        :param color: Color object which organize the ownerships.
        :type rental: Color
        :param rental: Ownership with a price.
        :type rental: Rental
        :return: Selling house.
        :rtype: void
        '''
        if rental.owner is not self.form:
            print("Vous devez être le propriétaire du terrain pour vendre"
                   " des maisons!")
        else:
            max_house = color.nb_house // color.nb_rental
            if max_house == rental.nb_house:
                amount = rental.house_price / 2
                self.get_money(amount)
                rental.nb_house -= 1
            elif rental.nb_house == 0:
                print("Nombre maximal de maison vendues atteinte pour ce "
                       "terrain!")
            else:
                print("Le nombre de maison sur les terrains de même "
                       "couleurs doivent être identiques!")

    def make_mortgage(self, ownership):
        '''This method is used to make mortgage.

        It permits the pawn to mortgage his ownership and to contract a debt.

        :param ownership: The ownership of the pawn.
        :type ownership: Ownership
        :param owner: The bank.
        :type owner: Owner
        :return: Make the mortgage.
        :rtype: void
        '''
        amount = ownership.mortgage_price
        self.get_money(amount)
        ownership.is_mortgaged = True
        self.debt += amount

    def refund_mortgage(self, ownership, owner):
        '''This method is used for the refund of mortgage.

        It permits the pawn to catch back his ownership and be free of a debt.

        :param ownership: The ownership of the pawn.
        :type ownership: Ownership
        :param owner: The bank.
        :type owner: Owner
        :return: Refund the mortgage.
        :rtype: void
        '''
        amount = ownership.mortgage_price + ownership.mortgage_price * 0.1
        self.give_money(amount, owner)
        ownership.is_mortgaged = False
        self.debt -= ownership.mortgage_price

    def draw_card(self):
        pass

    def auction_sale(self, ownership, card):
        if ownership is None and card is not None:
            pass
        elif ownership is not None and card is None:
            pass
        else:
            print("Une enchère doit mettre en jeu une possession!")

    def auction_bid(self):
        pass
