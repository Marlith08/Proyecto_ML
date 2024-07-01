import streamlit as st
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Título de la aplicación
st.title('Predicción de Imágenes con Modelo de Deep Learning')

# Subir una imagen de entrada
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

# Verificación de carga de archivo
if uploaded_file is not None:
    # Ruta completa al modelo
    modelo_path = 'https://github.com/Marlith08/Proyecto_ML/blob/main/.gitattributes'

    # Cargar el modelo
    modelo = load_model(modelo_path)

    # Mostrar la imagen subida
    st.image(uploaded_file, caption='Imagen de entrada', use_column_width=True)

    # Preprocesamiento de la imagen para hacer la predicción
    img = image.load_img(uploaded_file, target_size=(224, 224))  # Ajusta según las dimensiones de entrada de tu modelo
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.

    # Realizar la predicción
    prediction = modelo.predict(img_array)

    # Mostrar resultados
    st.write(f'Predicción: {prediction}')
