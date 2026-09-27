from enum import Enum


class Turno(str, Enum):
  MANHA = "manhã"
  TARDE = "tarde"

class StatusInscricao(str, Enum):
  APROVADO = "APROVADO"
  REPROVADO = "NÃO APROVADO"
  BANCO_TALENTOS = "BANCO DE TALENTOS"