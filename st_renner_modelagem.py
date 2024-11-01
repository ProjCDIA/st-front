import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

def main():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Modelagem</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_modelagem = '''
        A etapa de modelagem envolve a aplicação de algoritmos de machine learning para segmentar os clientes de acordo com características semelhantes.
        
        Exemplo de código de modelagem:
    '''

    # Mostra o texto na página
    st.markdown(texto_modelagem)