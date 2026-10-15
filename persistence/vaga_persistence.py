import json
from pathlib import Path

from models.vaga import Vaga


DATA_PATH = Path("data/vagas.json")

def salvar_vaga(vaga_data: Vaga) -> None:
  DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

  dados = carregar_vagas()
  dados.append(vaga_data.__dict__)

  with open(DATA_PATH, "w", encoding="utf-8") as file:
    json.dump(dados, file, indent=4, ensure_ascii=False)


def carregar_vagas() -> list[dict]:
  if not DATA_PATH.exists():
    return []

  with open(DATA_PATH, "r", encoding="utf-8") as file:
    try:
      return json.load(file)
    except json.JSONDecodeError:
      return []