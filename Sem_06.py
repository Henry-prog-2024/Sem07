import streamlit as st

#título de la aplicación
st.title("Ejercicios con bucles básicos en python")

#Ejercicio 1: Imprimir 10 veces 'Hola mundo'
st.subheader("Ejercicio 1: imprimir 'Hola Mundo' 10 veces")
if st.button("Ejecutar Ejercicio 1"):
    for i in range(10):
        st.write("Hola Mundo")

#Ejercicio 2: Imprimir los 10 primeros números'
st.subheader("Ejercicio 2: imprimir los 10 primeros números")
if st.button("Ejecutar Ejercicio 2"):
    for i in range(1,11):
        st.write(i)