import random
from Monopoly.Pawn import Pawn


def roll_dice():  # Roll dices
    dice_1 = random.randrange(6)
    dice_2 = random.randrange(6)
    return dice_1, dice_2


def check_rolls():  # Check results
    double = 0

    dice_1, dice_2 = roll_dice()
    result = dice_1 + dice_2

    Pawn.moving(result)
    if dice_1 == dice_2:
        if double < 3:
            roll_dice()
            double += 1
        else:  # go to jail
            pass
    Pawn.turn += 1


class Board:
    cell_number = 40
    money = 0
    pawn = 0
