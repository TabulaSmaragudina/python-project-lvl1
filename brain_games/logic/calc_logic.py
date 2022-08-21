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
        question = str(random.randint(1, 100))+' '+random.choice(['+', '-', '*'])+' '+str(random.randint(1, 100))
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        true_answer = str(eval(question))
        if answer == true_answer:
            print('Correct!')
            index += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{true_answer}'."
                         f"\nLet`s try again, {name}!")
    print(f'Congratulations, {name}!')
