
import string
import random

def strArr(string):
    '''Creates the list from the text'''
    return [char for char in string]

def strGenerator(size, chars=string.ascii_letters+' '+'.'+','):
    '''Generate a random string'''
    return [random.choice(chars) for _ in range(size)]

def mutatesChar(chars=string.ascii_letters+' '):
    '''Return random char'''
    return random.choice(chars)