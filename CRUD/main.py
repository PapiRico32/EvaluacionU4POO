import sys
from repositorio_servicios import RepositorioServicios
from controlador_servicios import ControladorServicios
from interfaz_tkinter import InterfazTkinter


def main():
    try:
        # Inicializar repositorio
        repositorio = RepositorioServicios(
            host="localhost",
            user="root",
            password="",
            database="taller_mecanico"
        )
        
        if not repositorio.conectar():
            print("❌ No se pudo conectar a la base de datos")
            print("Verifique que MySQL esté ejecutándose y las credenciales sean correctas")
            sys.exit(1)
        
        print("✅ Conexión a base de datos establecida")
        
        controlador = ControladorServicios(repositorio)
        
        interfaz = InterfazTkinter(controlador)
        
        interfaz.ejecutar()
        
    except Exception as e:
        print(f"❌ Error crítico: {str(e)}")
        sys.exit(1)
    
    finally:
        if 'repositorio' in locals():
            repositorio.desconectar()
            print("✅ Conexión cerrada")


if __name__ == "__main__":
    main()