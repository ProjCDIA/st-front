import streamlit as st
import plotly.express as px
import base64
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# Criar função para ler parquets e transformar em dataframe
def read_parquet(file_path: str) -> pd.DataFrame:
    """
    Lê arquivos parquet e transforma em dataframe.
    
    :param file_path: Caminho do arquivo parquet
    :return df: Dataframe com os dados do arquivo parquet
    """
    df = pd.read_parquet(file_path, engine='pyarrow')

    return df

def transform_clients(df_clientes: pd.DataFrame) -> pd.DataFrame:
    # Conversão das datas
    df_clientes['data_ultima_compra_renner'] = pd.to_datetime(df_clientes['data_ultima_compra_renner']).dt.date
    df_clientes['data_primeira_compra_renner'] = pd.to_datetime(df_clientes['data_primeira_compra_renner']).dt.date

    # Lista de todas as capitais brasileiras, incluindo o Distrito Federal, em maiúscula e sem acentuação
    capitais = [
        'ARACAJU', 'BELEM', 'BELO HORIZONTE', 'BOA VISTA', 'BRASILIA', 'CAMPO GRANDE', 
        'CUIABA', 'CURITIBA', 'FLORIANOPOLIS', 'FORTALEZA', 'GOIANIA', 'JOAO PESSOA', 
        'MACAPA', 'MACEIO', 'MANAUS', 'NATAL', 'PALMAS', 'PORTO ALEGRE', 'PORTO VELHO', 
        'RECIFE', 'RIO BRANCO', 'RIO DE JANEIRO', 'SALVADOR', 'SAO LUIS', 'SAO PAULO', 
        'TERESINA', 'VITORIA'
    ]

    # Adicionar coluna "capital" com a informação 1 quando Capital ou 0 quando outro
    df_clientes['capital'] = df_clientes['cidade'].apply(lambda x: 1 if x in capitais else 0)

    # Mapear os valores 0 e 1 para "Interior" e "Capital"
    df_clientes['capital_label'] = df_clientes['capital'].map({1: 'Capital', 0: 'Interior'})

    return df_clientes


def transform_navigation(df_navegacao: pd.DataFrame) -> pd.DataFrame:
    # Convertendo a data para o formato datetime
    df_navegacao['data_evento'] = pd.to_datetime(df_navegacao['data_evento'])

    return df_navegacao

def plot_graph(df: pd.DataFrame) -> None:
    # Gráfico 1: Distribuição de Idade dos Clientes
    plt.figure(figsize=(10, 6))
    sns.histplot(df['idade'], bins=10, color='red', kde=True)
    sns.despine(bottom=True, right=True)
    plt.title('Distribuição de Idade dos Clientes', fontsize=14)
    plt.xlabel('Idade')
    plt.ylabel('Número de Clientes')
    plt.grid(True, linestyle='-', linewidth=0.3)
    plt.show()