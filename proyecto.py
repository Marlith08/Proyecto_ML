import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import gdown

# Descargar el modelo de Google Drive
@st.cache_resource
def load_model():
    url = 'https://drive.google.com/drive/u/0/folders/1YmhsgmJpdeyDSOZ8I9KqHosJrkyDMfKD'
    output = 'model.h5'
    gdown.download(url, output, quiet=False)
    model = tf.keras.models.load_model(output)
    return model

model = load_model()

# Función para procesar la imagen y hacer la predicción
def predict(image):
    image = image.resize((224, 224))  # Ajusta el tamaño de la imagen
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    
    # Hacer la predicción
    predictions = model.predict(image)
    return predictions

st.title("Clasificación de Imágenes con Machine Learning")
st.write("Sube una imagen para obtener una predicción")

# Subir imagen
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Abrir la imagen
    image = Image.open(uploaded_file)
    
    # Mostrar la imagen
    st.image(image, caption='Imagen subida.', use_column_width=True)
    st.write("")
    st.write("Clasificando...")
    
    # Hacer la predicción
    predictions = predict(image)
    
    # Mostrar el resultado
    st.write(f"Predicción: {predictions}")
