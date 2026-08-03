import pdb
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'CRUD'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from servicio import Servicio
from repositorio_servicios import RepositorioServicios


def buscar_servicio_debug():
    print("=" * 50)
    print("DEBUG - Búsqueda en Base de Datos")
    print("=" * 50)
    
    repositorio = RepositorioServicios(
        host="localhost",
        user="root",
        password="",
        database="cru_ana_celia"
    )
    
    if not repositorio.conectar():
        print("❌ Error de conexión a la BD")
        return
    
    print("✅ Conexión establecida")
    print("\nBuscando servicio con ID = 1")
    print("Presiona Enter para iniciar debugging...")
    input()
    
    id_busqueda = 1
    
    pdb.set_trace()
    
    print(f"\nEjecutando consulta para ID: {id_busqueda}")
    resultado = repositorio.leer_por_id(id_busqueda)
    
    pdb.set_trace()
    
    if resultado:
        print(f"\n✅ Servicio encontrado:")
        print(f"   ID: {resultado.id}")
        print(f"   Cliente: {resultado.cliente}")
        print(f"   Vehículo: {resultado.vehiculo}")
        print(f"   Costo: ${resultado.costo}")
    else:
        print("\n❌ Servicio no encontrado")
    
    print("\n\nBuscando servicio inexistente (ID = 999)")
    print("Presiona Enter para continuar...")
    input()
    
    pdb.set_trace()
    
    resultado_inexistente = repositorio.leer_por_id(999)
    
    pdb.set_trace()
    
    if resultado_inexistente:
        print(f"\n✅ Encontrado: {resultado_inexistente}")
    else:
        print("\n❌ No encontrado (como se esperaba)")
    
    repositorio.desconectar()
    print("\n✅ Debugging completado - Conexión cerrada")


if __name__ == "__main__":
    buscar_servicio_debug()