from dataclasses import dataclass, field
from datetime import datetime
from models.candidato import Candidato
from models.vaga import Vaga
from models.enums import StatusInscricao


@dataclass
class Inscricao:
    candidato: Candidato
    vaga: Vaga
    inscricao: str = field(init=False)
    data_inscricao: datetime = field(default_factory=datetime.now)
    motivos: list[str] = field(default_factory=list, init=False)
    pontuacao: int = field(init=False)
    status: StatusInscricao = field(init=False)

    def __post_init__(self):
        self.inscricao = f"{self.candidato.matricula}-{self.vaga.id}"
        self.motivos = self.vaga.validar_requisitos(self.candidato)
        self.pontuacao = self.vaga.calcular_pontuacao(self.candidato)
        self.status = self._validar_status()

    def _validar_status(self) -> StatusInscricao:    
        if self.motivos or self.pontuacao < 8:
            return StatusInscricao.REPROVADO
        elif self.pontuacao >= 8 and self.pontuacao <= 11:
            return StatusInscricao.BANCO_TALENTOS
        else:
            return StatusInscricao.APROVADO