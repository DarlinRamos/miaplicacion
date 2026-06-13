import streamlit as st
import pandas as pd


def recomendacion():

    st.title("🎬 Sistema de Recomendación de K-Dramas")

    st.write("""
    Seleccione sus preferencias para recibir
    recomendaciones personalizadas.
    """)

    df = pd.read_csv("data/kdramas.csv")

    col1, col2 = st.columns(2)

    with col1:
        genero = st.selectbox(
            "🎭 Seleccione Género",
            df["genero"].unique()
        )

    with col2:
        plataforma = st.selectbox(
            "📺 Seleccione Plataforma",
            df["plataforma"].unique()
        )

    rating = st.slider(
        "⭐ Rating mínimo",
        1.0,
        10.0,
        8.5
    )

    año = st.slider(
        "📅 Año mínimo",
        2016,
        2025,
        2020
    )

    resultado = df[
        (df["genero"] == genero)
        &
        (df["plataforma"] == plataforma)
        &
        (df["rating"] >= rating)
        &
        (df["año"] >= año)
    ]

    st.markdown("---")
    st.subheader("🎥 Recomendaciones")

    if resultado.empty:

        st.warning(
            "No se encontraron K-Dramas con esos filtros."
        )

    else:

        st.success(
            f"Se encontraron {len(resultado)} recomendaciones"
        )

        for _, row in resultado.iterrows():

            with st.container():

                st.markdown(f"""
### 🎬 {row['nombre']}

⭐ **Rating:** {row['rating']}  
📺 **Plataforma:** {row['plataforma']}  
📅 **Año:** {row['año']}  
🎞️ **Episodios:** {row['episodios']}  
🎭 **Género:** {row['genero']}

---
""")