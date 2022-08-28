from random import randint


Description = "Answer 'yes' if the number is even, otherwise answer 'no'."


def main():
    number = randint(1, 100)
    print(f'Question: {number}')
    if number % 2 == 0:
        result = 'yes'
    elif number % 2 != 0:
        result = 'no'
    return result
