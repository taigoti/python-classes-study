from models.candidato import Candidato
from validators.candidato_validator import validar_desclassificacao, calcular_pontuacao

candidato = Candidato.cadastrar()

motivos = validar_desclassificacao(
    candidato.idade, candidato.trabalho_em_equipe,
    conhecimentos_compativeis, candidato.turno)

print(candidato)

if motivos:
  print("CLASSIFICAÇÃO: NÃO APROVADO")
  print("Motivo(s):")

  for motivo in motivos:
    print(f"-> {motivo}")

else:
  pontuacao = calcular_pontuacao()

  print(f"Pontuação final: {pontuacao}")

  if pontuacao >= 9:
    print("Parabéns! Você foi APROVADO!")

  elif pontuacao > 5 and pontuacao < 9:
    print("Quase lá! Você ficou no banco de talentos, pois não atingiu todos os requisitos.")
  
  else:
    print("NÃO APROVADO. Sua pontuação foi menor que ou igual a 4.")