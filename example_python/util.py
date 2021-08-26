'''
Example utilities module.
'''
import random

def get_integer(minimum:int = 0, maximum:int = 10) -> int:
    '''
    Gets a random integer.
    '''
    return random.randint(minimum, maximum)
