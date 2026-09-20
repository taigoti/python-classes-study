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