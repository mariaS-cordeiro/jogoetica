import streamlit as st

st.set_page_config(
    page_title="LABPE",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ LABPE")
st.subheader("Laboratório Virtual de Pesquisa em Educação")

st.write("Bem-vindo(a)!")

if st.button("▶ Iniciar Jornada"):
    st.success("A jornada começará em breve...")
