import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.Description)
    answers_count = 0
    while answers_count < 3:
        true_answer = game.main()
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            answers_count += 1
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{true_answer}'.
                            Let's try again, {name}!""")
            return 0
    print(f'Congratulations, {name}!')
