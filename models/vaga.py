from models.candidato import Candidato

class Vaga:
    def __init__(self, id: int, titulo: str, descricao: str, conhecimentos: set, turno: set):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.conhecimentos = conhecimentos
        self.turno = turno

    def validar_candidato(self, candidato: Candidato) -> list[str]:
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