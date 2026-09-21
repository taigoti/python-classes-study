from models.constantes import *

def validar_conhecimentos(candidato: object) -> set:

    conhecimentos_candidato = candidato.conhecimentos

    conhecimentos_compativeis = conhecimentos_candidato.intersection(
        CONHECIMENTOS_EXIGIDOS)

    conhecimentos_faltantes = CONHECIMENTOS_EXIGIDOS.difference(
        conhecimentos_candidato)

    return conhecimentos_compativeis, conhecimentos_faltantes

