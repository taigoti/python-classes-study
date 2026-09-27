from models.inscricao import Inscricao
from models.vaga import Vaga
from views.terminal_view import input_candidato, print_inscricao
from models.enums import Turno, Pontuacao


candidato = input_candidato()

vaga = Vaga(
    id="dstf",
    titulo="Desenvolvedor de Software",
    descricao="Vaga para desenvolvedor de software com experiência em Python e Java.",
    conhecimentos={"python", "java", "sql", "javascript"},
    turno=Turno,
    pontuacao=Pontuacao
)

inscricao = Inscricao(candidato, vaga)


if __name__ == "__main__":
    print_inscricao(inscricao)