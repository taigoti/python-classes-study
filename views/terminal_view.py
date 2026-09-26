from models.candidato import Candidato

def input_candidato() -> Candidato:
    nome = str(input("Nome: ").strip())
    idade = int(input("Idade: "))
    curso = str(input("Curso: ").strip())
    semestre = int(input("Semestre: "))

    while True:
        email = str(input("Email: ").strip()).lower()

        if '@' in email and '.' in email:
            break

        print("Digite um email válido!")

    turno = str(input("Turno disponível (manhã/tarde/noite): ").strip())

    trabalho_em_equipe = input(
        "Trabalho em equipe? (s/n): ").strip().lower() == 'sim'
    
    computador_proprio = input(
        "Possui computador próprio? (s/n): ").strip().lower() == 'sim'
    
    input_conhecimentos = input("Conhecimentos (separados por vírgula): ").strip().split(',')
    conhecimentos = {conhecimento.strip() for conhecimento in input_conhecimentos if conhecimento.strip()}

    return Candidato(
        nome=nome,
        idade=idade,
        curso=curso,
        semestre=semestre,
        email=email,
        turno=turno,
        trabalho_em_equipe=trabalho_em_equipe,
        computador_proprio=computador_proprio,
        conhecimentos=conhecimentos
    )