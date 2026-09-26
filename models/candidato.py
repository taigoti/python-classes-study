import random

class Candidato:
    __slots__ = (
      'nome', 'idade', 'curso',
      'semestre', 'email', 'turno',
      'trabalho_em_equipe', 'computador_proprio',
      'conhecimentos', 'matricula'
    )
    
    def __init__(
        self,
        nome: str,
        idade: int,
        curso: str,
        semestre: int,
        email: str,
        turno: str,
        trabalho_em_equipe: bool,
        computador_proprio: bool,
        conhecimentos: set
    ):

        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.semestre = semestre
        self.email = email
        self.turno = turno
        self.trabalho_em_equipe = trabalho_em_equipe
        self.computador_proprio = computador_proprio
        self.conhecimentos = conhecimentos
        self.matricula = self._gerar_matricula()

    def __str__(self) -> str:
        return f"""
            Candidato: {self.nome},
            Matrícula: {self.matricula},
            Email: {self.email},
            Curso: {self.curso},
            Semestre: {self.semestre}.
            Turno disponível: {self.turno},
            Conhecimentos: {self.conhecimentos}
        """

    def _gerar_matricula(self) -> str:
        id_unico = random.randint(100, 999)

        prefixo_nome = self.nome[:1].lower()
        prefixo_curso = self.curso[:1].lower()

        return f"{prefixo_nome}{prefixo_curso}{self.semestre}{id_unico}"