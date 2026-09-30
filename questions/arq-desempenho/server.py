import random


def generate(data):
    instrucoes = random.choice([200, 300, 400, 500, 600, 800])  # milhões de instruções
    cpi = random.choice([1.2, 1.5, 2.0, 2.5])
    freq = random.choice([1.0, 1.5, 2.0, 2.5, 3.0])  # GHz
    data["params"]["instrucoes"] = instrucoes
    data["params"]["cpi"] = str(cpi).replace(".", ",")
    data["params"]["freq"] = str(freq).replace(".", ",")
    # tempo = instruções x CPI / frequência, em milissegundos
    data["correct_answers"]["tempo"] = instrucoes * 1e6 * cpi / (freq * 1e9) * 1e3
