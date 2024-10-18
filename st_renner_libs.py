import streamlit as st
import plotly.express as px
import base64
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

def descricao_projeto():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Descrição do Projeto</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_descricao_problema = '''
        Com o crescente aumento do uso de e-commerce, diversidade de produtos e serviços disponíveis, e características distintas de clientes que utilizam este tipo de plataforma, estratégias que funcionavam de maneira eficiente tempos atrás, podem não responder tão bem às demandas atuais. 

        Conseguir identificar de maneira correta as diferenças fundamentais entre grupos de clientes e a partir disso, ser capaz de elaborar estratégias ideais para cada grupo é um desafio contemporâneo e dinâmico, mas que tem se tornado um diferencial importante na retenção e incremento de receitas. 
    '''

    # Mostra o texto na página
    st.markdown(texto_descricao_problema)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Descrição da Solução Proposta</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_descricao_solucao = '''
        Como proposta de trabalho, o grupo planeja desenvolver uma ferramenta chamada “Renner 
        Rethink”, que visa analisar cada cliente sob diversos prismas e agrupá-los através de técnicas de 
        Clusterização, para identificar os produtos mais relevantes a serem oferecidos para cada grupo de 
        clientes. 
        Os entregáveis serão feitos através de páginas web com as seguintes funções: 
        - Detalhamentos das análises e tratamento dos dados 
        - Modelagem interativa, onde a Renner pode executar testes e avaliar resultados sobre os modelos 
        - Relatório em PDF com toda a explicação do projeto baseado no CRISP-DM
    '''

    # Mostra o texto na página
    st.markdown(texto_descricao_solucao)

def compreensao_negocio():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Background</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_background = '''
        - Mercado de e-commerce cada vez mais concorrido:
            - Maior oferta e diversidade de opções 
            - Clientes podem rapidamente encontrar informações relevantes sobre suas demandas
        - Entender o comportamento do público
        - Definir estratégias competitivas
        - Ser acurado na identificação de campanhas atrativas para diferentes grupos 
            - Peça-chave na prospecção e fidelização de clientes 

        - Grupo Renner: um dos players mais importantes no país
            - Busca ser referência no uso de dados para inteligência de mercado
            - Alinhando tecnologia aos produtos de moda, decoração, financeiro e serviços
    '''

    # Mostra o texto na página
    st.markdown(texto_background)

    # Cria o sub-título da seção
    st.markdown("<h4 style='color: #FF0000;'>Objetivos de Negócio</h4>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_objetivos_negocio = '''        
        - Encontrar agrupamentos de clientes com base no estágio de vida e padrão de consumo
        - Buscar identificar quais produtos e canais são mais aderentes ao seus gostos
        - Hipótese: estes segmentos refletem necessidades e preferências distintas, permitindo:
            - Campanhas de marketing mais direcionadas e personalizadas
            - Estratégias de vendas otimizadas
    '''

    # Mostra o texto na página
    st.markdown(texto_objetivos_negocio)

    # Cria o sub-título da seção
    st.markdown("<h4 style='color: #FF0000;'>Critérios de Sucesso</h4>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_criterios_negocio = '''
        - Técnico:
            - Métricas consolidadas para avaliação dos clusters
            - Capacidade de representar segmentos distintos de clientes baseado nas características comuns entre indivíduos de um mesmo cluster. 

        - Negócio: 
            - Clusters explicáveis e coerentes, com caracterização clara de similaridade e diferenciação. 
            - Resultados e características dos clusters coerentes e alinhados com as expectativas da Renner. 
        '''

    # Mostra o texto na página
    st.markdown(texto_criterios_negocio)

def eda():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Análise Exploratória</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_analise_exp = '''
        - Objetivo principal: entender a distribuição, características e particularidades dos dados
        - Para garantir um melhor entendimento e possibilitando o grupo a escolher as melhores abordagens para serem aplicadas tanto ne preparação, quanto na modelagem do problema. 

        Abaixo, algumas observações feitas pelo grupo:
    '''

    # Mostra o texto na página
    st.markdown(texto_analise_exp)

    # Insere uma imagem na página
    st.image('dist_idade_clientes.png', use_column_width=True)

    # Cria o texto da página
    texto_idade = '''
        - Casos com idade negativa
            - Análise dos valores indicou que podem ser facilmente tratados tomando-se o valor absoluto das idades
    '''

    # Mostra o texto na página
    st.markdown(texto_idade)

    # Insere uma imagem na página
    st.image('dist_genero_clientes.png', use_column_width=True)

    # Cria o texto da página
    texto_idade = '''
        - Grande predominância de clientes do sexo feminino, o que era esperado considerando as tendências de clientes do negócio da organização parceira
    '''

    # Mostra o texto na página
    st.markdown(texto_idade)

    # Insere uma imagem na página
    st.image('dist_cidades.png', use_column_width=True)

    # Cria o texto da página
    texto_cidades = '''
        - São Paulo e Rio de Janeiro representam 20% do número total de clientes
        - Adicionando-se Porto Alegre e Brasília obtém-se pouco mais de 25%, o que demonstra como as duas primeiras cidades possuem grande representatividade no dataset
    '''

    # Mostra o texto na página
    st.markdown(texto_cidades)

    # Insere uma imagem na página
    st.image('eventos_navegacao.png', use_column_width=True)

    # Cria o texto da página
    texto_eventos = '''
        - Predominante a presença dos eventos 'view_item' e 'select_item', tendo os demais eventos poucos registros
    '''

    # Mostra o texto na página
    st.markdown(texto_eventos)

    # Insere uma imagem na página
    st.image('tipo_venda.png', use_column_width=True)

    # Cria o texto da página
    texto_tipo_vendas = '''
        - Grande diferença de registros quando comparadas compras Online e Offline
        - Vendas Online representam em torno de 1/3 do total de vendas 
    '''

    # Mostra o texto na página
    st.markdown(texto_tipo_vendas)

    # Insere uma imagem na página
    st.image('valor_por_categoria.png', use_column_width=True)

    # Cria o texto da página
    texto_valores = '''
        - Os valores das vendas por categoria têm certo equilíbrio nos dados
        - Porém, ainda existem muitos outliers que deverão ser tratados 
    '''

    # Mostra o texto na página
    st.markdown(texto_valores)

    # Insere uma imagem na página
    st.image('itens_mais_vendidos.png', use_column_width=True)

    # Cria o texto da página
    texto_top10_total = '''
        - Avaliando os 10 itens com maior valor total em vendas, podemos perceber que há um item com Código 108799 que possui valor total acima de 2 milhões de reais
            - O segundo item que mais vende (Código 77850) possui um total de pouco mais de 115 mil reais
            - Supõe-se que possa haver algum tipo de erro para o primeiro caso que deverá ser tratado
    '''

    # Mostra o texto na página
    st.markdown(texto_top10_total)


def etl():
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
    st.image('dist_idades_corrigida.png', use_column_width=True)

    # Cria o texto da página
    texto_idade_corrigida = '''
        - Verificamos 23 clientes cuja data da primeira compra na Renner estava registrada como posterior a data da última compra
        - Fizemos a inversão dos registros para corrigir o problema
    '''

    # Mostra o texto na página
    st.markdown(texto_idade_corrigida)

    # Insere uma imagem na página
    st.image('intervalo_entre_compras.png', use_column_width=True)


def feature_engineering():
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


def modelagem():
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

    df_final = pd.read_csv('./cliente_final.csv', sep=';', index_col='id_cliente')
    df_final['data_ultima_compra_renner'] = pd.to_datetime(df_final['data_ultima_compra_renner'])
    df_final['dias_ultima_compra_renner'] = (df_final['data_ultima_compra_renner'].max() - df_final['data_ultima_compra_renner']).dt.days
    df_final['purchase'] = df_final['purchase'].apply(lambda x: float(x.replace(',', '.')))
    df_final['ticket_medio'] = df_final['ticket_medio'].apply(lambda x: float(x.replace(',', '.')))
    df_final = df_final[df_final['ticket_medio'] > 0]
    df_final['intervalo_medio'] = df_final['intervalo_medio'].apply(lambda x: float(x.replace(',', '.')))
    conditions = [
        (df_final['dias_ultima_compra_renner'] == 0),
        (df_final['dias_ultima_compra_renner'] > 1) & (df_final['dias_ultima_compra_renner'] < 5)
    ]
    choices = [0, 1]
    # Recency conditions
    recency_conditions = [
        (df_final['dias_ultima_compra_renner'] < 90),
        (df_final['dias_ultima_compra_renner'] >= 90) & (df_final['dias_ultima_compra_renner'] <= 180),
        (df_final['dias_ultima_compra_renner'] > 180) & (df_final['dias_ultima_compra_renner'] <= 270),
        (df_final['dias_ultima_compra_renner'] > 270) & (df_final['dias_ultima_compra_renner'] <= 365),
        (df_final['dias_ultima_compra_renner'] > 365)
    ]
    recency_choices = [5, 4, 3, 2, 1]

    # Frequency conditions
    frequency_conditions = [
        (df_final['total_compras'] < 5),
        (df_final['total_compras'] >= 5) & (df_final['total_compras'] <= 10),
        (df_final['total_compras'] >= 10) & (df_final['total_compras'] <= 15),
        (df_final['total_compras'] >= 15) & (df_final['total_compras'] <= 20),
        (df_final['total_compras'] > 20)
    ]
    frequency_choices = [1, 2, 3, 4, 5]

    # Monetary Conditions

    monetary_conditions = [
        (df_final['ticket_medio'] < 200),
        (df_final['ticket_medio'] >= 200) & (df_final['ticket_medio'] <= 400),
        (df_final['ticket_medio'] >= 400) & (df_final['ticket_medio'] <= 600),
        (df_final['ticket_medio'] >= 600) & (df_final['ticket_medio'] <= 800),
        (df_final['ticket_medio'] > 800)
    ]
    monetary_choices = [1, 2, 3, 4, 5]
    df_final['Recency Score'] = np.select(recency_conditions, recency_choices)
    df_final['Frequency Score'] = np.select(frequency_conditions, frequency_choices)
    df_final['Monetary Score'] = np.select(monetary_conditions, monetary_choices)
    profile_conditions = [
        (df_final['Recency Score'] == 5) & (df_final['Frequency Score'] == 5) & (df_final['Monetary Score'] == 5), # Soulmates
        (df_final['Recency Score'] >= 4) & (df_final['Frequency Score'] >= 3) & (df_final['Monetary Score'] >= 3), # Lovers
        (df_final['Recency Score'] == 5) & (df_final['Frequency Score'] == 1) & (df_final['Monetary Score'] >= 4), # New Passions
        (df_final['Recency Score'] == 4) & (df_final['Frequency Score'] == 1) & (df_final['Monetary Score'] == 4), # Flirting
        (df_final['Recency Score'] == 4) & (df_final['Frequency Score'] == 1) & (df_final['Monetary Score'] == 1), # Apprentice
        (df_final['Recency Score'] >= 2) & (df_final['Recency Score'] <= 3) & (df_final['Frequency Score'] >= 1) & (df_final['Monetary Score'] >= 1), # About to Dump You
        (df_final['Recency Score'] == 1) & (df_final['Frequency Score'] == 5) & (df_final['Monetary Score'] == 5), # Ex Lovers
        (df_final['Recency Score'] == 1) & (df_final['Frequency Score'] == 1) & (df_final['Monetary Score'] == 5), # Don Juan
        (df_final['Recency Score'] == 1) & (df_final['Frequency Score'] == 2) & (df_final['Monetary Score'] == 1), # Break-ups
        (df_final['Recency Score'] == 5) & (df_final['Frequency Score'] == 1) & (df_final['Monetary Score'] == 5), # Potencial Lovers
        (df_final['Recency Score'] >= 3) & (df_final['Recency Score'] <= 4) & (df_final['Frequency Score'] == 3) & (df_final['Monetary Score'] >= 3) & (df_final['Monetary Score'] <= 4), # Platonic Friends
    ]

    profile_choices = ['Soulmates', 'Lovers', 'New Passions', 'Flirting', 'Apprentice', 'About to Dump You', 'Ex Lovers', 'Don Juan', 'Break-ups', 'Potential Lovers', 'Platonic Friends']
    df_final['Profile'] = np.select(profile_conditions, profile_choices, 'No Profile')

    # Criar um mapeamento para os valores categóricos de 'Profile'
    profile_categories = df_final['Profile'].astype('category').cat.codes

    # Criar gráfico 3D de dispersão
    fig = go.Figure(data=[go.Scatter3d(
        x=df_final['dias_ultima_compra_renner'],
        y=df_final['total_compras'],
        z=df_final['ticket_medio'],
        mode='markers',
        marker=dict(
            size=5,
            opacity=0.55,
            color=profile_categories,  # Usar códigos numéricos para a cor
            colorscale='Viridis',  # Escolher uma escala de cores
            colorbar=dict(title='Profile')  # Adicionar a barra de cores
        )
    )])

    # Configurar o layout do gráfico
    fig.update_layout(
        title='Distribuição 3D de Compras por Cliente',
        scene=dict(
            xaxis_title='Dias Desde Última Compra',
            yaxis_title='Total de Compras',
            zaxis_title='Ticket Médio'
        )
    )


def conclusao():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Conclusão</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_conclusao = '''
        Com base nos resultados obtidos, podemos concluir que a segmentação de clientes permite uma melhor personalização das estratégias de marketing, aumentando o engajamento e a satisfação dos clientes.
        
        O arquivo a seguir contém o relatório final do projeto:
    '''

    # Mostra o texto na página
    st.markdown(texto_conclusao)
    
    # Função para exibir PDF
    file = 'C:\\Users\\ferre\\OneDrive\\PUCRS\\ProjetoEmCienciaDeDadosI\\Renner_Rethink\\ProjCD - Relatorio de Andamento.pdf'

    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display =  f"""<embed
    class="pdfobject"
    type="application/pdf"
    title="Embedded PDF"
    src="data:application/pdf;base64,{base64_pdf}"
    style="overflow: auto; width: 100%; height: 800px;">"""

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

def segmentacao_final():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Segmentação Final</h3>", unsafe_allow_html=True)

    # Cria o texto da página    
    texto_segmentacao = '''
        A segmentação final dos clientes foi realizada com sucesso, agrupando-os em cinco categorias distintas com base em características comportamentais.

        Exemplo de código para visualização dos segmentos:
    '''

    # Mostra o texto na página
    st.markdown(texto_segmentacao)