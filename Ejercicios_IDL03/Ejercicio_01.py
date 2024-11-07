import streamlit as st

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

def dividir(num1, num2):
    return num1/num2

def main():
    st.title("Programa operaciones matemáticas")
    oper = st.selectbox("Operación", ("Suma", "Resta", "Multiplicación", "División"))
    num1 = st.number_input("ingrese primer número", value=0)
    num2 = st.number_input("ingrese segundo número", value=0)
    st.button("Operación")
    
    if oper == "Suma":
        st.button(oper)
        resultado = suma(num1, num2)
        st.write(f"la suma es: {resultado}")
    if oper == "Resta":
        st.button(oper)
        resultado = resta(num1, num2)
        st.write(f"la resta es: {resultado}")


if __name__ == "__main__":
    main()

