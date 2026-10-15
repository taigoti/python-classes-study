from models.candidato import Candidato
from models.inscricao import Inscricao
from models.vaga import Vaga
from models.enums import Turno, Pontuacao
from persistence.vaga_persistence import salvar_vaga
from views.terminal_view import input_candidato, print_inscricao
from persistence.candidato_persistence import salvar_candidato
from persistence.inscricao_persistence import salvar_inscricao

#candidato = input_candidato()
candidato = Candidato(
    nome="Maria Silva",
    idade=22,
    curso="Engenharia de Software",
    semestre=4,
    email="t@t.com",
    turno="tarde",
    trabalho_em_equipe=True,
    computador_proprio=True,
    conhecimentos={"python", "java", "sql", "javascript"}
)

vaga = Vaga(
    id="dstf",
    titulo="Desenvolvedor de Software",
    descricao="Vaga para desenvolvedor de software com experiência em Python e Java.",
    conhecimentos={"python", "java", "sql", "javascript"},
    turno=Turno.TARDE,
    pontuacao=Pontuacao
)

inscricao = Inscricao(candidato, vaga)
salvar_inscricao(inscricao)
salvar_vaga(vaga)

if __name__ == "__main__":
    print_inscricao(inscricao)