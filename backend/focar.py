import unicodedata

from backend.funcoes import focarcorpoCeleste

# ---------------------------------------------------------------
# AJUSTE PRINCIPAL PARA A CÚPULA
# Fração do diâmetro da cúpula que o astro deve ocupar.
#   0.20 = astro menor, mais "ar" ao redor
#   0.30 = padrão (bom equilíbrio)
#   0.45 = astro grande, quase enchendo a vista
# ---------------------------------------------------------------
OCUPACAO = 0.30

# Menor FOV que o Stellarium aceita com segurança (graus)
FOV_MINIMO = 0.001

# Diâmetro angular típico visto da Terra, em graus
# (Saturno inclui os anéis; os valores variam um pouco ao longo do ano)
DIAMETROS = {
    "Sol": 0.53,
    "Mercúrio": 0.0019,
    "Vênus": 0.0056,
    "Lua": 0.52,
    "Marte": 0.0022,
    "Júpiter": 0.011,
    "Saturno": 0.011,
    "Urano": 0.0010,
    "Netuno": 0.00064,
}

NOMES_STELLARIUM = {
    "Sol": "Sun",
    "Mercúrio": "Mercury",
    "Vênus": "Venus",
    "Lua": "Moon",
    "Marte": "Mars",
    "Júpiter": "Jupiter",
    "Saturno": "Saturn",
    "Urano": "Uranus",
    "Netuno": "Neptune",
}


def calcularFov(diametro_graus, ocupacao=OCUPACAO):
    """FOV necessário para o astro ocupar 'ocupacao' do diâmetro da cúpula."""
    return max(round(diametro_graus / ocupacao, 4), FOV_MINIMO)


PLANETAS = {
    nome_pt: {"nome": NOMES_STELLARIUM[nome_pt], "fov": calcularFov(diametro)}
    for nome_pt, diametro in DIAMETROS.items()
}


def normalizarTexto(texto):
    """Minúsculas e sem acentos: 'Vênus' -> 'venus'."""
    texto = unicodedata.normalize("NFD", texto.strip().lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def buscarAstro(nome_digitado):
    """Retorna os dados do astro (ou None), ignorando acentos e maiúsculas."""
    alvo = normalizarTexto(nome_digitado)
    for chave, dados in PLANETAS.items():
        if normalizarTexto(chave) == alvo:
            return dados
    return None


def focarsistemaSolar(nome_digitado):
    astro = buscarAstro(nome_digitado)
    if astro is None:
        print("Astro não encontrado.")
        return False
    return focarcorpoCeleste(astro["nome"])


if __name__ == "__main__":
    for nome, dados in PLANETAS.items():
        print(f"{nome:10} {dados['nome']:8} fov = {dados['fov']}")