import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Cargar el modelo de Machine Learning
model = tf.keras.models.load_model('ruta/a/tu/modelo.h5')

# Función para procesar la imagen y hacer la predicción
def predict(image):
    # Preprocesar la imagen para que tenga el formato correcto
    image = image.resize((224, 224))  # Asegúrate de que el tamaño de la imagen sea el que necesita tu modelo
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

