from datetime import datetime
from models.candidato import Candidato
from models.vaga import Vaga

class Inscricao:
    def __init__(self, candidato: Candidato, vaga: Vaga):
        self.candidato = candidato
        self.vaga = vaga
        self.inscricao = f"{candidato.matricula}-{vaga.id}"
        self.data_inscricao = datetime.now()
        self.pontuacao = self.calcular_pontuacao()
        self.status = self.validar_status()

    def validar_status(self) -> str:
        motivos = self.vaga.validar_requisitos(self.candidato)

        if motivos:
            return "NÃO APROVADO"
        else:
            return "APROVADO"

    def calcular_pontuacao(self) -> int:
        return self.vaga.calcular_pontuacao(self.candidato)