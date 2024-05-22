import streamlit as st
from PIL import Image

# Configurar la página
st.set_page_config(page_title="Los Camones", page_icon=":meat_on_bone:", layout="wide")

# Cargar imagenes
logo = Image.open("logo_los_camones.png")
carnitas = Image.open("carnitas.png")
 
# Encabezado
st.image(logo, width=200)
st.title("Restaurante de Carnitas Los Camones")
st.subheader("¡Bienvenidos a Los Camones! Disfruta de las mejores carnitas de la ciudad.")

# Descripción
st.markdown("""
Los Camones es un restaurante familiar especializado en la preparación de deliciosas carnitas. 
Ofrecemos una experiencia gastronómica única con ingredientes frescos y un ambiente acogedor.
""")

# Mostrar imagen de carnitas
st.image(carnitas, caption="Nuestras famosas carnitas", use_column_width=True)

# Menú del restaurante
st.header("Menú")
menu_items = {
    "Taco de Carnitas": 20,
    "Torta de Carnitas": 35,
    "Quesadilla de Carnitas": 25,
    "Orden de Carnitas (1kg)": 200,
    "Refresco": 15,
    "Cerveza": 30
}

# Mostrar el menú
for item, price in menu_items.items():
    st.write(f"**{item}**: ${price} MXN")

# Selección de platillos
st.header("Haz tu pedido")
selected_items = st.multiselect("Selecciona tus platillos:", options=list(menu_items.keys()))

# Calcular total
if selected_items:
    total = sum(menu_items[item] for item in selected_items)
    st.write(f"Total a pagar: **${total} MXN**")

# Información de contacto
st.header("Contacto")
with st.form("contact_form"):
    name = st.text_input("Nombre:")
    email = st.text_input("Correo electrónico:")
    message = st.text_area("Mensaje:")
    submitted = st.form_submit_button("Enviar")

    if submitted:
        st.write("¡Gracias por contactarnos! Nos pondremos en contacto contigo pronto.")

# Opiniones de clientes
st.header("Opiniones de Clientes")
st.text_area("Deja tu opinión:")

# Mostrar opiniones (ejemplo)
st.write("**Juan Pérez**: Las mejores carnitas que he probado. ¡Recomendado!")
st.write("**Ana López**: Excelente servicio y comida deliciosa.")

# Mapa de ubicación
st.header("Ubicación")
st.map()

# Redes sociales
st.header("Síguenos en redes sociales")
st.write("[Facebook](https://www.facebook.com/LosCamones)")
st.write("[Instagram](https://www.instagram.com/LosCamones)")

# Pie de página
st.markdown("""
**Los Camones** \n
Dirección: Av. Carnitas 123, Ciudad, País \n
Teléfono: (123) 456-7890 \n
Correo: contacto@loscamones.com
""")
