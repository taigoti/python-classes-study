from models.constantes import *

def validar_conhecimentos(candidato: object) -> set:

    conhecimentos_candidato = candidato.conhecimentos

    conhecimentos_compativeis = conhecimentos_candidato.intersection(
        CONHECIMENTOS_EXIGIDOS)

    conhecimentos_faltantes = CONHECIMENTOS_EXIGIDOS.difference(
        conhecimentos_candidato)

    return conhecimentos_compativeis, conhecimentos_faltantes


def calcular_pontuacao(candidato, conhecimentos_compativeis) -> int:
  pontuacao = PONTUACAO['equipe'] + PONTUACAO['turno']
  pontuacao += len(conhecimentos_compativeis) * PONTUACAO['conhecimento']

  if candidato.computador_proprio:
    pontuacao += PONTUACAO['computador']

  return pontuacao
b

def validar_pontuacao(pontuacao: int) -> str:
  if pontuacao >= 9:
    return "Parabéns! Você foi APROVADO!"

  elif pontuacao > 5 and pontuacao < 9:
    return "Quase lá! Você ficou no BANCO DE TALENTOS, pois não atingiu todos os requisitos."
  
  else:
    return "NÃO APROVADO. Sua pontuação foi menor que ou igual a 4."

  
def validar_desclassificacao(
    idade: int,
    trabalho_em_equipe: bool,
    conhecimentos_compativeis: set,
    conhecimentos_faltantes: set,
    turno: str
    ) -> list[str]:
  
  erros = []
  
  if idade < 16:
    erros.append(MOTIVOS_DESAPROVACAO['idade'])

  if not trabalho_em_equipe:
    erros.append(MOTIVOS_DESAPROVACAO['equipe'])

  if len(conhecimentos_compativeis) < 3:
    erros.append(f"{MOTIVOS_DESAPROVACAO['conhecimentos']} {conhecimentos_faltantes}")

  if turno not in TURNOS_DISPONIVEIS:
    erros.append(MOTIVOS_DESAPROVACAO['turno'])
  
  return erros