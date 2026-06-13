import streamlit as st
from textblob import TextBlob


def sentimientos():

    st.title("🎭 Análisis de Sentimientos")

    st.write("""
    Escriba una opinión sobre un K-Drama
    y el sistema analizará el sentimiento.
    """)

    texto = st.text_area(
        "✍️ Escriba su opinión aquí"
    )

    if st.button("Analizar Sentimiento"):

        if texto == "":

            st.warning("Ingrese una opinión")

        else:

            
            try:
                texto_en = TextBlob(texto).translate(
                    from_lang="es", to="en"
                )
                analisis = TextBlob(str(texto_en))
            except Exception:
               
                analisis = TextBlob(texto)

            polaridad = analisis.sentiment.polarity

            st.subheader("Resultado")

        
            st.progress(
                int((polaridad + 1) / 2 * 100),
                text=f"Polaridad: {polaridad:.2f}  (-1 negativo → +1 positivo)"
            )

            if polaridad > 0.1:

                st.success("😊 Sentimiento Positivo")
                st.write("Parece que disfrutaste este K-Drama.")

            elif polaridad < -0.1:

                st.error("😞 Sentimiento Negativo")
                st.write("Parece que el K-Drama no fue de tu agrado.")

            else:

                st.info("😐 Sentimiento Neutral")
                st.write("Tu opinión parece neutral o mixta.")
