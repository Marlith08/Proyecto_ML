import streamlit as st

def main():
    st.title("Bienvenido a mi aplicación Streamlit!")
    st.write("Esta es una aplicación sencilla que muestra un saludo personalizado.")

    name = st.text_input("Por favor, ingresa tu nombre:")
    
    if name:
        st.write(f"Hola, {name}! Encantado de conocerte.")
    else:
        st.write("Ingresa tu nombre en la casilla de texto.")

if __name__ == "__main__":
    main()

