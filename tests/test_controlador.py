
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'CRUD'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'exceptions'))

from servicio import Servicio
from exceptions.servicio_no_encontrado_error import ServicioNoEncontradoError
from exceptions.costo_invalido_error import CostoInvalidoError


class TestControladorServicios:
    """Pruebas para el controlador de servicios"""
    
    def test_registrar_servicio_valido(self, controlador_test, servicio_valido):
        """Prueba registro exitoso de servicio"""
        # Arrange - ya está en el fixture
        
        # Act
        id_generado = controlador_test.registrar_servicio(servicio_valido)
        
        # Assert
        assert id_generado == 1
        assert servicio_valido.id_servicio == 1
    
    def test_registrar_servicio_costo_invalido(self, controlador_test):
        """Prueba que costo inválido lance excepción"""
        # Arrange
        servicio = Servicio(
            cliente="Test",
            vehiculo="Test",
            tipo_servicio="Test",
            costo=-50.00
        )
        
        # Act & Assert
        with pytest.raises(CostoInvalidoError):
            controlador_test.registrar_servicio(servicio)
    
    def test_consultar_todos(self, controlador_test, servicio_valido):
        """Prueba consulta de todos los servicios"""
        # Arrange
        controlador_test.registrar_servicio(servicio_valido)
        
        # Act
        resultados = controlador_test.consultar_todos()
        
        # Assert
        assert len(resultados) == 1
        assert resultados[0].cliente == "Test User"
    
    def test_consultar_por_id_existente(self, controlador_test, servicio_valido):
        """Prueba consulta por ID exitosa"""
        # Arrange
        id_esperado = controlador_test.registrar_servicio(servicio_valido)
        
        # Act
        resultado = controlador_test.consultar_por_id(id_esperado)
        
        # Assert
        assert resultado.id_servicio == id_esperado
    
    def test_consultar_por_id_inexistente(self, controlador_test):
        """Prueba que consultar ID inexistente lance excepción"""
        # Act & Assert
        with pytest.raises(ServicioNoEncontradoError):
            controlador_test.consultar_por_id(999)
    
    def test_actualizar_servicio(self, controlador_test, servicio_valido):
        """Prueba actualización de servicio"""
        # Arrange
        id_servicio = controlador_test.registrar_servicio(servicio_valido)
        servicio_valido.costo = 150.00
        
        # Act
        exito = controlador_test.actualizar_servicio(servicio_valido)
        
        # Assert
        assert exito is True
        assert controlador_test.consultar_por_id(id_servicio).costo == 150.00
    
    def test_actualizar_servicio_inexistente(self, controlador_test, servicio_valido):
        """Prueba que actualizar servicio inexistente falle"""
        # Arrange
        servicio_valido.id_servicio = 999
        
        # Act & Assert
        with pytest.raises(ServicioNoEncontradoError):
            controlador_test.actualizar_servicio(servicio_valido)
    
    def test_eliminar_servicio(self, controlador_test, servicio_valido):
        """Prueba eliminación de servicio"""
        # Arrange
        id_servicio = controlador_test.registrar_servicio(servicio_valido)
        
        # Act
        exito = controlador_test.eliminar_servicio(id_servicio)
        
        # Assert
        assert exito is True
        
        with pytest.raises(ServicioNoEncontradoError):
            controlador_test.consultar_por_id(id_servicio)
    
    def test_eliminar_servicio_inexistente(self, controlador_test):
        """Prueba que eliminar ID inexistente lance excepción"""
        # Act & Assert
        with pytest.raises(ServicioNoEncontradoError):
            controlador_test.eliminar_servicio(999)