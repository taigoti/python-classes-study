from models.inscricao import Inscricao
from models.vaga import Vaga
from views.terminal_view import input_candidato, print_inscricao


candidato = input_candidato()

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