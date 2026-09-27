from enum import Enum


class Turno(str, Enum):
  MANHA = "manhã"
  TARDE = "tarde"

class StatusInscricao(str, Enum):
  APROVADO = "APROVADO"
  REPROVADO = "NÃO APROVADO"
  BANCO_TALENTOS = "BANCO DE TALENTOS"

class Pontuacao(int, Enum):
  EQUIPE = 2
  TURNO = 1
  CONHECIMENTO = 2
  COMPUTADOR_PROPRIO = 1