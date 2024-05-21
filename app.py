import streamlit as st
import pandas as pd
from io import StringIO

# Crear un widget para subir un archivo
uploaded_file = st.file_uploader("Elige un archivo")

# Verificar si se ha subido un archivo
if uploaded_file is not None:
    # Intentar decodificar el archivo con manejo de errores
    try:
        file_content = uploaded_file.getvalue().decode("utf-8", errors='replace')
        # Convertir a un objeto similar a StringIO
        stringio = StringIO(file_content)
        st.write("StringIO data:")
        st.write(stringio)

        # Leer el archivo como una cadena de texto
        string_data = stringio.read()
        st.write("String data:")
        st.write(string_data)

        # Leer el archivo como un DataFrame de pandas
        dataframe = pd.read_csv(StringIO(file_content))
        st.write("DataFrame:")
        st.write(dataframe)
    except Exception as e:
        st.error(f"Ocurrió un error al leer el archivo: {e}")
