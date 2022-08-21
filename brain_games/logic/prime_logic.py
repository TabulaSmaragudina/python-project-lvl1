from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def prime_game():
    name = welcome_user()
    index = 0
    print("""Answer "yes" if given number is prime. Otherwise answer "no".""")
    while index < 3:
        number = randint(1, 100)
        d = 2
        while number % d != 0:
            d += 1
        if d == number:
            true_answer = 'yes'
        else:
            true_answer = 'no'
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            index += 1
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{true_answer}'.
                        Let's try again, {name}!""")
            return 0
    print(f'Congratulations, {name}!')
