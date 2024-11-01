import streamlit as st

def main():
    st.title("Calculadora de Suma y Media")

    # Usar una lista para almacenar los números
    if 'numeros' not in st.session_state:
        st.session_state.numeros = []

    # Entrada del número
    numero = st.number_input("Introduce un número (0 para terminar):", step=1.0)

    # Añadir el número a la lista si no es 0
    if numero != 0:
        st.session_state.numeros.append(numero)

    # Mostrar resultados si hay números
    if st.session_state.numeros:
        suma = sum(st.session_state.numeros)
        media = suma / len(st.session_state.numeros)
        st.write(f"Suma: {suma}")
        st.write(f"Media: {media}")

    # Mostrar un mensaje si no se introdujeron números
    if len(st.session_state.numeros) == 0 and numero == 0:
        st.write("No se introdujeron números.")

if __name__ == "__main__":
    main()
