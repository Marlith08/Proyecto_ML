# Importa las bibliotecas necesarias
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
    # Cargar el modelo entrenado
    modelo_path = 'modelo_path = 'C:/Users/anton/Proyecto_ML/Xception_diabetic_retinopathy_colab_v2.h5'
    modelo = load_model(modelo_path)

    # Mostrar la imagen subida
    st.image(uploaded_file, caption='Imagen de entrada', use_column_width=True)

    # Preprocesamiento de la imagen para hacer la predicción
    img = image.load_img(uploaded_file, target_size=(img_width, img_height))  # Ajusta img_width e img_height según tu modelo
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Añade una dimensión para batch
    img_array /= 255.  # Normaliza los valores de píxeles

    # Realizar la predicción
    prediction = modelo.predict(img_array)
    # Aquí puedes manejar la salida de la predicción según tu modelo específico

    # Mostrar resultados
    st.write(f'Predicción: {prediction}')
