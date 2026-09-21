from models.candidato import Candidato
from validators.candidato_validator import *

candidato = Candidato.cadastrar()

conhecimentos_compativeis, conhecimentos_faltantes = validar_conhecimentos(candidato)

motivos = validar_desclassificacao(
    candidato.idade, candidato.trabalho_em_equipe,
    conhecimentos_compativeis, conhecimentos_faltantes,
    candidato.turno)

print(candidato)

if motivos:
  print("CLASSIFICAÇÃO: NÃO APROVADO")
  print("Motivo(s):")

  for motivo in motivos:
    print(f"-> {motivo}")

else:
  pontuacao = calcular_pontuacao(candidato, conhecimentos_compativeis)

  print(f"Pontuação final: {pontuacao}")

  print(validar_pontuacao(pontuacao))