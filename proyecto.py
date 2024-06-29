import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import gdown

# Descargar el modelo de Google Drive
@st.cache_resource
def load_model():
    url = 'https://drive.google.com/uc?id=1pHQW0c7nauYcO1748kBNyX1nwcmFFx8l'  # Enlace de descarga directa
    output = 'Xception_diabetic_retinopathy_colab_v2.h5'  # Nombre correcto del archivo
    gdown.download(url, output, quiet=False)
    model = tf.keras.models.load_model(output)
    return model

model = load_model()

# Función para procesar la imagen y hacer la predicción
def predict(image):
    # Preprocesar la imagen para que tenga el formato correcto
    image = image.resize((224, 224))  # Ajusta el tamaño según tu modelo
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    # Hacer la predicción
    predictions = model.predict(image)
    return predictions

# Interfaz de usuario con Streamlit
st.title("Clasificación de Imágenes con Machine Learning")
st.write("Sube una imagen para obtener una predicción")

# Subir imagen
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida.', use_column_width=True)
    st.write("")
    st.write("Clasificando...")

    predictions = predict(image)
    st.write("Predicción:", predictions)
