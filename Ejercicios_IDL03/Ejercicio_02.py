import streamlit as st

def main():
    st.title("Calculadora de Suma y Media")
    
    numeros = []
    
    while True:
        numero = st.number_input("Introduce un número (0 para terminar):", step=1.0)
        
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