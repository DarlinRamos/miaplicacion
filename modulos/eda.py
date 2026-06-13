import streamlit as st
import pandas as pd
import plotly.express as px


def eda():

    st.title("📊 Análisis Exploratorio de K-Dramas")

    df = pd.read_csv("data/kdramas.csv")

    submenu = st.sidebar.selectbox(
        "Submenú EDA",
        (
            "Descripción del Dataset",
            "Descripción de Campos",
            "Navegador Dataset",
            "Buscador por Código",
            "Graficador",
            "Hipótesis"
        )
    )

    # =====================================
    # DESCRIPCIÓN DATASET
    # =====================================
    if submenu == "Descripción del Dataset":

        st.subheader("📋 Información del Dataset")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Filas", df.shape[0])

        with col2:
            st.metric("Columnas", df.shape[1])

        st.subheader("Tipos de Datos")
        st.write(df.dtypes)

        st.subheader("Estadísticas")
        st.write(df.describe())

    # =====================================
    # DESCRIPCIÓN DE CAMPOS
    # =====================================
    elif submenu == "Descripción de Campos":

        descripciones = {
            "codigo": "Código único del K-Drama",
            "nombre": "Nombre del K-Drama",
            "genero": "Tipo de género del drama",
            "episodios": "Cantidad total de episodios",
            "rating": "Calificación promedio",
            "plataforma": "Plataforma de streaming",
            "año": "Año de estreno"
        }

        campo = st.selectbox(
            "Seleccione un campo",
            df.columns
        )

        st.subheader(f"📌 Campo: {campo}")

        st.info(descripciones[campo])

        if df[campo].dtype == "object":

            st.subheader("Valores posibles")
            st.write(df[campo].unique())

        else:

            st.subheader("Descripción estadística")
            st.write(df[campo].describe())

    # =====================================
    # NAVEGADOR DATASET
    # =====================================
    elif submenu == "Navegador Dataset":

        st.subheader("📄 Navegador Dataset")

        st.dataframe(df)

    # =====================================
    # BUSCADOR
    # =====================================
    elif submenu == "Buscador por Código":

        st.subheader("🔍 Buscador")

        codigo = st.text_input(
            "Ingrese código",
            "KD001"
        )

        resultado = df[
            df["codigo"] == codigo.upper()
        ]

        if resultado.empty:

            st.error("No encontrado")

        else:

            st.success("K-Drama encontrado")
            st.dataframe(resultado)

    # =====================================
    # GRAFICADOR
    # =====================================
    elif submenu == "Graficador":

        st.subheader("📈 Graficador Exploratorio")

        campo = st.selectbox(
            "Seleccione un campo",
            (
                "rating",
                "episodios",
                "genero",
                "plataforma"
            )
        )

        if campo in ["rating", "episodios"]:

            fig = px.histogram(
                df,
                x=campo,
                title=f"Distribución de {campo}"
            )

        elif campo == "genero":

            conteo = df["genero"].value_counts()

            fig = px.bar(
                x=conteo.index,
                y=conteo.values,
                labels={
                    "x": "Genero",
                    "y": "Cantidad"
                },
                title="K-Dramas por Género"
            )

        else:

            fig = px.pie(
                df,
                names="plataforma",
                title="Distribución por Plataforma"
            )

        st.plotly_chart(fig)

    # =====================================
    # HIPÓTESIS
    # =====================================
    elif submenu == "Hipótesis":

        st.subheader("🧪 Hipótesis")

        hipotesis = st.selectbox(
            "Seleccione una hipótesis",
            (
                "Más episodios = mejor rating",
                "Netflix tiene mejor rating"
            )
        )

        # Hipótesis 1
        if hipotesis == "Más episodios = mejor rating":

            fig = px.scatter(
                df,
                x="episodios",
                y="rating",
                color="genero",
                trendline="ols",
                title="Episodios vs Rating"
            )

            st.plotly_chart(fig)

            st.success("""
            Conclusión:
            Tener más episodios no garantiza
            un mejor rating.
            """)

        # Hipótesis 2
        else:

            promedio = df.groupby(
                "plataforma"
            )["rating"].mean()

            fig = px.bar(
                x=promedio.index,
                y=promedio.values,
                title="Promedio de Rating por Plataforma"
            )

            st.plotly_chart(fig)

            st.success("""
            Conclusión:
            Netflix tiene ratings altos,
            pero depende del contenido.
            """)