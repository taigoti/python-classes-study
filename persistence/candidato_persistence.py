import json
from pathlib import Path

from models.candidato import Candidato

DATA_PATH = Path("data/candidatos.json")

def salvar_candidato(candidato_data: Candidato) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    dados = carregar_candidatos()
    dados.append(candidato_data.__dict__)

    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)


def carregar_candidatos() -> list[dict]:
    if not DATA_PATH.exists():
        return []

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []