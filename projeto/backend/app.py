
from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

# ⚠️ COLOQUE SEU IP AQUI (o que apareceu no Stellarium)
STELLARIUM_URL = "http://10.41.82.206:8090"

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Painel Stellarium</title>

<style>
body {
    background: #0b0f1a;
    color: white;
    text-align: center;
    font-family: Arial;
}

h1 {
    margin-top: 20px;
}

button {
    padding: 20px;
    margin: 10px;
    font-size: 18px;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    width: 220px;
}

.on { background: #2ecc71; }
.off { background: #e74c3c; }
</style>
</head>

<body>

<h1>🌌 Controle Stellarium</h1>

<form method="post" action="/acao">

<button name="acao" value="atmos_on" class="on">Atmosfera ON</button>
<button name="acao" value="atmos_off" class="off">Atmosfera OFF</button><br>

<button name="acao" value="land_on" class="on">Paisagem ON</button>
<button name="acao" value="land_off" class="off">Paisagem OFF</button><br>

<button name="acao" value="const_on" class="on">Constelações ON</button>
<button name="acao" value="const_off" class="off">Constelações OFF</button><br>

<button name="acao" value="time_forward">⏩ Tempo +</button>
<button name="acao" value="time_pause">⏸ Pausar</button>
<button name="acao" value="time_back">⏪ Tempo -</button><br>

<button name="acao" value="modo_palestra">🎤 Modo Palestra</button>
<h3>Digite o Corpo Celeste:</h3>
<input name="corpo_celeste" type="text" placeholder="ex: Mars"><br><br>

<button name="acao" value="buscar_objeto">🔍 Buscar</button>

</form>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)


def set_prop(prop, val):
    try:
        r = requests.post(
            f"{STELLARIUM_URL}/api/stelproperty/set",
            data={"id": prop, "value": val}
        )
        print(prop, val, "->", r.text)
    except Exception as e:
        print("Erro:", e)


@app.route("/acao", methods=["POST"])
def acao():
    acao = request.form.get("acao")
    corpo_celeste = request.form.get("corpo_celeste")

    if acao == "atmos_on":
        set_prop("LandscapeMgr.atmosphereDisplayed", "true")

    elif acao == "atmos_off":
        set_prop("LandscapeMgr.atmosphereDisplayed", "false")

    elif acao == "land_on":
        set_prop("LandscapeMgr.landscapeDisplayed", "true")

    elif acao == "land_off":
        set_prop("LandscapeMgr.landscapeDisplayed", "false")

    elif acao == "const_on":
        set_prop("ConstellationMgr.linesDisplayed", "true")

    elif acao == "const_off":
        set_prop("ConstellationMgr.linesDisplayed", "false")

    elif acao == "time_forward":
        requests.post(f"{STELLARIUM_URL}/api/main/time", data={"timerate": "100"})

    elif acao == "time_pause":
        requests.post(f"{STELLARIUM_URL}/api/main/time", data={"timerate": "0"})

    elif acao == "time_back":
        requests.post(f"{STELLARIUM_URL}/api/main/time", data={"timerate": "-100"})

    elif acao == "modo_palestra":
        set_prop("StelSkyDrawer.flagAtmosphere", "false")
        set_prop("LandscapeMgr.flagLandscape", "false")
        set_prop("ConstellationMgr.linesDisplayed", "true")

   
    elif acao == "buscar_objeto":
        if corpo_celeste:
            try:
                corpo_celeste = corpo_celeste.strip().title()

                requests.post(
                    f"{STELLARIUM_URL}/api/main/focus",
                    data={"target": corpo_celeste}
                )

                print("Focando em:", corpo_celeste)

            except Exception as e:
                print("Erro:", e)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

