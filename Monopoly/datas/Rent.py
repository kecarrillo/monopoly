class Rent:
    """
    This class represents the rents.
    """

    def __init__(self, empty, house_1, house_2, house_3, house_4, hotel,
                 house_price, hotel_price):
        """This method is the constructor of the class.

        :param empty: Price of the empty buildable.
        :type empty: integer
        :param house_1: Price of the buildable with 1 house.
        :type house_1: integer
        :param house_2: Price of the buildable with 2 houses.
        :type house_2: integer
        :param house_3: Price of the buildable with 3 houses.
        :type house_3: integer
        :param house_4: Price of the buildable with 4 houses.
        :type house_4: integer
        :param hotel: Price of the buildable with 1 hotel.
        :type hotel: integer
        :param house_price: Price of 1 house.
        :type house_price: integer
        :param hotel_price: Price of 1 hotel.
        :type hotel_price: integer
        """

        self.empty = empty
        self.house_1 = house_1
        self.house_2 = house_2
        self.house_3 = house_3
        self.house_4 = house_4
        self.hotel = hotel
        self.hotel_price = hotel_price
        self.house_price = house_price
