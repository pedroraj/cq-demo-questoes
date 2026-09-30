import random


def generate(data):
    distancia = random.randint(10, 99)
    tempo = random.choice([2, 4, 5, 8])
    data["params"]["distancia"] = distancia
    data["params"]["tempo"] = tempo
    data["correct_answers"]["velocidade"] = distancia / tempo
