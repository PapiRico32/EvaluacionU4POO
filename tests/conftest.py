
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'CRUD'))

from servicio import Servicio
from repositorio_servicios import RepositorioServicios
from controlador_servicios import ControladorServicios


@pytest.fixture
def servicio_valido():
    return Servicio(
        cliente="Test User",
        vehiculo="Test Car",
        tipo_servicio="Test Service",
        costo=100.00
    )


@pytest.fixture
def servicio_invalido_costo():
    return Servicio(
        cliente="Test User",
        vehiculo="Test Car",
        tipo_servicio="Test Service",
        costo=-50.00
    )


@pytest.fixture
def repositorio_test():
    class RepositorioMock:
        def __init__(self):
            self.servicios = {}
            self.next_id = 1
        
        def conectar(self):
            return True
        
        def desconectar(self):
            pass
        
        def crear(self, servicio):
            servicio.id_servicio = self.next_id
            self.servicios[self.next_id] = servicio
            self.next_id += 1
            return servicio.id_servicio
        
        def leer_todos(self):
            return list(self.servicios.values())
        
        def leer_por_id(self, id_servicio):
            return self.servicios.get(id_servicio)
        
        def actualizar(self, servicio):
            if servicio.id_servicio in self.servicios:
                self.servicios[servicio.id_servicio] = servicio
                return True
            return False
        
        def eliminar(self, id_servicio):
            if id_servicio in self.servicios:
                del self.servicios[id_servicio]
                return True
            return False
    
    return RepositorioMock()


@pytest.fixture
def controlador_test(repositorio_test):
    """Fixture para controlador con repositorio mock"""
    return ControladorServicios(repositorio_test)