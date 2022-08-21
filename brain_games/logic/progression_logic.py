from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def progression_game():
    name = welcome_user()
    answers_count = 0
    print("What number is missing in the progression? ")
    while answers_count < 3:
        number_1 = randint(1, 10)
        number_2 = randint(80, 120)
        number_3 = randint(5, 12)
        progression = list(range(number_1, number_2, number_3))
        index = randint(1, len(progression) - 1)
        true_answer = progression[index]
        progression[index] = '..'
        progression_question = (' '.join(map(str, progression)))
        print(f"Question: {progression_question}")
        answer = prompt.string('Your answer: ')
        if answer == str(true_answer):
            print('Correct!')
            answers_count += 1
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{true_answer}'.
                        Let's try again, {name}!""")
            return 0
    print(f'Congratulations, {name}!')
