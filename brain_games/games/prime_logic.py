from random import randint


Description = """Answer "yes" if given number is prime.\
 Otherwise answer "no"."""


def run_logic():
    number = randint(1, 100)
    d = 2
    while number % d != 0:
        d += 1
    if d == number:
        result = 'yes'
    else:
        result = 'no'
    question = number
    return result, question
