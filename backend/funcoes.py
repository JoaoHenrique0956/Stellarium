import requests

# IP da máquina que executa o Stellarium
STELLARIUM_URL = "http://10.41.82.204:8090"
TIMEOUT = 5


def _post(endpoint, dados):
    """Envia um POST ao Stellarium. Retorna True se deu certo, False se falhou."""
    try:
        r = requests.post(f"{STELLARIUM_URL}{endpoint}", data=dados, timeout=TIMEOUT)
        r.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Erro ao enviar comando ({endpoint}):", e)
        return False


def enviarStellarium(prop, val):
    return _post("/api/stelproperty/set", {"id": prop, "value": val})


def focarcorpoCeleste(corpo_celeste):
    return _post("/api/main/focus", {"target": corpo_celeste})


def regularZoom(valor):
    return _post("/api/main/fov", {"fov": str(valor)})


# Se True, confere se o Stellarium conhece o objeto antes de focar.
# (Sem isso, um nome inválido faria o zoom acontecer no lugar errado.)
VERIFICAR_OBJETO = True


def objetoExiste(nome_stellarium):
    try:
        r = requests.get(
            f"{STELLARIUM_URL}/api/objects/find",
            params={"str": nome_stellarium},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        return len(r.json()) > 0
    except (requests.RequestException, ValueError) as e:
        print("Erro ao procurar objeto:", e)
        return False


def focarComZoom(nome_stellarium, fov, mover=5, esperar=5, zoom=8):
    """Mesma sequência do script do tour, com movimentos lentos e suaves
    (melhores para projeção em cúpula, evitam enjoo na plateia).
    mover/esperar/zoom são durações em segundos."""
    if VERIFICAR_OBJETO and not objetoExiste(nome_stellarium):
        print("Objeto não encontrado no Stellarium:", nome_stellarium)
        return False
    codigo = (
        f'core.selectObjectByName("{nome_stellarium}"); '
        f'core.moveToSelectedObject({mover}); '
        f'core.wait({esperar}); '
        f'StelMovementMgr.zoomTo({fov}, {zoom});'
    )
    return _post("/api/scripts/direct", {"code": codigo})


# Equivalente ao modoPalestra() do script do tour
_MODO_APRESENTACAO = (
    "LandscapeMgr.setFlagAtmosphere(false); "
    "LandscapeMgr.setFlagLandscape(false); "
    "LandscapeMgr.setFlagCardinalPoints(false); "
    "ConstellationMgr.setFlagLines(false); "
    "ConstellationMgr.setFlagLabels(false); "
    "ConstellationMgr.setFlagArt(false); "
    "ConstellationMgr.setFlagBoundaries(false); "
    "GridLinesMgr.setFlagEquatorGrid(false); "
    "GridLinesMgr.setFlagEquatorLine(false); "
    "GridLinesMgr.setFlagAzimuthalGrid(false); "
    "GridLinesMgr.setFlagEclipticLine(false); "
    "GridLinesMgr.setFlagMeridianLine(false); "
    "GridLinesMgr.setFlagCircumpolarCircles(false); "
    "GridLinesMgr.setFlagCelestialPoles(false); "
    "core.setGuiVisible(false);"
)


def modoApresentacao():
    """Limpa o céu (sem atmosfera, chão, linhas, grades) e esconde a interface."""
    return _post("/api/scripts/direct", {"code": _MODO_APRESENTACAO})


def mostrarInterface():
    return _post("/api/scripts/direct", {"code": "core.setGuiVisible(true);"})


def alterarTempo(taxa):
    return _post("/api/main/time", {"timerate": str(taxa)})


# Ações simples (propriedade, valor) para uso por texto/terminal
ACOES = {
    "atmos_on": ("LandscapeMgr.atmosphereDisplayed", "true"),
    "atmos_off": ("LandscapeMgr.atmosphereDisplayed", "false"),
    "land_on": ("LandscapeMgr.landscapeDisplayed", "true"),
    "land_off": ("LandscapeMgr.landscapeDisplayed", "false"),
    "const_on": ("ConstellationMgr.linesDisplayed", "true"),
    "const_off": ("ConstellationMgr.linesDisplayed", "false"),
    "art_constelation_on": ("ConstellationMgr.artDisplayed", "true"),
    "art_constelation_off": ("ConstellationMgr.artDisplayed", "false"),
    "name_constelation_on": ("ConstellationMgr.namesDisplayed", "true"),
    "name_constelation_off": ("ConstellationMgr.namesDisplayed", "false"),
}

TEMPO = {"time_forward": 100, "time_pause": 0, "time_back": -100}


def executarAcao(acao):
    if acao in ACOES:
        return enviarStellarium(*ACOES[acao])
    if acao in TEMPO:
        return alterarTempo(TEMPO[acao])
    print("Ação desconhecida:", acao)
    return False


# Teste rápido pelo terminal: python -m backend.funcoes
if __name__ == "__main__":
    executarAcao(input("Digite a ação: ").strip())