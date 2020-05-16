from Monopoly.Ownership import Ownership


class Buildable(Ownership):

    def __init__(self, house_price, hotel_price):
        super().__init__()
        self.hotel_price = hotel_price
        self.house_price = house_price
        self.nb_house = 0
        self.nb_hotel = 0

    def get_monopoly(self):
        pass

    def get_house(self):
        pass

    def get_hotel(self):
        pass

    @classmethod
    def complex_rent( cls, name ):
        pass

    @classmethod
    def simple_empty_rent( cls, name ):
        pass
