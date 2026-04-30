# Mini_projeto_2
Projeto LGPD

# 🔒 Mini Projeto 2 — LGPD

Projeto desenvolvido para a disciplina **Linguagem de Programação II** da **Fatec Rio Claro**, sob orientação do Prof. Orlando Saraiva Júnior.

O objetivo é aplicar os conceitos da **Lei Geral de Proteção de Dados (Lei nº 13.709/2018)** em um sistema que lê dados pessoais de um banco PostgreSQL, anonimiza as informações sensíveis e gera relatórios em arquivos CSV.

---

## 📋 Atividades

### Atividade 1 — Anonimização dos dados
A função `LGPD(row)` anonimiza os seguintes campos de cada registro:

| Campo | Original | Anonimizado |
|-------|----------|-------------|
| Nome | `Olivia Araújo` | `O***** A*****` |
| CPF | `237.615.809-59` | `237.***.***-**` |
| E-mail | `nuneserick@example.com` | `n*********@example.com` |
| Telefone | `+55 (011) 9483-6810` | `6810` |

### Atividade 2 — Arquivos por ano de nascimento
Gera um arquivo CSV por ano de nascimento com os dados **anonimizados**.
Exemplo: `1990.csv`, `1991.csv`, `1992.csv`...

### Atividade 3 — Arquivo com todos os registros
Gera um único arquivo `todos.csv` contendo apenas **nome** e **CPF** de todos os usuários, **sem anonimização**.

### Atividade 4 — Decorador de tempo com log
Utiliza o decorador `@medir_tempo` para medir e registrar em log o tempo de execução das Atividades 2 e 3.
O log é salvo no arquivo `execucao.log`.

---

## 🗂️ Estrutura do projeto

```
Mini_projeto_2/
│
├── lgpd.py               # Script principal com todas as atividades
├── decorator_tempo.py    # Decorador que mede e loga o tempo de execução
├── requirements.txt      # Dependências do projeto
├── execucao.log          # Log gerado automaticamente ao rodar
├── todos.csv             # Gerado pela Atividade 3
└── 1990.csv, 1991.csv... # Gerados pela Atividade 2
```

---

## 🏦 Banco de dados

| Campo | Valor |
|-------|-------|
| **HOST** | 200.19.224.150 |
| **USER** | alunos |
| **PASSWORD** | AlunoFatec |
| **DATABASE** | atividade2 |
| **PORTA** | 5432 |

---

## 🚀 Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/sarabiotto/Mini_projeto_2
cd Mini_projeto_2
```

### 2. Crie e ative o ambiente virtual
```bash
# Criar
python -m venv .venv

# Ativar no Windows
.venv\Scripts\activate

# Ativar no Mac/Linux
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o projeto
```bash
python lgpd.py
```

---

## 📦 Dependências

```
Faker==37.11.0
greenlet==3.2.4
psycopg2-binary==2.9.10
SQLAlchemy==2.0.43
typing_extensions==4.15.0
tzdata==2025.2
```

---

## 📚 Referências

- [Lei Geral de Proteção de Dados — Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- Myers, Jason; Copeland, Rick. **Essential SQLAlchemy**. 2. ed. O'Reilly Media, 2015.
- Ramalho, Luciano. **Fluent Python**. 2. ed. O'Reilly Media, 2022.

---

## 👨‍🏫 Informações acadêmicas

- **Instituição:** Fatec Rio Claro
- **Disciplina:** Linguagem de Programação II
- **Professor:** Orlando Saraiva Júnior


