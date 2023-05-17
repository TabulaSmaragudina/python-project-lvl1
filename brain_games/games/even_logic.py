from random import randint


Description = "Answer 'yes' if the number is even, otherwise answer 'no'."


def run_logic():
    number = randint(1, 100)
    question = number
    if number % 2 == 0:
        result = 'yes'
    elif number % 2 != 0:
        result = 'no'
    return result, question
