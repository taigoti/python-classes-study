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
        id_unico = random.randint(10000, 99999)

        prefixo_nome = self.nome[:3].lower()
        prefixo_curso = self.curso[:2].lower()

        return f"{prefixo_nome}{prefixo_curso}-{self.semestre}{id_unico}"

    @classmethod
    def cadastrar(cls):
        nome = str(input("Nome: ").strip())
        idade = int(input("Idade: "))
        curso = str(input("Curso: ").strip())
        semestre = int(input("Semestre: "))

        while True:
            email = str(input("Email: ").strip()).lower()

            if '@' in email and '.' in email:
                break

            print("Digite um email válido!")

        turno = str(
            input("Turno disponível: ").strip())

        trabalho_em_equipe = str(
            input("Você aceita trabalhar em equipe? ")).lower() == "sim"

        computador_proprio = str(
            input("Você tem computador próprio? ")).lower() == "sim"

        conhecimentos_input = input("Insira seus conhecimentos separados por vírgula: ")
        conhecimentos = {conhecimento.strip() for conhecimento in conhecimentos_input.split(',') if conhecimento.strip()}

        return cls(
            nome = nome,
            idade = idade,
            curso = curso,
            semestre = semestre,
            email = email,
            turno = turno,
            trabalho_em_equipe = trabalho_em_equipe,
            computador_proprio = computador_proprio,
            conhecimentos = conhecimentos
        )