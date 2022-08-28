from brain_games.games import calc_logic
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(game):
    name = welcome_user()
    answers_count = 0
    print(game.Description)
    while answers_count < 3:
        print(game.Question)
        answer = prompt.string('Your answer: ')
        if answer == game.true_answer:
            print('Correct!')
            answers_count += 1
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{game.true_answer}'.
                            Let's try again, {name}!""")
            return 0
    print(f'Congratulations, {name}!')

run_game(calc_logic)
