import pytest
import os

from CRUD.servicio import Servicio


class TestRepositorioMock:
    
    def test_crear_servicio_retorna_id(self, repositorio_test, servicio_valido):

        id_generado = repositorio_test.crear(servicio_valido)
        
        assert id_generado == 1
        assert servicio_valido.id_servicio == 1
    
    def test_leer_todos_retorna_lista(self, repositorio_test, servicio_valido):
        repositorio_test.crear(servicio_valido)
        
        resultados = repositorio_test.leer_todos()
        
        assert isinstance(resultados, list)
        assert len(resultados) == 1
        assert resultados[0].cliente == "Test User"
    
    def test_leer_por_id_encontrado(self, repositorio_test, servicio_valido):
        id_esperado = repositorio_test.crear(servicio_valido)
        
        resultado = repositorio_test.leer_por_id(id_esperado)
        
        assert resultado is not None
        assert resultado.id_servicio == id_esperado
    
    def test_leer_por_id_no_encontrado(self, repositorio_test):
        resultado = repositorio_test.leer_por_id(999)
        
        assert resultado is None
    
    def test_actualizar_servicio_existente(self, repositorio_test, servicio_valido):
        id_servicio = repositorio_test.crear(servicio_valido)
        servicio_valido.tipo_servicio = "Servicio Actualizado"
        
        exito = repositorio_test.actualizar(servicio_valido)
        
        assert exito is True
        assert repositorio_test.leer_por_id(id_servicio).tipo_servicio == "Servicio Actualizado"
    
    def test_actualizar_servicio_inexistente(self, repositorio_test, servicio_valido):
        servicio_valido.id_servicio = 999
        
        exito = repositorio_test.actualizar(servicio_valido)
        
        assert exito is False
    
    def test_eliminar_servicio_existente(self, repositorio_test, servicio_valido):
        id_servicio = repositorio_test.crear(servicio_valido)
        
        exito = repositorio_test.eliminar(id_servicio)
        
        assert exito is True
        assert repositorio_test.leer_por_id(id_servicio) is None
    
    def test_eliminar_servicio_inexistente(self, repositorio_test):
        exito = repositorio_test.eliminar(999)
        
        assert exito is False