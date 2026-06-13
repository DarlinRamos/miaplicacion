import streamlit as st
from PIL import Image

from modulos.eda import eda
from modulos.ml import ml
from modulos.recomendacion import recomendacion


def main():

    st.set_page_config(
        page_title="K-Drama Analytics",
        page_icon="🎬",
        layout="wide"
    )

    st.sidebar.title("🎬 MENU K-DRAMAS")

    menu = st.sidebar.selectbox(
        "Seleccione una opcion",
        (
            "INICIO",
            "EDA",
            "MACHINE LEARNING",
            "RECOMENDACION"
        )
    )

   
    if menu == "INICIO":

        st.title("🎬 Sistema Inteligente de K-Dramas")

        st.write("""
Esta aplicación permite analizar información
sobre K-Dramas mediante Análisis Exploratorio
de Datos (EDA), Machine Learning y un
Sistema de Recomendación inteligente.
""")
        imagen = Image.open("images/portada.jpg")
        st.image(imagen)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("🎥 K-Dramas", "35")

        with col2:
            st.metric("📺 Plataformas", "3")

        with col3:
            st.metric("⭐ Rating Promedio", "8.9")

    elif menu == "EDA":
        eda()

    elif menu == "MACHINE LEARNING":
        ml()

    elif menu == "RECOMENDACION":
        recomendacion()


if __name__ == "__main__":
    main()