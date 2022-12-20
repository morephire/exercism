"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(minutes:int) -> int:
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_time = EXPECTED_BAKE_TIME - minutes
    return remaining_time


def preparation_time_in_minutes(layers):
    """Return layers per preparation time.

    :param layers: int - number of layers
    :return: int - numbers of layer multiplied preparation time

    This function tike the number of layers and multiplies it for the preparation time
    which is 2 minutes per layer.
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Return elapsed cooking time.

    :param number_of_layers: int - number of layers
    :param elapsed_bake_time: int - time spent baking
    :return: int - time per minute of preparation for a layer plus time in oven

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time
    