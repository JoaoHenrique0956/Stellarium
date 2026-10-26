"""Catálogo de astros extras: nome em português -> (nome no Stellarium, FOV).

O FOV (em graus) pensa na cúpula: o objeto ocupa cerca de 30% da vista.
Os valores são estimativas por categoria; ajuste testando na cúpula:
  - mude o FOV padrão da categoria em CATEGORIAS, ou
  - mude um astro específico em FOV_ESPECIFICO.
"""

GALAXIAS = {
    "galáxia de andrômeda": "Andromeda Galaxy",
    "galáxia do triângulo": "Triangulum Galaxy",
    "galáxia do redemoinho": "Whirlpool Galaxy",
    "galáxia do charuto": "Cigar Galaxy",
    "galáxia de bode": "Bode's Galaxy",
    "galáxia do catavento": "Pinwheel Galaxy",
    "galáxia do sombrero": "Sombrero Galaxy",
    "galáxia do sombreiro": "Sombrero Galaxy",
    "galáxia do olho negro": "Black Eye Galaxy",
    "galáxia do girassol": "Sunflower Galaxy",
    "galáxia do escultor": "Sculptor Galaxy",
    "galáxia do sul": "Southern Pinwheel Galaxy",
    "galáxia da roda de carroça": "Cartwheel Galaxy",
    "galáxia das antenas": "Antennae Galaxies",
    "galáxia de centauro A": "Centaurus A",
    "galáxia elíptica de virgem": "M87",
    "galáxia do triângulo M33": "M33",
    "galáxia M51": "M51",
    "galáxia M81": "M81",
    "galáxia M82": "M82",
    "galáxia M101": "M101",
    "galáxia M104": "M104",
}

ESTRELAS = {
    "estrela polar": "Polaris",
    "sírius": "Sirius",
    "vega": "Vega",
    "betelgeuse": "Betelgeuse",
    "rigel": "Rigel",
    "antares": "Antares",
    "aldebarã": "Aldebaran",
    "arcturo": "Arcturus",
    "canopus": "Canopus",
    "canopus da quilha": "Canopus",
    "capela": "Capella",
    "procyon": "Procyon",
    "altair": "Altair",
    "spica": "Spica",
    "deneb": "Deneb",
    "formalhaut": "Fomalhaut",
    "castor": "Castor",
    "pólux": "Pollux",
    "regulus": "Regulus",
    "mimosa": "Mimosa",
    "acrux": "Acrux",
    "hadar": "Hadar",
    "achernar": "Achernar",
    "shaula": "Shaula",
    "bellatrix": "Bellatrix",
    "algol": "Algol",
    "alnitak": "Alnitak",
    "alnilam": "Alnilam",
    "mintaka": "Mintaka",
    "meissa": "Meissa",
    "mirfak": "Mirfak",
    "dubhe": "Dubhe",
    "merak": "Merak",
    "mizar": "Mizar",
    "alcor": "Alcor",
    "algorab": "Algorab",
    "denebola": "Denebola",
    "izar": "Izar",
    "sadr": "Sadr",
    "gacrux": "Gacrux",
    "peacock": "Peacock",
    "estrela de barnard": "Barnard's Star",
    "proxima centauri": "Proxima Centauri",
    "alfa centauri": "Alpha Centauri",
    "tau ceti": "Tau Ceti",
    "epsilon eridani": "Epsilon Eridani",
}

NEBULOSAS_DIFUSAS = {
    "nebulosa de órion": "Orion Nebula",
    "nebulosa do caranguejo": "Crab Nebula",
    "nebulosa da lagoa": "Lagoon Nebula",
    "nebulosa da trífida": "Trifid Nebula",
    "nebulosa da águia": "Eagle Nebula",
    "nebulosa ômega": "Omega Nebula",
    "nebulosa da tarântula": "Tarantula Nebula",
    "nebulosa da cabeça de cavalo": "Horsehead Nebula",
    "nebulosa da chama": "Flame Nebula",
    "nebulosa do cone": "Cone Nebula",
    "nebulosa da roseta": "Rosette Nebula",
    "nebulosa da carina": "Carina Nebula",
    "nebulosa do véu": "Veil Nebula",
    "nebulosa do pelicano": "Pelican Nebula",
    "nebulosa da íris": "Iris Nebula",
    "nebulosa do coração": "Heart Nebula",
    "nebulosa da alma": "Soul Nebula",
    "nebulosa da medusa": "Jellyfish Nebula",
}

NEBULOSAS_PLANETARIAS = {
    "nebulosa da hélice": "Helix Nebula",
    "nebulosa do anel": "Ring Nebula",
    "nebulosa do haltere": "Dumbbell Nebula",
    "nebulosa da borboleta": "Butterfly Nebula",
    "nebulosa do esquimó": "Eskimo Nebula",
    "nebulosa do olho de gato": "Cat's Eye Nebula",
    "nebulosa do ovo": "Egg Nebula",
    "nebulosa da coruja": "Owl Nebula",
    "nebulosa da formiga": "Ant Nebula",
    "nebulosa da aranha vermelha": "Red Spider Nebula",
    "nebulosa do retângulo vermelho": "Red Rectangle Nebula",
    "nebulosa da caveira": "Skull Nebula",
}

AGLOMERADOS = {
    "plêiades": "Pleiades",
    "híades": "Hyades",
    "aglomerado do presépio": "Beehive Cluster",
    "aglomerado de hércules": "Hercules Cluster",
    "aglomerado duplo de perseu": "Double Cluster",
    "aglomerado borboleta": "Butterfly Cluster",
    "aglomerado de joias": "Jewel Box",
    "aglomerado de ômega centauri": "Omega Centauri",
    "aglomerado 47 tucanae": "47 Tucanae",
    "47 tucanae": "47 Tucanae",
    "aglomerado M3": "M3",
    "aglomerado M5": "M5",
    "aglomerado M13": "M13",
    "aglomerado M15": "M15",
    "aglomerado M22": "M22",
    "aglomerado M92": "M92",
    "aglomerado M4": "M4",
    "aglomerado M10": "M10",
    "aglomerado M12": "M12",
    "aglomerado M2": "M2",
    "aglomerado M14": "M14",
    "aglomerado M71": "M71",
    "aglomerado M56": "M56",
    "aglomerado M80": "M80",
    "aglomerado M28": "M28",
    "aglomerado M9": "M9",
    "aglomerado M19": "M19",
    "aglomerado M62": "M62",
    "aglomerado M69": "M69",
    "aglomerado M70": "M70",
    "aglomerado M107": "M107",
    "aglomerado M11": "M11",
    "aglomerado M6": "M6",
    "aglomerado M7": "M7",
    "aglomerado M35": "M35",
    "aglomerado M36": "M36",
    "aglomerado M37": "M37",
    "aglomerado M38": "M38",
    "aglomerado M41": "M41",
    "aglomerado M44": "M44",
    "aglomerado M46": "M46",
    "aglomerado M47": "M47",
    "aglomerado M48": "M48",
    "aglomerado M50": "M50",
    "aglomerado M52": "M52",
    "aglomerado M67": "M67",
    "aglomerado M93": "M93",
    "aglomerado M103": "M103",
    "aglomerado NGC 869": "NGC 869",
    "aglomerado NGC 884": "NGC 884",
}

PLANETAS_ANOES = {
    "plutão": "Pluto",
    "ceres": "Ceres",
    "eris": "Eris",
    "haumea": "Haumea",
    "makemake": "Makemake",
}

COMETAS = {
    "cometa halley": "Halley",
    "cometa hale-bopp": "Hale-Bopp",
    "cometa neowise": "C/2020 F3 (NEOWISE)",
    "cometa encke": "Encke",
    "cometa swift-tuttle": "109P/Swift-Tuttle",
    "cometa 67p": "67P/Churyumov-Gerasimenko",
}

SATELITES = {
    "fobos": "Phobos",
    "deimos": "Deimos",
    "europa": "Europa",
    "ganimedes": "Ganymede",
    "calisto": "Callisto",
    "io": "Io",
    "titã": "Titan",
    "encélado": "Enceladus",
    "reia": "Rhea",
    "jápeto": "Iapetus",
    "dione": "Dione",
    "téti": "Tethys",
    "mimas": "Mimas",
    "hipérion": "Hyperion",
    "titânia": "Titania",
    "oberon": "Oberon",
    "ariel": "Ariel",
    "umbriel": "Umbriel",
    "tritão": "Triton",
    "caronte": "Charon",
}

OUTROS = {
    "quasar 3C 273": "3C 273",
    "quasar 3C 279": "3C 279",
    "aglomerado de coma": "Coma Cluster",
    "grande nuvem de magalhães": "Large Magellanic Cloud",
    "pequena nuvem de magalhães": "Small Magellanic Cloud",
    "nuvem de magalhães": "Large Magellanic Cloud",
}

# (dicionário, FOV padrão em graus)
CATEGORIAS = [
    (GALAXIAS, 1.0),
    (ESTRELAS, 20),
    (NEBULOSAS_DIFUSAS, 1.5),
    (NEBULOSAS_PLANETARIAS, 0.3),
    (AGLOMERADOS, 2.0),
    (PLANETAS_ANOES, 0.01),
    (COMETAS, 0.5),
    (SATELITES, 0.01),
    (OUTROS, 0.5),
]

# Exceções: objetos bem maiores ou menores que o padrão da categoria
FOV_ESPECIFICO = {
    "galáxia de andrômeda": 10,
    "galáxia do triângulo": 3.5,
    "galáxia do triângulo M33": 3.5,
    "nebulosa de órion": 3,
    "nebulosa da carina": 3,
    "nebulosa da roseta": 3,
    "nebulosa do véu": 6,
    "nebulosa do pelicano": 3,
    "nebulosa do coração": 3,
    "nebulosa da alma": 3,
    "nebulosa da medusa": 3,
    "nebulosa do caranguejo": 0.5,
    "nebulosa do cone": 0.5,
    "nebulosa da hélice": 1.5,
    "plêiades": 6,
    "híades": 15,
    "aglomerado do presépio": 4,
    "aglomerado M44": 4,
    "aglomerado duplo de perseu": 3,
    "aglomerado de ômega centauri": 1.5,
    "aglomerado 47 tucanae": 1.0,
    "47 tucanae": 1.0,
    "aglomerado de coma": 4,
    "grande nuvem de magalhães": 30,
    "nuvem de magalhães": 30,
    "pequena nuvem de magalhães": 15,
}


def _montar():
    catalogo = {}
    for astros, fov_padrao in CATEGORIAS:
        for nome_pt, nome_api in astros.items():
            fov = FOV_ESPECIFICO.get(nome_pt, fov_padrao)
            catalogo[nome_pt] = (nome_api, fov)
    return catalogo


OUTROS_ASTROS = _montar()


def outrosAstros():
    """Retorna {nome_pt: (nome_stellarium, fov)}."""
    return OUTROS_ASTROS