import streamlit as st

#Función principal para verificar automóviles
def verificar_automoviles():
    st.title("Centro de verificación de automóviles")

#Lista para verificar los puntos contaminantes.
If 'puntos_contaminantes' not in st.session_state:
    st.session_state.puntos_contaminantes =[]

    # Input para los puntos contaminanttes del automovil
    puntos = st.numbers_input("Ingrese los puntos fundamentales del automovil", min_value=0.0, step=0.1)

    # Botón para registrar el automovil
    if st.button("Registrar automovil"):
        st.session_state.puntos_contaminantes.append(puntos)
        st.success(f"Automovil registrado con {puntos} putos contaminantes.")

    # Mostrar los datos registrados hasta el momento
    if len(st.session_state.puntos_contaminantes) > 0 and st.button("calcular resultados"):
        promedio=sum(st.session_state.puntos_contaminantes)/len(st.session_state.puntos_contaminantes)
        menos_contaminacion = min(st.session_state.puntos_contaminantes)
        mas_contaminacion = max(st.session_state.puntos_contaminantes)

        # Mostrar resultados
        st.write(f"Promedio de puntos contaminantes: {promedio:.2f}")
        st.write(f"El automovil que menos contamino tiene: {menos_contaminacion:.2f}")
        st.write(f"El automovil que más contaminó tiene: {mas_contaminacion:.2f}")

    #Opción para reiniciar los datos
    if st.button("Reiniciar datos"):
        st.seccion_state.puntos_contaminantes = []
        st.susses("Datos reiniciados correctamente")

#Ejecutar la función
if __name__ == "__main__"
    verificar automoviles()
