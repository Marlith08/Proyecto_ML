import streamlit as st
from keras.models import Model
from keras.layers import GlobalAveragePooling2D, Dense, Dropout
from keras.applications import Xception
from keras.preprocessing import image
from keras.engine import saving
import numpy as np
import urllib.request
import os
import h5py

# Función para descargar el modelo
@st.experimental_memo
def download_model(url, filename):
    urllib.request.urlretrieve(url, filename)

# Descargar el modelo si no está ya en la carpeta
model_url = 'http://server01.labs.org.pe:2005/Xception_diabetic_retinopathy_colab_v2.h5'
model_filename = 'Xception_diabetic_retinopathy_colab_v2.h5'

if not os.path.exists(model_filename):
    with st.spinner('Descargando el modelo...'):
        try:
            download_model(model_url, model_filename)
            st.success('Modelo descargado con éxito!')
        except Exception as e:
            st.error(f'Error descargando el modelo: {e}')
            st.stop()

# Título de la aplicación
st.title('Predicción de Imágenes con Modelo de Deep Learning')

# Subir una imagen de entrada
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

# Verificación de carga de archivo
if uploaded_file is not None:
    try:
        # Definir el modelo base preentrenado
        target_size = (229, 229)
        base_model = Xception(weights='imagenet', include_top=False, input_shape=target_size + (3,))
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(1024, activation='relu')(x)
        x = Dropout(0.5)(x)
        predictions = Dense(1, activation='sigmoid')(x)
        model = Model(inputs=base_model.input, outputs=predictions)

        # Cargar los pesos del modelo desde el archivo h5
        try:
            with h5py.File(model_filename, 'r') as f:
                saving.load_weights_from_hdf5_group(f['model_weights'], model.layers)
            st.success("Modelo cargado correctamente.")
        except (UnicodeDecodeError, ValueError, OSError) as e:
            st.error(f"Error al cargar los pesos del modelo: {e}")
            model = None

        if model:
            # Mostrar la imagen subida
            st.image(uploaded_file, caption='Imagen de entrada', use_column_width=True)

            # Preprocesamiento de la imagen para hacer la predicción
            img = image.load_img(uploaded_file, target_size=target_size)
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.

            # Realizar la predicción
            prediction = model.predict(img_array)

            # Mostrar resultados
            st.write(f'Predicción: {prediction}')
    except Exception as e:
        st.error(f'Error cargando el modelo o realizando la predicción: {e}')
