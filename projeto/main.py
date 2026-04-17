import requests

BASE_URL = "http://localhost:8090/api"


def focar_objeto(nome):
    url = f"{BASE_URL}/main/focus"
    params = {"target": nome}

    r = requests.post(url, data=params)

    if r.status_code == 200:
        print(f"Focando em {nome}")
    else:
        print("Erro ao focar:", r.text)


def acelerar_tempo():
    url = f"{BASE_URL}/main/time"
    params = {"timerate": 100}

    r = requests.post(url, data=params)

    if r.status_code == 200:
        print("Tempo acelerado")
    else:
        print("Erro:", r.text)


def mostrar_constelacoes():
    url = f"{BASE_URL}/main/view"
    params = {"constellation_art": "true"}

    r = requests.post(url, data=params)

    if r.status_code == 200:
        print("Constelações ativadas")
    else:
        print("Erro:", r.text)


# TESTE
focar_objeto("Mars")
acelerar_tempo()
mostrar_constelacoes()