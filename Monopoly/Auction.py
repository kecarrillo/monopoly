class Auction:

    def __init__(self, ownership, pawn):
        self.time_up = 10
        self.bids = {}
        self.ownership = ownership
        self.original_owner = pawn


