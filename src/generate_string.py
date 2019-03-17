import random

def generate_string():
    """a function that generates a string that is 28 characters long
    by choosing random letters from the 26 letters in the alphabet
    plus the space."""
    genString = ''
    for i in range(28):
        genString += random.choice('abcdefghijklmnopqrstuvwxyz ')

    return genString
