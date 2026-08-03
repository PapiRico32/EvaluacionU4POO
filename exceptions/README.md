# Manejo de Excepciones - Taller Mecánico

## Excepciones personalizadas

### ServicioNoEncontradoError

Se lanza cuando se intenta operar con un servicio que no existe.

```python
from exceptions import ServicioNoEncontradoError

try:
    controlador.consultar_por_id(999)
except ServicioNoEncontradoError as e:
    print(f"Error: {e}")
    # Salida: Error: Servicio con ID 999 no encontrado
```

### CostoInvalidoError

Se lanza cuando el costo es menor o igual a cero.

```python
from exceptions import CostoInvalidoError

try:
    servicio = Servicio(cliente="Test", vehiculo="Test", 
                       tipo_servicio="Test", costo=-50)
except CostoInvalidoError as e:
    print(f"Error: {e}")
    # Salida: Error: Costo inválido: $-50. El costo debe ser mayor a 0
```

## Uso de try/except/else/finally

```python
try:
    # Código que puede fallar
    controlador.eliminar_servicio(id_servicio)
except ServicioNoEncontradoError as e:
    # Manejo específico
    print(f"Error: {e}")
except Exception as e:
    # Manejo genérico
    print(f"Error inesperado: {e}")
else:
    # Se ejecuta si no hay excepción
    print("Operación exitosa")
finally:
    # Siempre se ejecuta
    print("Limpieza completada")
```

## Casos de estudio

### Caso 1: Registrar servicio con costo negativo

```python
servicio = Servicio(
    cliente="Test",
    vehiculo="Test",
    tipo_servicio="Test",
    costo=-100.00
)

# Resultado esperado: CostoInvalidoError
```

### Caso 2: Eliminar servicio inexistente

```python
controlador.eliminar_servicio(999)

# Resultado esperado: ServicioNoEncontradoError
```