"""Ponto de entrada do Planetary Hub.

Execute a partir da pasta do projeto:
    python main.py
"""
import sys
from pathlib import Path

# Garante que 'backend' e 'templates' sejam encontrados em qualquer cenário
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Importar abre a interface (o desktop_principal chama janela.mainloop())
from templates import desktop_principal  # noqa: F401