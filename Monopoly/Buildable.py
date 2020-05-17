from Monopoly.Ownership import Ownership


class Buildable(Ownership):
    """
    This class represents the buildable ownerships.
    """

    def __init__(self, name, position, color, group, mortgage_price, price,
                 is_expansive, rent):
        """This method is the constructor of the class.

        :param name: Name of the buildable.
        :type name: string
        :param position: Position of the buildable.
        :type position: integer
        :param color: Color of the ownership.
        :type color: string
        :param group: Group which contains this ownership.
        :type group: string
        :param mortgage_price: Amount gained with mortgaging this ownership.
        :type mortgage_price: integer
        :param price: Price of this ownership.
        :type price
        :param is_expansive: Cheaper or not?
        :type is_expansive: boolean
        :param rent: Rent of the ownership.
        :type rent: Rent
        """
        super().__init__(name, position, color, price, mortgage_price, group)
        self.nb_house = 0
        self.nb_hotel = 0
        self.is_expansive = is_expansive
        self.rent = rent

    def complex_rent(self):
        """This method return the rent if the buildable is empty and the group
        is a monopoly or if there are some houses or a hotel on this buildable.

        :return: Cost of the rent.
        :rtype: integer
        """
        if self.nb_house == 0 and self.nb_hotel == 0:
            if self.is_expansive:
                amount = self.rent.expansive("empty") * 2
                return amount
            else:
                amount = self.rent.empty * 2
                return amount
        elif self.nb_house == 1:
            if self.is_expansive:
                amount = self.rent.expansive("house_1")
                return amount
            else:
                amount = self.rent.house_1
                return amount
        elif self.nb_house == 2:
            if self.is_expansive:
                amount = self.rent.expansive("house_2")
                return amount
            else:
                amount = self.rent.house_2
                return amount
        elif self.nb_house == 3:
            if self.is_expansive:
                amount = self.rent.expansive("house_3")
                return amount
            else:
                amount = self.rent.house_3
                return amount
        elif self.nb_house == 4:
            if self.is_expansive:
                amount = self.rent.expansive("house_4")
                return amount
            else:
                amount = self.rent.house_4
                return amount
        else:
            if self.is_expansive:
                amount = self.rent.expansive("hotel")
                return amount
            else:
                amount = self.rent.hotel
                return amount

    def simple_empty_rent(self):
        """This method return the rent if the buildable is empty and the group
        is not a monopoly.

        :return: Cost of the rent.
        :rtype: integer
        """
        if self.is_expansive:
            amount = self.rent.expansive("empty")
            return amount
        else:
            amount = self.rent.empty
            return amount
