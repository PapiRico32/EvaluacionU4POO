import pdb
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'CRUD'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from servicio import Servicio


def validar_servicio_debug():
    print("=" * 50)
    print("DEBUG - Validación de Servicio")
    print("=" * 50)
    
    servicio = Servicio(
        cliente="Ana Celia",
        vehiculo="Toyota",
        tipo_servicio="Mantenimiento",
        costo=100.00
    )
    
    print(f"\nServicio creado: {servicio}")
    print("\nPresiona Enter para iniciar debugging...")
    input()
    
    pdb.set_trace()
    
    print("\n--- Iniciando validaciones ---")
    errores = []
    
    if not servicio.cliente or not servicio.cliente.strip():
        errores.append("Cliente vacío")
        print("❌ Cliente vacío")
    else:
        print("✅ Cliente válido")
    
    if not servicio.vehiculo or not servicio.vehiculo.strip():
        errores.append("Vehículo vacío")
        print("❌ Vehículo vacío")
    else:
        print("✅ Vehículo válido")
    
    if servicio.costo <= 0:
        errores.append(f"Costo inválido: {servicio.costo}")
        print(f"❌ Costo inválido: ${servicio.costo}")
    else:
        print(f"✅ Costo válido: ${servicio.costo}")
    
    print(f"\nErrores encontrados: {errores}")
    print(f"¿Servicio válido? {len(errores) == 0}")
    
    return len(errores) == 0


def debug_servicio_con_error():
    print("=" * 50)
    print("DEBUG - Servicio con datos inválidos")
    print("=" * 50)
    
    print("\nCreando servicio con vehículo vacío y costo negativo...")
    print("El breakpoint se activará ANTES de la validación")
    print("\nPresiona Enter para continuar...")
    input()
    
    servicio = Servicio(
        cliente="Test User",
        vehiculo="",
        tipo_servicio="Test Service",
        costo=50.00
    )
    
    pdb.set_trace()
    
    print("\n--- Validando servicio ---")
    
    if not servicio.cliente:
        print("❌ Cliente vacío")
    
    if not servicio.vehiculo:
        print("❌ Vehículo vacío")
    
    if servicio.costo <= 0:
        print(f"❌ Costo inválido: {servicio.costo}")
    else:
        print(f"✅ Costo válido: ${servicio.costo}")
    
    return servicio


if __name__ == "__main__":
    print("\n=== Opción 1: Servicio válido ===")
    validar_servicio_debug()
    
    print("\n\n=== Opción 2: Servicio con error ===")
    debug_servicio_con_error()
    
    print("\n✅ Debugging completado")