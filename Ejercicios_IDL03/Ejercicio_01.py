import streamlit as st

def suma(num1, num2):
    return num1 + num2

def main():
    st.title("Este programa es mío")
    num1 = st.number_input("ingrese primer número", value=0)
    num2 = st.number_input("ingrese segundo número", value=0)
    suma = calcular(num1, num2)

st.write(f"la suma es: {suma}")

