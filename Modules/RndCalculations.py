import math
import random as rnd


def Start():
    print('here is some useless math:')
    rnd.randint(1, 50)
    number = rnd.randint(5, 15)
    print('Number:', number)
    print('{0}! = {1}'.format(number, math.factorial(number)))
    print('{0}^2 = {1}'.format(number, number ** 2))
    print('log({0}) = {1}'.format(number, math.log10(number)))