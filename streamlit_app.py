import streamlit as st

st.title("Boda Cristina y Marcos")

text_input = st.text_input(
    "Introducir la frase"   
)
if text_input == None or text_input == "" :
        st.write("")
elif text_input == 'Vuestros primos son unos cabrones':
    st.write("CORRECTO!!! Espero que hayáis disfrutado del reto! Enviadnos un whastapp y os enviaremos un bizum")
else:
    st.write("Seguid intentándolo.")
