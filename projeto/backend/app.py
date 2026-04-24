
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# ⚠️ COLOQUE SEU IP AQUI (o que apareceu no Stellarium)
STELLARIUM_URL = "http://10.41.82.206:8090"

# Chama a requisição web/interage
@app.route("/")
def index():
    return render_template("index.html")

# Permite acesso e manipulação dos arquivos do Stellarium, afim de automatização de funções
def set_prop(prop, val):
    try:
        r = requests.post(
            f"{STELLARIUM_URL}/api/stelproperty/set",
            data={"id": prop, "value": val}
        )
        print(prop, val, "->", r.text)
    except Exception as e:
        print("Erro:", e)

# Permite que as funções sejam executadas via "POST" (por meio de interface e caixa de texto)
@app.route("/acao", methods=["POST"])
def acao():
    acao = request.form.get("acao")
    corpo_celeste = request.form.get("corpo_celeste")

    # Liga a atmosfera
    if acao == "atmos_on":
        set_prop("LandscapeMgr.atmosphereDisplayed", "true")

    # Desliga a atmosfera
    elif acao == "atmos_off":
        set_prop("LandscapeMgr.atmosphereDisplayed", "false")

    #Liga o "chão"
    elif acao == "land_on":
        set_prop("LandscapeMgr.landscapeDisplayed", "true")

    #Desliga o "chão"
    elif acao == "land_off":
        set_prop("LandscapeMgr.landscapeDisplayed", "false")

     #Liga as constelações"
    elif acao == "const_on":
        set_prop("ConstellationMgr.linesDisplayed", "true")

    # Desliga as constelações
    elif acao == "const_off":
        set_prop("ConstellationMgr.linesDisplayed", "false")

        

    # Acelera o tempo em 100
    elif acao == "time_forward":
        requests.post(f"{STELLARIUM_URL}/api/main/time", data={"timerate": "100"})

    elif acao == "time_pause":
        requests.post(f"{STELLARIUM_URL}/api/main/time", data={"timerate": "0"})

    elif acao == "time_back":
        requests.post(f"{STELLARIUM_URL}/api/main/time", data={"timerate": "-100"})



    elif acao == "art_constelation_on":
        set_prop("ConstellationMgr.artDisplayed" , "true")

    elif acao == "art_constelation_off":
        set_prop("ConstellationMgr.artDisplayed" , "false")

    elif acao == "name_constelation_on":
        set_prop("ConstellationMgr.namesDisplayed" , "true")

    elif acao == "name_constelation_off":
        set_prop("ConstellationMgr.namesDisplayed" , "false")

    


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
    elif acao == "modo_palestra":
        set_prop("LandscapeMgr.landscapeDisplayed", "false") 
        set_prop("LandscapeMgr.atmosphereDisplayed", "false")
        set_prop("ConstellationMgr.linesDisplayed", "true")

        set_prop("ConstellationMgr.namesDisplayed" , "true")
        set_prop("ConstellationMgr.artDisplayed" , "false")

    return redirect("/")
  

if __name__ == "__main__":
    app.run(debug=True)

