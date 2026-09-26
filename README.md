# Cadastro de Candidatos para Seleção Acadêmica

Este projeto em Python simula um processo de inscrição e avaliação de candidatos para uma vaga acadêmica. A estrutura atual foi organizada em classes e módulos, com uso de `set` para armazenar conhecimentos e `dict` para definir os critérios de pontuação de cada oportunidade.

## Objetivo

O sistema coleta dados do candidato, valida os requisitos mínimos da vaga, calcula uma pontuação final e decide se a inscrição será:

- `APROVADA`;
- `NÃO APROVADA`.

## Estrutura do projeto

```text
candidato/
├── main.py
├── models/
│   ├── candidato.py
│   ├── vaga.py
│   └── inscricao.py
├── README.md
└── .gitignore
```

## Descrição dos módulos

### main.py
Arquivo principal da aplicação. Ele:

1. instancia um objeto `Candidato`;
2. cria uma `Vaga` com requisitos e pontuação;
3. gera uma `Inscricao` vinculando candidato e vaga;
4. exibe os dados e o status final da inscrição.

### models/candidato.py
Define a classe `Candidato`, responsável por armazenar os dados pessoais do participante e gerar a matrícula do candidato.

Principais recursos:

- `__slots__`: limita os atributos da classe para organização e controle de memória;
- `__init__`: inicializa os dados do candidato;
- `__str__`: retorna uma representação textual do candidato;
- `_gerar_matricula()`: gera uma matrícula com base no nome, no curso e no semestre;
- `cadastrar()`: coleta os dados via entrada do terminal.

O atributo `conhecimentos` é armazenado como `set`, evitando duplicatas e permitindo comparações com os requisitos da vaga.

### models/vaga.py
Define a classe `Vaga`, que representa uma oportunidade disponível para inscrição.

Principais recursos:

- `validar_requisitos(candidato)`: verifica se o candidato atende aos requisitos mínimos e retorna a lista de motivos de desclassificação;
- `calcular_pontuacao(candidato)`: soma os pontos com base em trabalho em equipe, turno, conhecimentos e computador próprio;
- `conhecimentos`: conjunto de requisitos exigidos pela vaga;
- `turno`: turnos permitidos para a vaga;
- `pontuacao`: dicionário com os valores usados no cálculo da pontuação.

### models/inscricao.py
Define a classe `Inscricao`, responsável por relacionar um candidato a uma vaga.

Principais recursos:

- `inscricao`: identifica a inscrição no formato `matricula-vaga`;
- `data_inscricao`: data e hora em que a inscrição foi criada;
- `pontuacao`: pontuação calculada com base na vaga e no candidato;
- `status`: indica se a inscrição foi aprovada ou não;
- `validar_status()`: chama a validação da vaga e define o resultado final.

## Regras de seleção

As regras implementadas no projeto são:

- candidato menor de 16 anos é desclassificado;
- quem não aceita trabalhar em equipe é desclassificado;
- devem existir pelo menos 3 conhecimentos compatíveis com a vaga;
- turno do candidato deve estar disponível para a oportunidade;
- a pontuação final é calculada e utilizada para avaliar a inscrição.

## Fluxo da aplicação

1. O usuário informa seus dados pessoais.
2. O sistema cria um objeto `Candidato`.
3. A aplicação define uma `Vaga` com requisitos e critérios de pontuação.
4. A inscrição compara os conhecimentos e valida os requisitos.
5. A pontuação total é calculada.
6. O programa exibe o status final da inscrição.

## Como executar

No terminal, na raiz do projeto, execute:

```bash
python main.py
```

## Exemplo de funcionamento

O programa cria um candidato, uma vaga e uma inscrição de forma direta para demonstrar o fluxo do sistema.

### Dados de exemplo

- Nome: João Silva
- Idade: 20
- Curso: Engenharia de Software
- Semestre: 3
- Email: joao.silva@me.com
- Turno: tarde
- Trabalho em equipe: Sim
- Computador próprio: Sim
- Conhecimentos: Python, SQL

### Resultado esperado

```text
Inscrição: j e 3 123 - 1
Data da inscrição: 2026-09-26 10:35:00
Pontuação: 11
Status: APROVADO
```

O exemplo acima representa a estrutura atual do projeto, em que a decisão é baseada em requisitos da vaga e pontuação acumulada.

## Observações

Este projeto demonstra bem o uso de:

- classes em Python;
- estruturas `set` para manipulação de conhecimentos;
- dicionários para regras de negócio e pontuação;
- organização por módulos e pacotes;
- modelagem orientada a objetos para candidatos, vagas e inscrições.

## Tecnologias utilizadas

- Python 3
- Estruturas nativas do Python (`set`, `dict`, `list`)
- Entrada via terminal (`input()`)
- Manipulação de datas com `datetime`
