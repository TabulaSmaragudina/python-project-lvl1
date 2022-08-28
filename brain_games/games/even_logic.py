from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even_game():
    name = welcome_user()
    index = 0
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    while index < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            true_answer = 'yes'
        elif number % 2 != 0:
            true_answer = 'no'
        if answer == true_answer:
            print('Correct!')
            index += 1
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{true_answer}'.
                        Let's try again, {name}!""")
            return 0
    print(f'Congratulations, {name}!')
