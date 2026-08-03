import pdb


from CRUD.servicio import Servicio
from CRUD.repositorio_servicios import RepositorioServicios


def buscar_servicio_debug(repositorio: RepositorioServicios, id_busqueda: int):
    """Función con breakpoint para depurar búsqueda en BD"""
    print("=" * 50)
    print("INICIANDO DEBUG DE BÚSQUEDA EN BASE DE DATOS")
    print("=" * 50)
    
    pdb.set_trace()
    
    print(f"Buscando servicio con ID: {id_busqueda}")
    
    resultado = repositorio.leer_por_id(id_busqueda)
    
    pdb.set_trace()
    
    if resultado:
        print(f"✅ Servicio encontrado: {resultado}")
    else:
        print(f"❌ Servicio no encontrado")
    
    return resultado


def main():
    """Ejecuta el debugging de BD"""
    print("Conectando a base de datos...")
    
    repositorio = RepositorioServicios(
        host="localhost",
        user="root",
        password="",
        database="taller_mecanico"
    )
    
    if not repositorio.conectar():
        print("❌ No se pudo conectar a la BD")
        return
    
    print("✅ Conexión establecida")
    
    print("\n--- Prueba 1: ID existente ---")
    buscar_servicio_debug(repositorio, 1)
    
    print("\n--- Prueba 2: ID inexistente ---")
    buscar_servicio_debug(repositorio, 999)
    
    repositorio.desconectar()
    print("\n✅ Debugging completado")


if __name__ == "__main__":
    main()