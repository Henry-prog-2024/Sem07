import random  # Importar la biblioteca random

def rellenar_array(tamano):
    """Rellena un array con números aleatorios."""
    return [random.randint(1, 100) for _ in range(tamano)]

def copiar_array(original):
    """Copia un array y lo devuelve."""
    return original.copy()

def mostrar_array(array):
    """Muestra todos los valores del array."""
    print("Contenido del array:", array)

def ordenar_burbuja(array):
    """Ordena el array utilizando el método de burbuja."""
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def main():
    # Definir el tamaño del array
    tamano = int(input("Introduce el tamaño del array: "))
    
    # Rellenar el array
    array = rellenar_array(tamano)
    
    # Mostrar el array original
    mostrar_array(array)
    
    # Copiar el array a otro
    array_copia = copiar_array(array)
    
    # Ordenar el array original
    array_ordenado = ordenar_burbuja(array)
    
    # Mostrar resultados
    print("Array ordenado:")
    mostrar_array(array_ordenado)
    
    print("Copia del array original:")
    mostrar_array(array_copia)

# Llamar a la función principal
if __name__ == "__main__":
    main()
