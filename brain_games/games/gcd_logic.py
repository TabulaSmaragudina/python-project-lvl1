from random import randint
import math


Description = "Find the greatest common divisor of given numbers."


def main():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    print(f"Question: {number_1} {number_2}")
    result = str(math.gcd(number_1, number_2))
    return result
