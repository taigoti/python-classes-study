from models.candidato import Candidato
from models.enums import Turno, Pontuacao

class Vaga:
    def __init__(self, id: int, titulo: str, descricao: str, conhecimentos: set, turno: Turno, pontuacao: Pontuacao):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.conhecimentos = conhecimentos
        self.turno = turno
        self.pontuacao = pontuacao

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