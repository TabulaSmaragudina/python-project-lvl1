import random


Description = "What is the result of the expression?"


def main():
    number_1 = str(random.randint(1, 100))
    number_2 = str(random.randint(1, 100))
    op = random.choice(['+', '-', '*'])
    question = number_1 + ' ' + op + ' ' + number_2
    print(f'Question: {question}')
    result = str(eval(question))
    return result
