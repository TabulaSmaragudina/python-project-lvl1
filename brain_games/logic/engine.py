import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.Description)
    answers_count = 0
    final_answer = 3
    while answers_count < final_answer:
        logic = game.run_logic()
        print(f'Question: {logic[1]}')
        true_answer = logic[0]
        answer = prompt.string('Your answer: ')
        if answer != true_answer:
            print(f"""'{answer}' is wrong answer ;(.\
Correct answer was '{true_answer}'.
Let's try again, {name}!""")
            return
        print('Correct!')
        answers_count += 1
    print(f'Congratulations, {name}!')
