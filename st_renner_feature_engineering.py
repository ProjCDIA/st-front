import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

def main():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Feature Engineering</h3>", unsafe_allow_html=True)

    # Cria o sub-título da seção
    st.markdown("<h4 style='color: #FF0000;'>Criação de atributos e registros</h4>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_fe = '''
        Foi verificado que um mesmo item possuía diversos valores de venda e para tentar entender melhor esse comportamento, criamos um dataset auxiliar em que capturamos o preço mínimo, médio, máximo e a moda do preço para cada item. 
        Com essas informações, pudemos calcular o desvio padrão, amplitude e coeficiente de variação de cada um dos itens, totalizando 186.127 itens. 
        
        Com objetivo de reduzir outliers, aplicamos as seguintes regras em sequência: 

        - Descartar Itens com moda do preço menor do que R$1,00. 
        - Descartar itens com desvio padrão calculado a partir de 1,5. 

        Na base de clientes criamos métricas para cada indivíduo, com dados de contagem de comprar por modalidade e por tipo de produto. Calculamos a diferença entre a primeira e a última compra, total de compras, tempo médio entre compras e ticket médio. Além disso, fizemos uma classificação se este cliente é de uma capital ou não. 

        Para os registros de navegação, aplicamos somente dados de contagem de cada evento por cliente. 
    '''

    # Mostra o texto na página
    st.markdown(texto_fe)

    # Cria o sub-título da seção
    st.markdown("<h4 style='color: #FF0000;'>Integração de dados</h4>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_integracao= '''
        Como recebemos bases com 3 perspectivas diferentes (Cliente, Navegação, Transação), utilizamos como chave primária em todas elas o campo id_cliente, dessa forma, foi possível unir todas as tabelas e criar um dataset completo com foco nos clientes, seus dados e características agregadas. 

        Após as junções, totalizamos 23.664 clientes diferentes.  
    '''

    # Mostra o texto na página
    st.markdown(texto_integracao)