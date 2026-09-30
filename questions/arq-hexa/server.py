import random


def generate(data):
    n = random.randint(40, 250)
    data["params"]["decimal"] = n
    data["correct_answers"]["hexa"] = format(n, "x")
