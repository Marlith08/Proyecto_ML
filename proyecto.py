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

# Crear un directorio 'uploads' si no existe
if not os.path.exists("uploads"):
    os.makedirs("uploads")

st.title("Aplicación de subida y eliminación de imágenes")

# Añadir estilo CSS
st.markdown(
    """
    <style>
    .image-container {
        width: 6in;
        height: 6in;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid #ddd;
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 20px;
    }
    .image-container img {
        max-width: 100%;
        max-height: 100%;
    }
    .button-container {
        display: flex;
        justify-content: space-between;
        width: 6in;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Mostrar un cuadro para la imagen y los botones
uploaded_file = st.file_uploader("Elige una imagen", type=["png", "jpg", "jpeg"])

with st.container():
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    if uploaded_file is not None:
        if save_uploaded_file(uploaded_file):
            st.success("Imagen subida exitosamente!")
            image_path = os.path.join("uploads", uploaded_file.name)
            image = Image.open(image_path)
            st.image(image, use_column_width=True)
        else:
            st.error("Error al subir la imagen.")
    else:
        st.info("Por favor, sube una imagen para verla aquí.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Subir imagen"):
            if uploaded_file is not None:
                st.success("Imagen subida exitosamente!")
            else:
                st.warning("Primero sube una imagen.")

    with col2:
        if st.button("Eliminar imagen"):
            if uploaded_file is not None:
                file_path = os.path.join("uploads", uploaded_file.name)
                if delete_uploaded_file(file_path):
                    st.success("Imagen eliminada exitosamente!")
                else:
                    st.error("Error al eliminar la imagen.")
            else:
                st.warning("Primero sube una imagen.")
    st.markdown('</div>', unsafe_allow_html=True)

# Recuadro para mostrar datos de la imagen
st.subheader("Datos de la imagen")
st.write("Aquí se mostrarán los datos de la imagen.")
