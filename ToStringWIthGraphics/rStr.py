
import string
import random
'''creates the list from the text'''
def strArr(string):
    return [char for char in string]
'''generate a random string'''
def strGenerator(size, chars=string.ascii_letters+' '):
    return [random.choice(chars) for _ in range(size)]
'''return random char'''
def mutatesChar(chars=string.ascii_letters+' '):
    return random.choice(chars)