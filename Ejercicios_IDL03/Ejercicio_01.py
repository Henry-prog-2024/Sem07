import streamlit as st
#Algoritmo que pida números hasta que se introduzca un
#cero. Debe imprimir la suma y la media de todos los números
#introducidos.

import streamlit as st

def main():
    st.title("Calcular SUMA y MEDIA")
    
    numeros = []
    
    while True:
        numero = st.number_input("Introduce un número (0 para terminar):", min_value=1)
        
        if numero == 0:
            break
            
        numeros.append(numero)

    if numeros:
        suma = sum(numeros)
        media = suma / len(numeros)
        st.write(f"Suma: {suma}")
        st.write(f"Media: {media}")
    else:
        st.write("No se introdujeron números.")

if __name__ == "__main__":
    main()
