from datetime import datetime
from models.candidato import Candidato
from models.vaga import Vaga

class Inscricao:
    def __init__(self, candidato: Candidato, vaga: Vaga):
        self.candidato = candidato
        self.vaga = vaga
        self.inscricao = f"{candidato.matricula}-{vaga.id}"
        self.data_inscricao = datetime.now()
        self.motivos = self.validar_requisitos()
        self.status = self.validar_status()
        self.pontuacao = self.calcular_pontuacao()

    def validar_requisitos(self) -> list[str]:
        return self.vaga.validar_requisitos(self.candidato)
    
    def validar_status(self) -> str:    
        if self.motivos:
            return "NÃO APROVADO"
        else:
            return "APROVADO"

    def calcular_pontuacao(self) -> int:
        return self.vaga.calcular_pontuacao(self.candidato)