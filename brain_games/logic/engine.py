import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.Description)
    for i in range(3):
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
    print(f'Congratulations, {name}!')
