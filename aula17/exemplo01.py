from sqlalchemy import create_engine
import pandas as pd
# pip install python-dotenv
from dotenv import load_dotenv
import os

# *******Início do código*******
# Carrega variáveis de ambiente
load_dotenv()

def conecta_banco():

    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    # Url de conexão com o banco
    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}{database}'
    )
    return engine
# Chama a função que conecta ao banco
engine = conecta_banco()

try:
    df_usuarios = pd.read_sql('tb_usuarios', engine)
    print(df_usuarios)

    df_livros = pd.read_sql('tb_livros', engine)
    print(df_livros)
    
    df_alugados = pd.read_sql('tb_alugados', engine)
    print(df_alugados)

    df_itens = pd.read_sql('tb_itens_alugados', engine)
    print(df_itens)



except Exception as e:
    print(f'Erro ao conectar aos dados {e}')

# Relacionando os dataframes com Merge
try:
    df_merge1 = pd.merge(
        df_livros, df_itens, on= 'id_livro '

    )
    df_merge2 = pd.merge(
        df_merge1, df_alugados, 'id_aluguel'
    )
    df_dados = pd.merge(
        df_merge2,df_usuarios, left_on= 'id usuario', rigth_on= 'id_usuario'
            )
    print(df_dados)

except Exception as e:
    print(f'Erro ao conectar aos dados {e}')

# Filtro para Novembro
try:
    df_novembro= df_dados[(
        (df_dados['data_devolução'] >= '2024-11-01') & 
        (df_dados['data_devolução'] <= '2024-11-30')
    )]
    print(df_novembro[
        [
            'id_usuario', 'nome', 
            'id_aluguel', 'data_aluguel', 'data_devolução'
            'id_livro','titulo'
        ]
    ])

except Exception as e:
    print(f'Erro ao conectar aos dados {e}')