from random import randint


Description = "What number is missing in the progression? "


def main():
    number_1 = randint(1, 10)
    number_2 = randint(80, 120)
    number_3 = randint(5, 12)
    progression = list(range(number_1, number_2, number_3))
    index = randint(1, len(progression) - 1)
    result = str(progression[index])
    progression[index] = '..'
    progression_question = (' '.join(map(str, progression)))
    print(f"Question: {progression_question}")
    return result