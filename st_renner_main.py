import streamlit as st
import st_renner_libs

# Cria a navegação entre as páginas
pages = st.navigation({
    "Descrição e Compreensão do Projeto": [
        st.Page(st_renner_libs.descricao_projeto,
                title="Descrição do Projeto",
                url_path="descricao_projeto"),
        st.Page(st_renner_libs.compreensao_negocio,
                title="Compreensão de Negócio",
                url_path="compreensao_negocio"),
    ],
    "Exploração e Transformação": [
        st.Page(st_renner_libs.eda,
                title="Análise Exploratória",
                url_path="eda"),
        st.Page(st_renner_libs.etl,
                title="ETL",
                url_path="etl")
    ],
    "Criação e Modelagem": [
        st.Page(st_renner_libs.feature_engineering,
                title="Feature Engineering",
                url_path="feature_engineering"),
        st.Page(st_renner_libs.modelagem,
                title="Modelagem",
                url_path="modelagem")
    ],
    "Resultados": [
        st.Page(st_renner_libs.conclusao,
                title="Conclusão",
                url_path="conclusao"),
        st.Page(st_renner_libs.segmentacao_final,
                title="Segmentação Final",
                url_path="segmentacao_final")
    ]}, position='sidebar')

# Configurações da página
st.set_page_config(page_title=f"Renner Rethink - {pages.title}",
                   layout='wide',
                   initial_sidebar_state='auto',
                   page_icon="renner-logo-6.png")


# Cria o markdown para estilizar o conteúdo da página
st.markdown(
    """
    <style>
    .block-container {
    padding-top: 1.5rem;
    padding-bottom: 0rem;
    padding-left: 5rem;
    padding-right: 5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Cria o markdown para estilizar o logo e o menu lateral
st.markdown(
    """
    <style>
    /* Titles in bright red */
    h1, h2, h3, h4, h5, h6 {
        color: #FF0000;  /* bright red */
    }

    [data-testid="stSidebarNav"] a {
        color: white !important;
    }

    /* Ensure text within the sidebar remains white */
    [data-testid="stSidebarNav"] a:hover {
        color: white !important;
    }

    /* Logo alignment and size adjustments */
    [data-testid="stSidebarHeader"] img[data-testid="stLogo"] {
        max-width: 100%;
        height: auto;
        width: 100%;
        margin-top: 5px;
    }

    /* Control button adjustments */
    [data-testid="stSidebarCollapseButton"] button {
        margin-top: 0px;
        margin-left: -25px;
    }

    [data-testid="collapsedControl"] > div > button {
        margin-top: 10px;
    }

    /* Collapsed logo size */
    [data-testid="collapsedControl"] img[data-testid="stLogo"] {
        width: 8rem;
        height: auto;
        max-width: 8rem;
        margin-top: 5px;
        margin-left: -10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Adiciona o logo na página
st.logo("renner_rethink_logo.png", icon_image="renner_rethink_logo.png")

# Roda a aplicação
try:
    pages.run()
except Exception as e:
    st.error(f"Something went wrong: {str(e)}", icon=":material/error:")