import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

def main():
    # Cria o título da página
    st.markdown("<h1 style='color: #FF0000;'>Renner ReThink.</h1>", unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>ETL</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_etl = '''
        - Casos com idade negativa:
            - Valor absoluto destas idades 
        - Nova distribuição dos valores ficou conforme abaixo: 
    '''

    # Mostra o texto na página
    st.markdown(texto_etl)

    # Insere uma imagem na página
    st.image('dist_idades_corrigida.png', use_container_width=True)

    # Cria o texto da página
    texto_idade_corrigida = '''
        - Verificamos 23 clientes cuja data da primeira compra na Renner estava registrada como posterior a data da última compra
        - Fizemos a inversão dos registros para corrigir o problema
    '''

    # Mostra o texto na página
    st.markdown(texto_idade_corrigida)

    # Insere uma imagem na página
    st.image('intervalo_entre_compras.png', use_container_width=True)

    # Insere uma imagem na página
    st.image('newplot.png', use_container_width=True)
