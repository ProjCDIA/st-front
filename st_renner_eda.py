import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
from st_renner_libs import read_parquet, transform_clients, transform_navigation, plot_graph

def main():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Análise Exploratória</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_analise_exp = '''
        - Objetivo principal: entender a distribuição, características e particularidades dos dados
        - Para garantir um melhor entendimento e possibilitando o grupo a escolher as melhores abordagens para serem aplicadas tanto na preparação, quanto na modelagem do problema. 

        Abaixo, algumas observações feitas pelo grupo:
    '''

    # Mostra o texto na página
    st.markdown(texto_analise_exp)

    # Insere uma imagem na página
    st.image('dist_idade_clientes.png', use_container_width=True)

    # Cria o texto da página
    texto_idade = '''
        - Casos com idade negativa
            - Análise dos valores indicou que podem ser facilmente tratados tomando-se o valor absoluto das idades
    '''

    # Mostra o texto na página
    st.markdown(texto_idade)

    # Insere uma imagem na página
    st.image('dist_genero_clientes.png', use_container_width=True)

    # Cria o texto da página
    texto_genero = '''
        - Grande predominância de clientes do sexo feminino, o que era esperado considerando as tendências de clientes do negócio da organização parceira
    '''

    # Mostra o texto na página
    st.markdown(texto_genero)

    # Insere uma imagem na página
    st.image('dist_cidades.png', use_container_width=True)

    # Cria o texto da página
    texto_cidades = '''
        - São Paulo e Rio de Janeiro representam 20% do número total de clientes
        - Adicionando-se Porto Alegre e Brasília obtém-se pouco mais de 25%, o que demonstra como as duas primeiras cidades possuem grande representatividade no dataset
    '''

    # Mostra o texto na página
    st.markdown(texto_cidades)

    # Insere uma imagem na página
    st.image('eventos_navegacao.png', use_container_width=True)

    # Cria o texto da página
    texto_eventos = '''
        - Predominante a presença dos eventos 'view_item' e 'select_item', tendo os demais eventos poucos registros
    '''

    # Mostra o texto na página
    st.markdown(texto_eventos)

    # Insere uma imagem na página
    st.image('tipo_venda.png', use_container_width=True)

    # Cria o texto da página
    texto_tipo_vendas = '''
        - Grande diferença de registros quando comparadas compras Online e Offline
        - Vendas Online representam em torno de 1/3 do total de vendas 
    '''

    # Mostra o texto na página
    st.markdown(texto_tipo_vendas)

    # Insere uma imagem na página
    st.image('valor_por_categoria.png', use_container_width=True)

    # Cria o texto da página
    texto_valores = '''
        - Os valores das vendas por categoria têm certo equilíbrio nos dados
        - Porém, ainda existem muitos outliers que deverão ser tratados 
    '''

    # Mostra o texto na página
    st.markdown(texto_valores)

    # Insere uma imagem na página
    st.image('itens_mais_vendidos.png', use_container_width=True)

    # Cria o texto da página
    texto_top10_total = '''
        - Avaliando os 10 itens com maior valor total em vendas, podemos perceber que há um item com Código 108799 que possui valor total acima de 2 milhões de reais
            - O segundo item que mais vende (Código 77850) possui um total de pouco mais de 115 mil reais
            - Supõe-se que possa haver algum tipo de erro para o primeiro caso que deverá ser tratado
    '''

    # Mostra o texto na página
    st.markdown(texto_top10_total)