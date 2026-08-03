import pdb


from CRUD.servicio import Servicio


def validar_servicio_debug(servicio: Servicio):
    """Función con breakpoint para inspeccionar validación"""
    print("=" * 50)
    print("INICIANDO DEBUG DE VALIDACIÓN DE SERVICIO")
    print("=" * 50)
    
    pdb.set_trace()
    
    errores = []
    
    if not servicio.cliente or len(servicio.cliente.strip()) == 0:
        errores.append("Cliente vacío")
    
    if not servicio.vehiculo or len(servicio.vehiculo.strip()) == 0:
        errores.append("Vehículo vacío")
    
    if servicio.costo <= 0:
        errores.append(f"Costo inválido: {servicio.costo}")
    
    print(f"Errores encontrados: {errores}")
    
    return len(errores) == 0


def main():
    print("Creando servicio de prueba...")
    
  
    servicio_prueba = Servicio(
        cliente="Juan Pérez",
        vehiculo="", 
        tipo_servicio="Cambio de aceite",
        costo=-100.00 
    )
    
    print(f"Servicio creado: {servicio_prueba}")

    es_valido = validar_servicio_debug(servicio_prueba)
    
    print(f"¿Servicio válido? {es_valido}")


if __name__ == "__main__":
    main()