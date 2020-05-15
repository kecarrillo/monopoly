from Monopoly.Cell import Cell


class Ownership(Cell):

    def __init__(self, color, price, mortgage_price, group):
        super().__init__()
        self.color = color
        self.price = price
        self.mortgage_price = mortgage_price
        self.group = group

    def water_company_rent(self):
        pass

    def electricity_company_rent(self):
        pass

    def train_station_rent(self):
        pass
