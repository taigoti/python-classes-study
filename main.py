from models.candidato import Candidato
from models.inscricao import Inscricao
from models.vaga import Vaga
from views.terminal_view import input_candidato, print_inscricao


#candidato = input_candidato()

candidato = Candidato(
    nome="João Silva",
    idade=20,
    curso="Engenharia de Software",
    semestre=4,
    email="joao.silva@example.com",
    turno="manhã",
    trabalho_em_equipe=False,
    computador_proprio=True,
    conhecimentos={"python", "java", "sql", "javascript"})

vaga = Vaga(
    id=1,
    titulo="Desenvolvedor de Software",
    descricao="Vaga para desenvolvedor de software com experiência em Python e Java.",
    conhecimentos={"python", "java", "sql", "javascript"},
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
    print_inscricao(inscricao)