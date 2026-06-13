import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error


def ml():

    st.title("🤖 Machine Learning K-Dramas")

    df = pd.read_csv("data/kdramas.csv")

    st.subheader("Configuración del Modelo")

    col1, col2 = st.columns(2)

    with col1:

        algoritmo = st.selectbox(
            "Seleccione algoritmo",
            (
                "Regresión Lineal",
                "Árbol de Decisión"
            )
        )

    with col2:

        train_size = st.slider(
            "Porcentaje entrenamiento",
            50,
            90,
            80
        )

    st.markdown("---")

    variable_x = st.selectbox(
        "Variable independiente (X)",
        [
            "episodios",
            "año",
            "rating"
        ]
    )

    variable_y = st.selectbox(
        "Variable dependiente (Y)",
        [
            "rating",
            "episodios"
        ]
    )

    X = df[[variable_x]]
    y = df[variable_y]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        train_size=train_size / 100,
        random_state=42
    )

    # Modelo
    if algoritmo == "Regresión Lineal":
        modelo = LinearRegression()

    else:
        modelo = DecisionTreeRegressor()

    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)

    # ======================
    # GRAFICA + RESULTADOS
    # ======================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📊 Gráfica")

        fig = px.scatter(
            df,
            x=variable_x,
            y=variable_y,
            color="genero",
            title=f"{variable_x} vs {variable_y}",
            trendline="ols"
        )

        st.plotly_chart(fig)

    with col2:

        st.subheader("📈 Resultados")

        st.metric(
            "R2 Score",
            abs(round(r2_score(y_test, y_pred), 2))
        )

        st.metric(
            "Error Medio",
            round(
                mean_absolute_error(
                    y_test,
                    y_pred
                ),
                2
            )
        )

        try:
            st.metric(
                "Coeficiente",
                round(modelo.coef_[0], 2)
            )

        except:
            st.metric(
                "Profundidad Árbol",
                modelo.get_depth()
            )

    st.markdown("---")

    # ======================
    # PREDICCION
    # ======================

    st.subheader("🎯 Predicción")

    valor = st.slider(
        f"Ingrese {variable_x}",
        int(df[variable_x].min()),
        int(df[variable_x].max()),
        int(df[variable_x].mean())
    )

    prediccion = modelo.predict([[valor]])

    st.success(
        f"Predicción estimada de {variable_y}: "
        f"{round(prediccion[0],2)}"
    )