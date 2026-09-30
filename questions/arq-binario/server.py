import random


def generate(data):
    n = random.randint(33, 254)
    data["params"]["binario"] = format(n, "08b")
    data["correct_answers"]["decimal"] = n
