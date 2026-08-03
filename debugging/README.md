## Procedimiento

1. Ejecutar: `python debugging/debug_servicio.py`
2. El programa se pausa en `pdb.set_trace()`
3. Usar comandos para inspeccionar:

### Comandos usados:
- `p servicio` - Ver objeto completo
- `p servicio.cliente` - Ver cliente
- `p servicio.vehiculo` - Ver vehículo
- `p servicio.costo` - Ver costo
- `p errores` - Ver lista de errores
- `n` - Avanzar a siguiente línea
- `c` - Continuar ejecución

### Variables inspeccionadas:
- `servicio`: Objeto Servicio con sus atributos
- `errores`: Lista que acumula validaciones fallidas
- `resultado`: Resultado de consulta a BD

### Correcciones realizadas:
- Se detectó vehículo vacío
- Se detectó costo negativo
- Se validó que el cliente no sea None