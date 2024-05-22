import streamlit as st

# Configurar la página
st.set_page_config(page_title="Frecuencias de Transmisor Rhode", page_icon=":satellite:", layout="centered")

st.title("Transmisor Rhode: Frecuencias de Operación")

# Información de canales y frecuencias
channels = {
    "Canal 1": 485,
    "Canal 2": 491,
    "Canal 3": 545
}

# Mostrar la información de los canales
st.header("Frecuencias de los Canales")
for channel, frequency in channels.items():
    st.write(f"**{channel}**: {frequency} MHz")

# Entrada de usuario para actualizar la frecuencia de un canal
st.header("Actualizar Frecuencia de un Canal")
channel_to_update = st.selectbox("Selecciona el canal a actualizar:", list(channels.keys()))
new_frequency = st.number_input(f"Introduce la nueva frecuencia para {channel_to_update} (MHz):", min_value=1, max_value=1000)

if st.button("Actualizar Frecuencia"):
    channels[channel_to_update] = new_frequency
    st.write(f"Frecuencia de **{channel_to_update}** actualizada a {new_frequency} MHz")

# Mostrar las frecuencias actualizadas
st.header("Frecuencias Actualizadas de los Canales")
for channel, frequency in channels.items():
    st.write(f"**{channel}**: {frequency} MHz")
