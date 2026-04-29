from sqlalchemy import create_engine, MetaData, Table, Column, Integer
from sqlalchemy import String, Date, DateTime, text
from datetime import datetime
import csv
from collections import defaultdict
from decorator_tempo import medir_tempo

engine = create_engine("postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2")
metadata = MetaData()

usuarios = Table(
    'usuarios', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False, index=True),
    Column('cpf', String(14), nullable=False),
    Column('email', String(100), nullable=False, unique=True),
    Column('telefone', String(20), nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

def anonimizar_nome(nome):
    partes = nome.split()
    return ' '.join(p[0] + '*' * (len(p) - 1) for p in partes)

def anonimizar_cpf(cpf):
    return cpf[:3] + '.***.***-**'

def anonimizar_email(email):
    usuario, dominio = email.split('@')
    return usuario[0] + '*' * (len(usuario) - 1) + '@' + dominio

def anonimizar_telefone(telefone):
    digitos = ''.join(filter(str.isdigit, telefone))
    return digitos[-4:]

def LGPD(row):
    return (
        row[0],                          
        anonimizar_nome(row[1]),         
        anonimizar_cpf(row[2]),           
        anonimizar_email(row[3]),        
        anonimizar_telefone(row[4]),     
        row[5],                          
        row[6],                          
        row[7]                            
    )

users = []
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios LIMIT 10;"))
    for row in result:
        row = LGPD(row)
        users.append(row)

for u in users:
    print(u)


dados_por_ano = defaultdict(list)

def gerar_csv_por_ano():
    dados_por_ano = defaultdict(list)

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM usuarios;"))
        for row in result:
            row_anon = LGPD(row)
            ano = row[5].year
            dados_por_ano[ano].append(row_anon)

    for ano, registros in dados_por_ano.items():
        with open(f'{ano}.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            writer.writerow(['id', 'nome', 'cpf', 'email', 'telefone', 'data_nascimento', 'created_on', 'updated_on'])
            for r in registros:
                writer.writerow([
                    r[0],      
                    r[1],       
                    r[2],     
                    r[3],       
                    r[4],       
                    str(r[5]),  
                    str(r[6]),
                    str(r[7])  
                ])

        print(f'Arquivo {ano}.csv gerado com {len(registros)} registros.')

medir_tempo
gerar_csv_por_ano()

def gerar_todos():
    with open('todos.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow(['nome', 'cpf'])

        with engine.connect() as conn:
            result = conn.execute(text("SELECT nome, cpf FROM usuarios;"))
            for row in result:
                writer.writerow([
                    row[0],   
                    row[1]    
                ])

    print('Arquivo todos.csv gerado com sucesso!')

medir_tempo
gerar_todos()