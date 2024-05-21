import streamlit as st
import pandas as pd
from io import StringIO

# Crear un widget para subir un archivo
uploaded_file = st.file_uploader("Elige un archivo")

# Verificar si se ha subido un archivo
if uploaded_file is not None:
    # Leer el archivo como bytes
    bytes_data = uploaded_file.getvalue()
    st.write("Bytes data:")
    st.write(bytes_data)

    # Convertir a un objeto similar a StringIO
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write("StringIO data:")
    st.write(stringio)

    # Leer el archivo como una cadena de texto
    string_data = stringio.read()
    st.write("String data:")
    st.write(string_data)

    # Leer el archivo como un DataFrame de pandas
    dataframe = pd.read_csv(uploaded_file)
    st.write("DataFrame:")
    st.write(dataframe)
