import random


def generate(data):
    a = random.randint(12, 89)
    b = random.randint(12, 89)
    data["params"]["a"] = a
    data["params"]["b"] = b
    data["correct_answers"]["soma"] = a + b
