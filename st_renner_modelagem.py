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

    # Cria o sub-título da seção
    st.markdown("<h4 style='color: #FF0000;'>Técnicas e Suposições</h4>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_modelagem = '''
        Baseando-se no artigo "A review on customer segmentation methods for personalized customer targeting in e-commerce use cases" [link](https://link.springer.com/article/10.1007/s10257-023-00640-4), optamos pela segmentação RFM por sua robustez e ampla utilização. Essa técnica será usada como baseline, pois é facilmente reproduzível com os dados da Renner, permitindo comparações com outros métodos.
    '''

    # Mostra o texto na página
    st.markdown(texto_modelagem)

    # Cria o sub-título da seção
    st.markdown("<h4 style='color: #FF0000;'>Avaliação de Score RFM</h4>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_modelagem2 = '''
    Utilizamos o score **RFM** como estratégia para segmentar consumidores em perfis de consumo. Amplamente adotado no marketing e na literatura de segmentação de clientes, o RFM avalia:
    - **Recência**: Tempo desde a última compra.
    - **Frequência**: Número de compras realizadas.
    - **Monetário**: Valor gasto pelo cliente.

    Os scores de **Frequência** e **Monetário** foram definidos com base em quantis, permitindo uma melhor distribuição de perfis. Já a **Recência** utilizou intervalos de 3 meses, que mostraram-se eficazes segundo análise empírica, alinhando-se à expectativa de compras em um e-commerce de moda.
    '''

    # Mostra o texto na página
    st.markdown(texto_modelagem2)

    # Dados para a tabela
    data = {
        "Score": [5, 4, 3, 2, 1],
        "Recência (em dias)": ["0-90", "[90-180]", "[180-270]", "[270-365]", "(365-"],
        "Frequência (em quantidade de compras)": ["(8-", "[6-8]", "[4-6]", "[2-4]", "[0-2]"],
        "Monetário (em reais)": ["(175-", "[150-175]", "[125-150]", "[100-125]", "[0-100]"]
    }

    # Criando o DataFrame
    df = pd.DataFrame(data)

    # Exibindo a tabela no Streamlit
    st.table(df)

    # Cria o texto da página
    texto_modelagem = '''
    A partir da geração de scores para as métricas de Recência, Frequência e Monetário, é possível criar clusters de clientes, baseando-se na metodologia do OmniConverter. Esses clusters ajudam no desenvolvimento de estratégias de marketing e fidelização. Abaixo, os principais grupos:

    - **Soulmates**: Clientes ideais, alta frequência e valor monetário. Priorize experiências positivas e atendimento especial.
    - **Lovers**: Promissores, com potencial de virar Soulmates. Aumente a confiança e frequência de compras.
    - **New Passions**: Novos clientes com alto potencial. Implementar onboarding e resolver problemas rapidamente pode evitar perdas.
    - **Flirting**: Novos clientes com menor frequência e valor. Estratégias de engajamento podem transformar em clientes leais.
    - **Apprentice**: Compraram 1-2 vezes com baixo valor. Abordagem com conversas para entender suas necessidades.
    - **Platonic Friends**: Ativos, fazem compras moderadas de valor médio.
    - **Potential Lovers**: Novos clientes com potencial de virarem Soulmates.
    - **About to Dump You**: Clientes inativos, é importante identificar motivos de afastamento e engajá-los novamente.
    - **Ex Lovers**: Clientes antigos com alta frequência e valor, mas que abandonaram a marca. Feedback é essencial para reconquistar ou ajustar estratégias.
    - **Don Juan**: Compraram poucas vezes, mas de alto valor. Investigue motivos e busque reengajamento.
    - **Break-Ups**: Clientes de baixo valor e alta taxa de devolução. Aceitar o churn e focar em segmentos mais promissores.
    '''

    # Mostra o texto na página
    st.markdown(texto_modelagem)

    # Dados da tabela
    data = {
        "Grupo": [
            "Soulmates", "Lovers", "New Passions", "Flirting", "Apprentice",
            "Platonic Friends", "Potential Lovers", "About to Dump You", 
            "Ex Lovers", "Don Juan", "Break Ups"
        ],
        "Score de Recência": [
            "5", "4-5", "5", "4", "4", "3-4", "5", "2-3", "1", "1", "1"
        ],
        "Score de Frequência": [
            "5", "3-5", "1", "1", "1", "3", "1", "1-5", "5", "1", "2"
        ],
        "Score Monetário": [
            "5", "3-5", "4-5", "4", "1", "3-4", "5", "1-5", "5", "5", "1"
        ]
    }

    # Cria o DataFrame
    df = pd.DataFrame(data)

    # Exibe a tabela no Streamlit
    st.table(df)

    # Texto resumido para colocar abaixo da tabela
    texto_adicional = '''
    Após aplicar a clusterização RFM, identificou-se que cerca de 50% dos clientes não se encaixavam em nenhum grupo definido, formando o grupo "No Profile". Para esses clientes, testou-se o algoritmo KNN para atribuí-los ao grupo mais próximo, mas surgiram problemas, como descaracterização de grupos.

    Uma solução sugerida foi o uso de um **KNN segmentado**, restringindo a análise a grupos específicos com características semelhantes, como score F > 2, garantindo maior precisão.

    Além disso, comparou-se o RFM com os algoritmos **KMeans** e **DBSCAN**. Usando KMeans, os clusters gerados foram muito diferentes dos 11 grupos do RFM, sugerindo necessidade de ajustes. A distribuição dos clusters foi a seguinte:
    - **Cluster 0**: 23.262 indivíduos
    - **Cluster 1**: 312 indivíduos
    - **Cluster 2**: 11 indivíduos

    Mais testes e iterações serão necessários para alinhar os resultados.
    '''

    # Mostra o texto adicional na página
    st.markdown(texto_adicional)