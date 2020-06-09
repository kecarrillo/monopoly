"""
This class generates auctions.
"""
from time import perf_counter
from operator import itemgetter

from Monopoly.Exceptions.TimerError import TimerError


class Auction:
    """
    This class represents an auction.
    """

    def __init__(self, ownership, owner, min_bid=0, time_up=10):
        """
        This method is the constructor of the class.

        :param ownership: Ownership to bid.
        :type ownership: Ownership
        :param owner: Original owner of the ownership.
        :type owner: Owner
        :param min_bid: Amount where begin the bids.
        :type min_bid: integer
        :param time_up: Second before validate the last bid.
        :type time_up: integer
        """
        self.bids = {}
        self.ownership = ownership
        self.owner = owner
        self.min_bid = min_bid
        self.time_up = time_up
        self.start_auction = None
        self.start()

    def __del__(self):
        """This method destroy the auction."""
        print("L'enchère est terminée.")

    def make_bid(self, pawn, bid):
        """
        This method allows pawns to make bids.

        :param pawn: Pawn which makes a bid.
        :type pawn: Pawn
        :param bid: Amount of the bid.
        :type bid: integer
        :return: Allows pawns to make a bid.
        :rtype: string
        """
        if bid > self.min_bid:
            self.stop()
            self.min_bid = bid
            self.bids[pawn] = bid
            print(f'{pawn} a surenchérit.\n'
                  f'{self.ownership} est maintenant à {bid} francs!')
            self.start()
        else:
            print(f'L\'enchère est inférieure au montant de '
                  f'l\'enchère actuelle!')

    def start(self):
        """Start a new timer, and stop it if the time is up.

        :return: start the timer. If it's a times up, run the stop() method.
        :rtype: void
        :raise TimeError: If the timer is not None.
        """
        if self.start_auction is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self.start_auction = perf_counter()

        print("Enchérissez!")

        elapsed_time = perf_counter() - self.start_auction
        if elapsed_time == self.time_up:
            self.stop(True)

    def stop(self, times_up=False):
        """Stop the timer, and report the elapsed time.

        :param times_up: Is it a times up?
        :type times_up: boolean
        :return: stop the timer. If it's a times up, makes the necessary
        actions.
        :rtype: void
        :raise TimeError: If the timer is not None.
        """
        if self.start_auction is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        self.start_auction = None

        # If it's a times up:
        if times_up is True:
            # If the dictionary bids is empty:
            if bool(self.bids) is False:
                self.__del__()
            else:
                new_owner = max(self.bids.iteritems(), key=itemgetter(1))[0]
                self.ownership.owner = new_owner
                self.owner.possessions.remove(self.ownership)
                new_owner.possessions.append(self.ownership)
                new_owner.give_money(self.min_bid, self.owner)
                self.__del__()
