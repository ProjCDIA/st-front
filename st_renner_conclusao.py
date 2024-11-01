import streamlit as st

def main():
    # Cria o título da página
    st.markdown('<h1 style="color: #FF0000;">Renner ReThink.</h1>', unsafe_allow_html=True)

    # Cria o título da seção
    st.markdown("<h3 style='color: #FF0000;'>Conclusão</h3>", unsafe_allow_html=True)

    # Cria o texto da página
    texto_conclusao = '''
        Com base nos resultados obtidos, podemos concluir que a segmentação de clientes permite uma melhor personalização das estratégias de marketing, aumentando o engajamento e a satisfação dos clientes.        
    '''

    # Mostra o texto na página
    st.markdown(texto_conclusao)
