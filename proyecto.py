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

# Estilos CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ADD8E6; /* Color celeste de fondo */
    }
    .stFileUploader {
        background-color: #E6E6FA; /* Color lila de los recuadros */
        border-radius: 10px;
        padding: 10px;
    }
    .stButton button {
        background-color: #E6E6FA; /* Color lila de los botones */
        border: none;
        border-radius: 10px;
        padding: 10px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #D8BFD8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Aplicación de subida y eliminación de imágenes")

# Crear un cuadro para que el usuario pueda subir una imagen
uploaded_file = st.file_uploader("Elige una imagen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        st.success("Imagen subida exitosamente!")
        
        # Redimensionar la imagen a 5x5 píxeles
        image = Image.open(uploaded_file)
        resized_image = image.resize((1, 1))

        # Mostrar la imagen redimensionada
        st.image(resized_image, caption="Imagen subida")

        if st.button("Eliminar imagen"):
            file_path = os.path.join("uploads", uploaded_file.name)
            if delete_uploaded_file(file_path):
                st.success("Imagen eliminada exitosamente!")
            else:
                st.error("Error al eliminar la imagen.")
    else:
        st.error("Error al subir la imagen.")

# Crear un directorio 'uploads' si no existe
if not os.path.exists("uploads"):
    os.makedirs("uploads")
