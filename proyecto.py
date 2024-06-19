import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

#Función de animación
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.freepik.com%2Fvector-premium%2Fpersonaje-dibujos-animados-codigo-barras-buscando-lupa-diseno-lindo_152558-13042.jpg&tbnid=ccR2z0Yn0m2SQM&vet=12ahUKEwjC4paX6-aGAxUZFGIAHTC9C5cQMygBegQIARBI..i&imgrefurl=https%3A%2F%2Fwww.freepik.es%2Fvector-premium%2Fpersonaje-dibujos-animados-codigo-barras-buscando-lupa-diseno-lindo_18499499.htm&docid=QSZoiCNT8Sj61M&w=626&h=626&q=imagen%20animada%20codigo&ved=2ahUKEwjC4paX6-aGAxUZFGIAHTC9C5cQMygBegQIARBI")
imagen_video =Image.opem("https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.freepik.com%2Ffotos-premium%2Fcodigos-binarios-movimiento-datos-digitales-abstractos-que-fluyen-traves-redes-ia-generativa_634358-1738.jpg&tbnid=Vx1Kmh1lRjxH3M&vet=12ahUKEwiM2ZPu6-aGAxWhFGIAHdSbD4gQMygPegQIARBr..i&imgrefurl=https%3A%2F%2Fwww.freepik.es%2Ffotos-premium%2Fcodigos-binarios-movimiento-datos-digitales-abstractos-que-fluyen-traves-redes-ia-generativa_41332183.htm&docid=OG5c9VFoFGMgkM&w=626&h=351&itg=1&q=imagen%20con%20movimiento%20de%20codigos&ved=2ahUKEwiM2ZPu6-aGAxWhFGIAHdSbD4gQMygPegQIARBr")











