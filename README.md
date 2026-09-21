# Cadastro de Candidatos para Seleção Acadêmica

Este projeto é uma aplicação simples em Python para realizar o cadastro de candidatos e avaliar sua elegibilidade para um projeto acadêmico. A lógica foi organizada em classes e módulos, utilizando estruturas como `set` para armazenar conhecimentos e `dict` para centralizar regras de pontuação e critérios de desclassificação.

## Objetivo

O sistema coleta dados do candidato, valida requisitos mínimos e calcula uma pontuação final para decidir se ele:

- é aprovado;
- entra na lista de espera;
- é desclassificado.

## Estrutura do projeto

```text
candidato/
├── main.py
├── models/
│   ├── candidato.py
│   └── constantes.py
├── validators/
│   └── candidato_validator.py
└── README.md
```

## Descrição dos módulos

### main.py
Arquivo principal da aplicação. Ele:

1. cria um candidato via `Candidato.cadastrar()`;
2. valida os conhecimentos do candidato;
3. verifica os motivos de desclassificação;
4. calcula a pontuação final;
5. imprime o resultado da seleção.

### models/candidato.py
Define a classe `Candidato`, responsável por armazenar os dados do participante e pela coleta dos dados via entrada do terminal.

Principais recursos:

- `__slots__`: limita os atributos da classe para organização e controle de memória;
- `__init__`: inicializa os dados do candidato;
- `__str__`: retorna uma representação textual do candidato;
- `_gerar_matricula()`: gera uma matrícula com base no nome, no curso e no semestre;
- `cadastrar()`: método de classe que coleta os dados do usuário pelo input.

O atributo `conhecimentos` é armazenado como `set`, o que evita duplicatas e permite operações de interseção, diferença e comparação com os requisitos exigidos.

### models/constantes.py
Centraliza as regras do projeto em dicionários e conjuntos.

- `PONTUACAO`: define os pontos atribuídos por equipe, computador, turno e conhecimentos;
- `CONHECIMENTOS_EXIGIDOS`: conjunto com os conhecimentos mínimos exigidos;
- `TURNOS_DISPONIVEIS`: turnos permitidos;
- `MOTIVOS_DESAPROVACAO`: mensagens utilizadas quando o candidato é recusado.

### validators/candidato_validator.py
Contém as funções que validam o perfil do candidato.

#### `validar_conhecimentos(candidato)`
Compara os conhecimentos do candidato com os requisitos mínimos.

- `conhecimentos_compativeis`: interseção entre os conhecimentos do candidato e os exigidos;
- `conhecimentos_faltantes`: diferença entre os requisitos exigidos e os conhecimentos do candidato.

#### `calcular_pontuacao(candidato, conhecimentos_compativeis)`
Calcula a pontuação final com base em:

- trabalho em equipe;
- disponibilidade de turno;
- número de conhecimentos compatíveis;
- possuir computador próprio.

#### `validar_desclassificacao(idade, trabalho_em_equipe, conhecimentos_compativeis, conhecimentos_faltantes, turno)`
Verifica se o candidato deve ser rejeitado por algum motivo, como:

- idade menor que 16 anos;
- não aceita trabalho em equipe;
- menos de 3 conhecimentos compatíveis;
- turno não disponível para o projeto.

## Regras de seleção

As regras implementadas no projeto são:

- candidato menor de 16 anos é desclassificado;
- quem não aceita trabalhar em equipe é desclassificado;
- devem existir pelo menos 3 conhecimentos compatíveis;
- turno deve ser `manhã` ou `tarde`;
- a pontuação final decide o resultado.

## Fluxo da aplicação

1. O usuário informa seus dados pessoais.
2. O sistema cria um objeto `Candidato`.
3. A aplicação compara os conhecimentos com a lista exigida.
4. São verificadas as condições de desclassificação.
5. A pontuação total é calculada.
6. O programa exibe a classificação final.

## Como executar

No terminal, na raiz do projeto, execute:

```bash
python main.py
```

## Exemplo de funcionamento

O programa solicita as seguintes informações:

- Nome
- Idade
- Curso
- Semestre
- Email
- Turno disponível
- Trabalho em equipe
- Possui computador próprio
- Conhecimentos separados por vírgula

Depois, ele retorna uma classificação como:

- `APROVADO`
- `Banco de talentos`
- `NÃO APROVADO`

## Observações

Este projeto demonstra bem o uso de:

- classes em Python;
- estruturas `set` para manipulação de conhecimento;
- dicionários para regras de negócio;
- validação por funções independentes;
- organização por módulos e pacotes.

## Tecnologias utilizadas

- Python 3
- Estruturas nativas do Python (`set`, `dict`, `list`)
- Entrada via terminal (`input()`)
