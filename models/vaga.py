class Vaga:
    def __init__(self, id: int, titulo: str, descricao: str, conhecimentos: set, turno: set):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.conhecimentos = conhecimentos
        self.turno = turno
