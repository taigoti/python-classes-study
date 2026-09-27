from dataclasses import dataclass, field
from models.candidato import Candidato
from models.enums import Turno, Pontuacao

@dataclass
class Vaga:
    id: str
    titulo: str
    descricao: str
    conhecimentos: set[str] = field(default_factory=set)
    turno: Turno = field(default_factory=lambda: Turno)
    pontuacao: Pontuacao = field(default_factory=lambda: Pontuacao)

    def validar_requisitos(self, candidato: Candidato) -> list[str]:
        motivos = []

        if candidato.idade < 16:
            motivos.append("Idade mínima não atingida")
        
        if not candidato.trabalho_em_equipe:
            motivos.append("Não atende aos requisitos de trabalho em equipe")
        
        if len(candidato.conhecimentos.intersection(self.conhecimentos)) < 3:
            motivos.append("Quantidade insuficiente de conhecimentos compatíveis")
        
        if candidato.turno not in self.turno:
            motivos.append("Turno não disponível")
        
        return motivos

    def calcular_pontuacao(self, candidato: Candidato) -> int:
        pontuacao = 0

        if candidato.trabalho_em_equipe:
            pontuacao += self.pontuacao.EQUIPE
        
        if candidato.turno in self.turno:
            pontuacao += self.pontuacao.TURNO
        
        pontuacao += len(
            candidato.conhecimentos.intersection(self.conhecimentos)
            ) * self.pontuacao.CONHECIMENTO
        
        if candidato.computador_proprio:
            pontuacao += self.pontuacao.COMPUTADOR_PROPRIO
        
        return pontuacao