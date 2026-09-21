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