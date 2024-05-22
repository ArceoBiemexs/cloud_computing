import streamlit as st

# Configurar la página
st.set_page_config(page_title="Tren de Video", page_icon=":tv:", layout="wide")

st.title("Tren de Video: Desde la Captura hasta la Transmisión")

# Etapas del tren de video
st.header("Etapas del Tren de Video")
st.markdown("""
1. **Captura de Video**
   - **Cámaras**: Captura de imágenes.
   - **Sensores**: Conversión de luz a señales eléctricas.

2. **Procesamiento Inicial**
   - **Corrección de color**: Ajuste de los niveles de color.
   - **Balance de blancos**: Ajuste de los colores según la iluminación.
   - **Reducción de ruido**: Eliminación de interferencias.

3. **Conversión de Señal**
   - **Digitalización**: Conversión de analógico a digital.
   - **Compresión**: Reducción del ancho de banda.

4. **Edición y Mezcla**
   - **Switchers de video**: Cambio entre diferentes fuentes.
   - **Inserción de gráficos**: Agregar gráficos y títulos.
   - **Efectos especiales**: Aplicación de efectos visuales.

5. **Procesamiento de Señal**
   - **Escalado**: Ajuste de la resolución.
   - **Intercalado/Desintercalado**: Conversión entre video entrelazado y progresivo.
   - **Corrección de errores**: Protección de la integridad de la señal.

6. **Modulación**
   - **Modulador**: Modulación de la señal de video a la frecuencia de RF.
   - **Frecuencia Portadora**: Selección de la frecuencia del canal.

7. **Transmisión**
   - **Amplificación**: Amplificación de la señal modulada.
   - **Antena**: Envío de la señal a través de una antena.
   - **Repetidores**: Mantenimiento de la calidad de la señal.

8. **Recepción**
   - **Antena receptora**: Recepción de la señal de RF.
   - **Demodulación**: Recuperación de la señal de video base.
   - **Conversión de señal**: Conversión a formato analógico.
""")

# Información adicional sobre frecuencias
st.header("Frecuencias de Transmisión")
channels = {
    "Canal 1": 485,
    "Canal 2": 491,
    "Canal 3": 545
}

# Mostrar la información de los canales
for channel, frequency in channels.items():
    st.write(f"**{channel}**: {frequency} MHz")
