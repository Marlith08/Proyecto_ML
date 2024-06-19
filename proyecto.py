import streamlit as st
from PIL import Image
import os

# Crear una función para guardar la imagen subida
def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except Exception as e:
        return False

# Crear una función para eliminar la imagen subida
def delete_uploaded_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
        return True
    except Exception as e:
        return False

st.title("Aplicación de subida y eliminación de imágenes")

# Crear un directorio 'uploads' si no existe
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Mostrar un cuadro para la imagen y los botones
uploaded_file = st.file_uploader("Elige una imagen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        st.success("Imagen subida exitosamente!")
        image_path = os.path.join("uploads", uploaded_file.name)
        image = Image.open(image_path)
        st.image(image, caption="Imagen subida", use_column_width=True)
    else:
        st.error("Error al subir la imagen.")

col1, col2 = st.columns([1, 1])

with col1:
    st.write("")  # Espacio para alinear el botón
    if st.button("Subir imagen"):
        if uploaded_file is not None:
            st.success("Imagen subida exitosamente!")
        else:
            st.warning("Primero sube una imagen.")

with col2:
    st.write("")  # Espacio para alinear el botón
    if st.button("Eliminar imagen"):
        if uploaded_file is not None:
            file_path = os.path.join("uploads", uploaded_file.name)
            if delete_uploaded_file(file_path):
                st.success("Imagen eliminada exitosamente!")
            else:
                st.error("Error al eliminar la imagen.")
        else:
            st.warning("Primero sube una imagen.")

# Recuadro para mostrar datos de la imagen
st.subheader("Datos de la imagen")
st.write("Aquí se mostrarán los datos de la imagen.")