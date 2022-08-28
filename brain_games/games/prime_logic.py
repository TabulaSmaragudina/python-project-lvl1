from random import randint


Description = """Answer "yes" if given number is prime.\
 Otherwise answer "no"."""


def main():
    number = randint(1, 100)
    d = 2
    while number % d != 0:
        d += 1
    if d == number:
        result = 'yes'
    else:
        result = 'no'
    print(f"Question: {number}")
    return result
