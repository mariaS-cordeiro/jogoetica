import streamlit as st

st.set_page_config(page_title="LABPE", page_icon="🏛️", layout="wide")

st.markdown("""
<style>
.game-area {
    position: relative;
    width: 100%;
}
.game-area img {
    width: 100%;
    border-radius: 10px;
}
.avatar {
    position: absolute;
    top: 74%;
    font-size: 45px;
    transition: left 0.5s ease;
}
</style>
""", unsafe_allow_html=True)

if "avatar" not in st.session_state:
    st.session_state.avatar = None

if "fase" not in st.session_state:
    st.session_state.fase = 0

avatares = ["👩🏻‍🔬", "👩🏾‍🦱", "👨🏻‍🎓", "👨‍🎤"]

salas = [
    "Recepção",
    "Biblioteca",
    "Sala do Pesquisador",
    "Sala dos Documentos",
    "Comitê de Ética",
    "Sala dos Dilemas Éticos",
    "Certificação Final"
]

posicoes = [8, 21, 34, 47, 60, 74, 88]

st.title("🏛️ LABPE")
st.subheader("Laboratório Virtual de Pesquisa em Educação")

if st.session_state.avatar is None:
    st.write("Escolha o avatar que irá acompanhar você nesta jornada:")

    cols = st.columns(4)
    for i, avatar in enumerate(avatares):
        with cols[i]:
            st.markdown(f"<div style='font-size:70px;text-align:center'>{avatar}</div>", unsafe_allow_html=True)
            if st.button("Escolher", key=f"avatar_{i}"):
                st.session_state.avatar = avatar
                st.rerun()

else:
    x = posicoes[st.session_state.fase]

    st.markdown(f"""
    <div class="game-area">
        <img src="cenario_labpe.png.png">
        <div class="avatar" style="left:{x}%;">{st.session_state.avatar}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### Você está em: **{salas[st.session_state.fase]}**")

    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        if st.button("⬅ Voltar") and st.session_state.fase > 0:
            st.session_state.fase -= 1
            st.rerun()

    with col2:
        if st.button("▶ Continuar") and st.session_state.fase < len(salas) - 1:
            st.session_state.fase += 1
            st.rerun()

    with col3:
        if st.button("🔄 Trocar avatar"):
            st.session_state.avatar = None
            st.session_state.fase = 0
            st.rerun()
