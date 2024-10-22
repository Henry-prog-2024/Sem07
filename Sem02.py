import streamlit as st

#Inicialización de variables
usuarios = []

#Funcion para agragar un usuario
def agregar_usuario(nombre):
    usuarios.append(nombre)
    st.success(f"Usuario:{nombre} agregado")

    #Funcion para mostrar usuarios
    def mostrar_usuarios():
    if usuarios:
        st.write("Lista de usuarios")
        for usuario in usuario:
    else
        st.warning("No hay usuarios registrados: ")
#Menu principal
st.title("Gestión de usuarios")
option = st.selectbox("Selecciona una opción:", ["Agregar usuasio", "Mostrar usuario"])
if option == "Agregar usuario":
    nombre = st.text_input ("Nombre del usuario: ")
    if st.botton("Agregar"):
        if nombre:
            agregar_usuario(nombre)
        else:
            st.error("El nombre no puede estar vacio")
elif option == "Mostrar usuario"
    mostrar_usuario()


