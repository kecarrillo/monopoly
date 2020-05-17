from Monopoly.Owner import Owner
from Monopoly.ClassManager.Singleton import Singleton


@Singleton
class Bank(Owner):
    """This class represents the bank (unique owner).
    """
    def __init__(self, name, money, nb_house, nb_hotel):
        """This method is the constructor of the class.

        :param name: Name of the bank.
        :type name: string
        :param money: Money of the bank.
        :type money: integer
        :param nb_house: Houses possessed by the bank.
        :type nb_house: integer
        :param nb_hotel: Hotel possessed by the bank.
        :type nb_hotel: integer
        """
        super().__init__(name, money)
        self.money = money
        self.nb_house = nb_house
        self.nb_hotel = nb_hotel
