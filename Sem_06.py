import streamlit as st

#título de la aplicación
st.title("Ejercicios con bucles básicos en python")

#Ejercicio 1: Imprimir 10 veces 'Hola mundo'
st.subheader("Ejercicio 1: imprimir 'Hola Mundo' 10 veces")
if st.button("Ejecutar Ejercicio 1"):
    for i in range(10):
        st.write("Hola Mundo")