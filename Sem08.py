import streamlit as st 
def validate_data(marca, modelo, kilometraje):
    """Valida los datos ingresados para el automóvil"""
    if not marca or not modelo:
        return  "La marca y el modelo no deben de estar vacios."
    try:
        kilometraje = float(kilometraje)
        if kilometraje < 0:
            return "El kilometraje no puede ser menor de 0."
    except ValueError:
        return "El kilometraje debe ser un número válido."
    return None

def main()
    st.title("Registro de automovil")
    st.write("Ingrese los datos del automóvil a continuación")
    ##Registro por el usuario
    error = validate_data(marca, modelo, kilometraje)
    if error:
        st.error(error)
    else:
        st.success("Automovil registrado exitosamente.")
        st.write("**Marca**", marca)
        st.write("**Modelo**", modelo)
        st.write("**kilometraje**", kilometraje)

if __name__ == "__main__":
    main()