import streamlit as st

st.set_page_config(
    page_title="LABPE",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ LABPE")
st.subheader("Laboratório Virtual de Pesquisa em Educação")

st.write("Teste de carregamento da imagem:")

st.image("cenario_labpe.png.png", use_container_width=True)
