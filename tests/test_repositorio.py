

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'CRUD'))

from servicio import Servicio


class TestRepositorioMock:
    
    def test_crear_servicio_retorna_id(self, repositorio_test, servicio_valido):

        # Act
        id_generado = repositorio_test.crear(servicio_valido)
        
        # Assert
        assert id_generado == 1
        assert servicio_valido.id_servicio == 1
    
    def test_leer_todos_retorna_lista(self, repositorio_test, servicio_valido):
        """Prueba que leer_todos() retorne lista de servicios"""
        # Arrange
        repositorio_test.crear(servicio_valido)
        
        # Act
        resultados = repositorio_test.leer_todos()
        
        # Assert
        assert isinstance(resultados, list)
        assert len(resultados) == 1
        assert resultados[0].cliente == "Test User"
    
    def test_leer_por_id_encontrado(self, repositorio_test, servicio_valido):
        """Prueba búsqueda por ID exitosa"""
        # Arrange
        id_esperado = repositorio_test.crear(servicio_valido)
        
        # Act
        resultado = repositorio_test.leer_por_id(id_esperado)
        
        # Assert
        assert resultado is not None
        assert resultado.id_servicio == id_esperado
    
    def test_leer_por_id_no_encontrado(self, repositorio_test):
        """Prueba que ID inexistente retorne None"""
        # Act
        resultado = repositorio_test.leer_por_id(999)
        
        # Assert
        assert resultado is None
    
    def test_actualizar_servicio_existente(self, repositorio_test, servicio_valido):
        """Prueba actualización de servicio"""
        # Arrange
        id_servicio = repositorio_test.crear(servicio_valido)
        servicio_valido.tipo_servicio = "Servicio Actualizado"
        
        # Act
        exito = repositorio_test.actualizar(servicio_valido)
        
        # Assert
        assert exito is True
        assert repositorio_test.leer_por_id(id_servicio).tipo_servicio == "Servicio Actualizado"
    
    def test_actualizar_servicio_inexistente(self, repositorio_test, servicio_valido):
        """Prueba que actualizar servicio inexistente falle"""
        # Arrange
        servicio_valido.id_servicio = 999
        
        # Act
        exito = repositorio_test.actualizar(servicio_valido)
        
        # Assert
        assert exito is False
    
    def test_eliminar_servicio_existente(self, repositorio_test, servicio_valido):
        """Prueba eliminación exitosa"""
        # Arrange
        id_servicio = repositorio_test.crear(servicio_valido)
        
        # Act
        exito = repositorio_test.eliminar(id_servicio)
        
        # Assert
        assert exito is True
        assert repositorio_test.leer_por_id(id_servicio) is None
    
    def test_eliminar_servicio_inexistente(self, repositorio_test):
        """Prueba que eliminar ID inexistente falle"""
        # Act
        exito = repositorio_test.eliminar(999)
        
        # Assert
        assert exito is False