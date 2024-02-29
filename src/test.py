from datetime import datetime, timedelta

# Obtener la fecha y hora actuales
fecha_actual = datetime.now()

# Restar 1.5 días
cantidad_dias = 1.5
fecha_resultado = fecha_actual - timedelta(days=cantidad_dias)

# Imprimir las fechas
print("Fecha y hora actual:", fecha_actual.strftime('%Y-%m-%d %H:%M:%S'))
print(f"Fecha y hora después de restar {cantidad_dias} días:", fecha_resultado.strftime('%Y-%m-%d %H:%M:%S'))


# RECIBIR EL DIFERENCIAL DE TIEMPO EN DÍAS -> 365 * 5
# RESTAR LA FECHA ACTUAL EN FORMATO UTC -5 CON EL DIFERENCIAL Y ALMACENAR EL VALOR DE LA DIFERENCIA
# ELIMINAR TODOS LOS ARCHIVOS ANTES DE ESA FECHA
