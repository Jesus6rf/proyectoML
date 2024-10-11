import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title("Aplicación Streamlit desde GitHub")

# Texto simple
st.write("Esta es una prueba simple para verificar la integración con GitHub.")

# Crear un botón interactivo
if st.button("Haz clic aquí"):
    st.write("¡Botón presionado!")

# Crear un deslizador
valor = st.slider("Selecciona un valor", 0, 100, 25)
st.write(f"Valor seleccionado: {valor}")

# Crear una tabla de datos aleatorios
st.write("Datos aleatorios generados:")
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['Columna 1', 'Columna 2', 'Columna 3']
)
st.write(data)

# Gráfico de línea basado en los datos generados
st.line_chart(data)
