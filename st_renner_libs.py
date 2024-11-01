import streamlit as st
import plotly.express as px
import base64
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

# Criar função para ler parquets e transformar em dataframe
def read_parquet(file_path):
    """
    Função para ler arquivos parquet e transformar em dataframe.
    
    :param file_path: Caminho do arquivo parquet
    :return df: Dataframe com os dados do arquivo parquet
    """
    df = pd.read_parquet(file_path)

    return df