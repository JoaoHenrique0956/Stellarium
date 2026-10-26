import sys
from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ_PROJETO))

import tkinter as tk
from tkinter import ttk, messagebox

from backend.funcoes import enviarStellarium, focarcorpoCeleste, regularZoom
from backend.focar import PLANETAS, normalizarTexto
from backend.outros_astros import outrosAstros

OUTROS_ASTROS = outrosAstros() 

# Interface
janela = tk.Tk()
janela.title("Planetary Hub | Stellarium")
janela.geometry("650x680")
janela.configure(bg="#070A10")

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure(
    "TLabel",
    background="#0D121B",
    foreground="#EAF2FF",
    font=("Segoe UI", 11)
)
estilo.configure(
    "TButton",
    background="#172437",
    foreground="#EAF2FF",
    padding=8
)
estilo.configure(
    "TEntry",
    fieldbackground="#111927",
    foreground="#EAF2FF"
)


def criar_secao(titulo):
    quadro = tk.LabelFrame(
        janela,
        text=titulo,
        bg="#0D121B",
        fg="#4EA1FF",
        font=("Segoe UI", 11, "bold"),
        padx=12,
        pady=10
    )
    quadro.pack(fill="x", padx=16, pady=8)
    return quadro


def atualizar_status(texto):
    status.config(text=texto)


# Busca de astros
secao_busca = criar_secao("Buscar objeto celeste")

tk.Label(
    secao_busca,
    text="Digite o nome em português:",
    bg="#0D121B",
    fg="#EAF2FF"
).pack(anchor="w")

entrada = ttk.Entry(secao_busca, font=("Segoe UI", 12))
entrada.pack(fill="x", pady=7)

lista = tk.Listbox(
    secao_busca,
    height=5,
    bg="#111927",
    fg="#EAF2FF",
    selectbackground="#24558A",
    font=("Segoe UI", 11)
)
lista.pack(fill="x")

selecionados = []


def obter_catalogo():
    catalogo = []

    for chave, dados in PLANETAS.items():
        catalogo.append((chave, dados["nome"], dados["fov"]))

    for nome_pt, (nome_stellarium, fov) in OUTROS_ASTROS.items():
        catalogo.append((nome_pt, nome_stellarium, fov))

    return catalogo


def atualizar_sugestoes(event=None):
    termo = normalizarTexto(entrada.get())
    lista.delete(0, tk.END)
    selecionados.clear()

    if not termo:
        return

    for nome_pt, nome_api, fov in obter_catalogo():
        if termo in normalizarTexto(nome_pt):
            selecionados.append((nome_pt, nome_api, fov))
            lista.insert(tk.END, nome_pt.title())


def focar_selecionado(event=None):
    selecao = lista.curselection()

    if not selecao:
        atualizar_status("Selecione um astro na lista.")
        return

    nome_pt, nome_api, fov = selecionados[selecao[0]]

    try:
        focarcorpoCeleste(nome_api)
        regularZoom(fov)
        atualizar_status(f"Comando de foco enviado: {nome_pt.title()}")
    except Exception as erro:
        atualizar_status(f"Erro: {erro}")


entrada.bind("<KeyRelease>", atualizar_sugestoes)
lista.bind("<Double-Button-1>", focar_selecionado)

ttk.Button(
    secao_busca,
    text="Focar no astro selecionado",
    command=focar_selecionado
).pack(fill="x", pady=8)


# Controles de ambiente
secao_ambiente = criar_secao("Ambiente")


def criar_botoes(quadro, botoes):
    grade = tk.Frame(quadro, bg="#0D121B")
    grade.pack(fill="x")

    for indice, (texto, comando) in enumerate(botoes):
        ttk.Button(
            grade,
            text=texto,
            command=comando
        ).grid(
            row=indice // 2,
            column=indice % 2,
            sticky="ew",
            padx=4,
            pady=4
        )

    grade.columnconfigure(0, weight=1)
    grade.columnconfigure(1, weight=1)


criar_botoes(secao_ambiente, [
    ("Atmosfera: ligar", lambda: enviarStellarium(
        "LandscapeMgr.atmosphereDisplayed", "true")),
    ("Atmosfera: desligar", lambda: enviarStellarium(
        "LandscapeMgr.atmosphereDisplayed", "false")),
    ("Chão: ligar", lambda: enviarStellarium(
        "LandscapeMgr.landscapeDisplayed", "true")),
    ("Chão: desligar", lambda: enviarStellarium(
        "LandscapeMgr.landscapeDisplayed", "false")),
])


# Controles de constelações
secao_constelacoes = criar_secao("Constelações")

criar_botoes(secao_constelacoes, [
    ("Linhas: ligar", lambda: enviarStellarium(
        "ConstellationMgr.linesDisplayed", "true")),
    ("Linhas: desligar", lambda: enviarStellarium(
        "ConstellationMgr.linesDisplayed", "false")),
    ("Ilustrações: ligar", lambda: enviarStellarium(
        "ConstellationMgr.artDisplayed", "true")),
    ("Ilustrações: desligar", lambda: enviarStellarium(
        "ConstellationMgr.artDisplayed", "false")),
    ("Nomes: ligar", lambda: enviarStellarium(
        "ConstellationMgr.namesDisplayed", "true")),
    ("Nomes: desligar", lambda: enviarStellarium(
        "ConstellationMgr.namesDisplayed", "false")),
])


# Tempo
secao_tempo = criar_secao("Tempo astronômico")


def alterar_tempo(taxa):
    import requests
    from backend.funcoes import STELLARIUM_URL

    try:
        resposta = requests.post(
            f"{STELLARIUM_URL}/api/main/time",
            data={"timerate": str(taxa)},
            timeout=5
        )
        resposta.raise_for_status()
        atualizar_status("Comando de tempo enviado.")
    except requests.RequestException as erro:
        atualizar_status(f"Erro ao alterar o tempo: {erro}")


criar_botoes(secao_tempo, [
    ("Retroceder", lambda: alterar_tempo(-100)),
    ("Pausar", lambda: alterar_tempo(0)),
    ("Avançar", lambda: alterar_tempo(100)),
])


# Zoom manual
secao_zoom = criar_secao("Zoom")

campo_zoom = ttk.Entry(secao_zoom)
campo_zoom.insert(0, "2")
campo_zoom.pack(side="left", fill="x", expand=True, padx=(0, 8))


def aplicar_zoom():
    try:
        valor = float(campo_zoom.get())

        if not 0 < valor <= 180:
            raise ValueError("O FOV deve ser maior que 0 e até 180.")

        regularZoom(valor)
        atualizar_status(f"Comando de zoom enviado: {valor}°")

    except ValueError as erro:
        messagebox.showerror("Zoom inválido", str(erro))


ttk.Button(
    secao_zoom,
    text="Aplicar",
    command=aplicar_zoom
).pack(side="right")


# Status
secao_status = criar_secao("Status")
status = tk.Label(
    secao_status,
    text="Aguardando comando.",
    bg="#0D121B",
    fg="#4EA1FF",
    anchor="w",
    wraplength=570
)
status.pack(fill="x")

janela.mainloop()
