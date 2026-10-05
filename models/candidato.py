from dataclasses import dataclass, field
import random


@dataclass
class Candidato:
    nome: str
    idade: int
    curso: str
    semestre: int
    email: str
    turno: str
    trabalho_em_equipe: bool
    computador_proprio: bool
    conhecimentos: set[str] = field(default_factory=set)


    @property
    def matricula(self) -> str:
        id_unico = random.randint(100, 999)

        prefixo_nome = self.nome[:1].lower()
        prefixo_curso = self.curso[:1].lower()

        return f"{prefixo_nome}{prefixo_curso}{self.semestre}{id_unico}"
    
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

    def __dict__(self) -> dict:
        return {
            "nome": self.nome,
            "matricula": self.matricula,
            "idade": self.idade,
            "curso": self.curso,
            "semestre": self.semestre,
            "email": self.email,
            "turno": self.turno,
            "trabalho_em_equipe": self.trabalho_em_equipe,
            "computador_proprio": self.computador_proprio,
            "conhecimentos": list(self.conhecimentos),
        }