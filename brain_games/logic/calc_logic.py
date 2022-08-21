import random
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def calc_game():
    name = welcome_user()
    index = 0
    print("What is the result of the expression?")
    while index < 3:
        number_1 = str(random.randint(1, 100))
        number_2 = str(random.randint(1, 100))
        op = random.choice(['+', '-', '*'])
        question = number_1 + ' ' + op + ' ' + number_2
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        true_answer = str(eval(question))
        if answer == true_answer:
            print('Correct!')
            index += 1
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{true_answer}'.
                        Let's try again, {name}!""")
            return 0
    print(f'Congratulations, {name}!')
