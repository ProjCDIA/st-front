import streamlit as st

def main():
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