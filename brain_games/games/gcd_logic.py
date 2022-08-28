from random import randint
import prompt
import math


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def gcd_game():
    name = welcome_user()
    index = 0
    print("Find the greatest common divisor of given numbers.")
    while index < 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        print(f"Question: {number_1} {number_2}")
        answer = prompt.string('Your answer: ')
        true_answer = math.gcd(number_1, number_2)
        if answer == str(true_answer):
            print('Correct!')
            index += 1
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{true_answer}'.
                        Let's try again, {name}!""")
            return 0
    print(f'Congratulations, {name}!')
