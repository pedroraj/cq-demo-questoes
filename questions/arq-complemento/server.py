import random


def generate(data):
    valor = random.choice([v for v in range(-120, 121) if abs(v) >= 5])
    data["params"]["bits"] = format(valor & 0xFF, "08b")
    data["correct_answers"]["valor"] = valor
