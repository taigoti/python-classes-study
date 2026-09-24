from datetime import datetime
from models.candidato import Candidato
from models.vaga import Vaga

class Inscricao:
    def __init__(self, candidato: Candidato, vaga: Vaga):
        self.candidato = candidato
        self.vaga = vaga
        self.inscricao = f"{candidato.matricula}-{vaga.id}"
        self.data_inscricao = datetime.now()
        self.pontuacao = 0