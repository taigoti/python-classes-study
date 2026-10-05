from models.inscricao import Inscricao
from models.vaga import Vaga
from models.enums import Turno, Pontuacao
from views.terminal_view import input_candidato, print_inscricao
from persistence.candidato_persistence import salvar_candidato
from persistence.inscricao_persistence import salvar_inscricao

candidato = input_candidato()
salvar_candidato(candidato)

vaga = Vaga(
    id="dstf",
    titulo="Desenvolvedor de Software",
    descricao="Vaga para desenvolvedor de software com experiência em Python e Java.",
    conhecimentos={"python", "java", "sql", "javascript"},
    turno=Turno,
    pontuacao=Pontuacao
)

inscricao = Inscricao(candidato, vaga)
salvar_inscricao(inscricao)

if __name__ == "__main__":
    print_inscricao(inscricao)