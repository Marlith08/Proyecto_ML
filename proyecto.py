import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('ruta/a/tu/modelo.h5')

# Función para procesar la imagen y hacer la predicción
def predict(image):
    # Preprocesar la imagen para que tenga el formato correcto
    image = image.resize((224, 224))  
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    
    predictions = model.predict(image)
    return predictions

st.title("Clasificación de Imágenes con Machine Learning")
st.write("Sube una imagen para obtener una predicción")

# Subir imagen
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    st.image(image, caption='Imagen subida.', use_column_width=True)
    st.write("")
    st.write("Clasificando...")
    
    # Hacer la predicción
    predictions = predict(image)
    
    # Mostrar el resultado
    st.write(f"Predicción: {predictions}")

