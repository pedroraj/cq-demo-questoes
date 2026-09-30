import random

# (estado com a preposição, capital). Sem o DF, que não é estado; São Paulo e Rio de Janeiro ficam só como
# distratoras, porque a capital tem o nome do estado.
ESTADOS = [
    ("do Acre", "Rio Branco"), ("de Alagoas", "Maceió"), ("do Amapá", "Macapá"), ("do Amazonas", "Manaus"),
    ("da Bahia", "Salvador"), ("do Ceará", "Fortaleza"), ("do Espírito Santo", "Vitória"), ("de Goiás", "Goiânia"),
    ("do Maranhão", "São Luís"), ("de Mato Grosso", "Cuiabá"), ("de Mato Grosso do Sul", "Campo Grande"),
    ("de Minas Gerais", "Belo Horizonte"), ("do Pará", "Belém"), ("da Paraíba", "João Pessoa"),
    ("do Paraná", "Curitiba"), ("de Pernambuco", "Recife"), ("do Piauí", "Teresina"),
    ("do Rio Grande do Norte", "Natal"), ("do Rio Grande do Sul", "Porto Alegre"), ("de Rondônia", "Porto Velho"),
    ("de Roraima", "Boa Vista"), ("de Santa Catarina", "Florianópolis"), ("de Sergipe", "Aracaju"),
    ("do Tocantins", "Palmas"),
]
OUTRAS = ["São Paulo", "Rio de Janeiro"]


def generate(data):
    estado, capital = random.choice(ESTADOS)
    candidatas = [c for _, c in ESTADOS if c != capital] + OUTRAS
    erradas = random.sample(candidatas, 3)
    data["params"]["estado"] = estado
    data["params"]["certa"] = capital
    data["params"]["errada1"] = erradas[0]
    data["params"]["errada2"] = erradas[1]
    data["params"]["errada3"] = erradas[2]
