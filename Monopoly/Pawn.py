import random

# from Monopoly.Bank import Bank
from Monopoly.Phase import Phase


class Pawn:

    def __init__(self, form):
        print(f'{self.form} créé.')
        self.form = form
        self.position = 0
        self.turn = 0
        self.money = 150_000
        self.jail_time = 0
        self.free_card = 0

    def salary(self):
        """
        Method to get salary.
        :return: void
        .. todo:: Adding money limits
        """
        # Bank.money = Bank.money - 20_000
        self.money = self.money + 20_000

    def roll_dice(self):  # Roll dices
        double = 0
        dice_1 = random.randrange(6)
        dice_2 = random.randrange(6)
        if dice_1 == dice_2:
            double += 1
            if double == 3:
                self.go_to_jail()
        self.position = self.position + dice_1 + dice_2
        if self.position > 39:
            Phase.through_start_cell()
            self.position = self.position - 40
        Phase.cell_phase(self.position)

    def get_money(self):
        pass

    def give_money(self):
        pass

    def is_penniless(self):
        pass

    def is_jailed( self ):
        pass


    # # To win money
    # def win_money(self, money):
    #     self.money = self.money + money
    #
    # # To pay
    # def pay(self, money, optional):
    #     remaining_money = self.money - money
    #     if remaining_money >= 0:
    #         self.money = remaining_money
    #         return True
    #     elif remaining_money < 0 and optional == "optional":
    #         print( "Impossible de payer cette somme." )
    #         return False
    #     elif remaining_money < 0 and optional == "mandatory":
    #         if self.mortgage(item) == True:
    #             self.pay( money, optional )
    #         else:
    #             print("Vous avez perdu!")
    #
    # # To buy item
    # def buying(self):
    #     name = Item.name
    #     self.pay(Item.price, optional)
    #
    # def bail(self):
    #     paid = self.pay(5_000, "optional")
    #     if paid:
    #         return True
    #     else:
    #         return False
    #
    # # To mortgage
    # def mortgage(item):
    #     pass
    #
    # # To free parc
    # def to_parc( self ):
    #     if self.position == 20:
    #         self.win_money(Board.money)
    #     Pawn.turn += 1
    #
    # # To jail
    # def to_jail(self):
    #     self.position = 10
    #     if 0 < self.jail_time < 4:
    #         dice_1, dice_2 = bd.roll_dice()
    #         if dice_1 == dice_2:
    #             result = dice_1 + dice_2
    #             self.moving(result)
    #         self.jail_time += 1
    #         self.turn += 1
    #     elif self.jail_time > 3:
    #         self.jail_time = 0
    #         bd.check_rolls()
    #     elif self.free_card > 0:
    #         self.free_card -= 1
    #         self.jail_time = 4
    #         self.turn += 1
    #     elif self.bail():
    #         self.jail_time = 4
    #         self.turn += 1
    #     else:
    #         self.turn += 1
    #
    # # Movement
    # def moving(self, result):
    #     self.position = self.position + result
    #     if self.position > 39:
    #         self.win_money(20_000)
    #         self.position = self.position - 40
    #         if self.position == 0:
    #             self.win_money(20_000)
    #     self.turn += 1
