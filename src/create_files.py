import os
from datetime import datetime

def generate_file(base_name):
    # Obtener la ruta actual
    ruta_actual = os.getcwd()

    fecha_hora_actual = datetime.now().strftime("%Y%m%d_%H%M%S%f")

    nombre_archivo = f"{base_name}_{fecha_hora_actual}.txt"
    ruta_archivo = os.path.join(ruta_actual, nombre_archivo)

    with open(ruta_archivo, 'w') as archivo:
        archivo.write(f"Contenido del archivo {nombre_archivo}")

    print(f"Archivo {nombre_archivo} creado en {ruta_actual}")

    return nombre_archivo