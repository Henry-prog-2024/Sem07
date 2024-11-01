import streamlit as st
#Algoritmo que pida números hasta que se introduzca un
#cero. Debe imprimir la suma y la media de todos los números
#introducidos.

def main():
    while True:
        numero = st.text_input("Introduce un número (0 para terminar):")
        numero = float(numero)
        if numero == 0:
            break
        
        suma = suma + numero
        contador = contador + 1
    if contador > 0:
        media = suma / contador
        st.write(f"Suma: {suma}")
        st.write(f"Media: {suma}")
    else:
        st.write("No se introdujeron números.")

if __name__ == "__main__":
    main()
