import streamlit as st
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import urllib.request
import os
# Función para descargar el modelo
@st.experimental_memo
def download_model(url, filename):
    urllib.request.urlretrieve(url, filename)
# Descargar el modelo si no está ya en la carpeta
model_url = 'http://server01.labs.org.pe:2005/Xception_diabetic_retinopathy_colab_v2.h5'
model_filename = 'Xception_diabetic_retinopathy_colab_v2.h5'

if not os.path.exists(model_filename):
    with st.spinner('Descargando el modelo...'):
        download_model(model_url, model_filename)
        st.success('Modelo descargado con éxito!')

# Título de la aplicación
st.title('Predicción de Imágenes con Modelo de Deep Learning')
	@@ -27,20 +31,23 @@ def download_model(url, filename):

# Verificación de carga de archivo
if uploaded_file is not None:
    # Cargar el modelo
    modelo = load_model(model_filename)

    # Mostrar la imagen subida
    st.image(uploaded_file, caption='Imagen de entrada', use_column_width=True)

    # Preprocesamiento de la imagen para hacer la predicción
    img = image.load_img(uploaded_file, target_size=(229, 229))  # Ajusta según las dimensiones de entrada de tu modelo
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.

    # Realizar la predicción
    prediction = modelo.predict(img_array)

    # Mostrar resultados
    st.write(f'Predicción: {prediction}')
