import random


Description = "What is the result of the expression?"
number_1 = str(random.randint(1, 100))
number_2 = str(random.randint(1, 100))
op = random.choice(['+', '-', '*'])
question = number_1 + ' ' + op + ' ' + number_2
Question = f'Question: {question}'
true_answer = str(eval(question))

