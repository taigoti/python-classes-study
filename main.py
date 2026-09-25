from models.candidato import Candidato
from models.inscricao import Inscricao
from models.vaga import Vaga


candidato = Candidato(
    nome="João Silva",
    idade=20,
    curso="Engenharia de Software",
    semestre=3,
    email="joao.silva@me.com",
    turno="tarde",
    trabalho_em_equipe=True,
    computador_proprio=True,
    conhecimentos={"Python", "SQL"}
  )

vaga = Vaga(
    id=1,
    titulo="Desenvolvedor de Software",
    descricao="Vaga para desenvolvedor de software com experiência em Python e Java.",
    conhecimentos={"Python", "Java", "SQL", "JavaScript"},
    turno={"manhã", "tarde"},
    pontuacao={
        "equipe": 2,
        "turno": 1,
        "conhecimento": 3,
        "computador_proprio": 1
    }
  )

inscricao = Inscricao(candidato, vaga)


if __name__ == "__main__":
    print(f"Inscrição: {inscricao.inscricao}")
    print(f"Data da inscrição: {inscricao.data_inscricao}")
    print(f"Pontuação: {inscricao.pontuacao}")
    print(f"Status: {inscricao.status}")