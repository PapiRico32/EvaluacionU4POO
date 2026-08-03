import pytest
import os


from CRUD.servicio import Servicio
from exceptions.servicio_no_encontrado_error import ServicioNoEncontradoError
from exceptions.costo_invalido_error import CostoInvalidoError


class TestControladorServicios:
    
    def test_registrar_servicio_valido(self, controlador_test, servicio_valido):
        
        id_generado = controlador_test.registrar_servicio(servicio_valido)
        
        assert id_generado == 1
        assert servicio_valido.id_servicio == 1
    
    def test_registrar_servicio_costo_invalido(self, controlador_test):
        servicio = Servicio(
            cliente="Test",
            vehiculo="Test",
            tipo_servicio="Test",
            costo=-50.00
        )
        
        with pytest.raises(CostoInvalidoError):
            controlador_test.registrar_servicio(servicio)
    
    def test_consultar_todos(self, controlador_test, servicio_valido):
        controlador_test.registrar_servicio(servicio_valido)
        
        resultados = controlador_test.consultar_todos()
        
        assert len(resultados) == 1
        assert resultados[0].cliente == "Test User"
    
    def test_consultar_por_id_existente(self, controlador_test, servicio_valido):
        id_esperado = controlador_test.registrar_servicio(servicio_valido)
        
        resultado = controlador_test.consultar_por_id(id_esperado)
        
        assert resultado.id_servicio == id_esperado
    
    def test_consultar_por_id_inexistente(self, controlador_test):
        with pytest.raises(ServicioNoEncontradoError):
            controlador_test.consultar_por_id(999)
    
    def test_actualizar_servicio(self, controlador_test, servicio_valido):
        id_servicio = controlador_test.registrar_servicio(servicio_valido)
        servicio_valido.costo = 150.00
        
        exito = controlador_test.actualizar_servicio(servicio_valido)
        
        assert exito is True
        assert controlador_test.consultar_por_id(id_servicio).costo == 150.00
    
    def test_actualizar_servicio_inexistente(self, controlador_test, servicio_valido):
        servicio_valido.id_servicio = 999
        
        with pytest.raises(ServicioNoEncontradoError):
            controlador_test.actualizar_servicio(servicio_valido)
    
    def test_eliminar_servicio(self, controlador_test, servicio_valido):
        id_servicio = controlador_test.registrar_servicio(servicio_valido)
        
        exito = controlador_test.eliminar_servicio(id_servicio)
        
        assert exito is True
        
        with pytest.raises(ServicioNoEncontradoError):
            controlador_test.consultar_por_id(id_servicio)
    
    def test_eliminar_servicio_inexistente(self, controlador_test):
        with pytest.raises(ServicioNoEncontradoError):
            controlador_test.eliminar_servicio(999)