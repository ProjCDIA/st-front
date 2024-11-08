import streamlit as st

def main():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Conclusão</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_conclusao = '''
    Página ainda em andamento. Aguarde atualizações.
    '''

    # Mostra o texto na página
    st.markdown(texto_conclusao)
