
import pytest
import os

from CRUD.servicio import Servicio


class TestServicio:
    
    def test_crear_servicio_valido(self):
        cliente = "Juan Pérez"
        vehiculo = "Toyota Corolla"
        tipo_servicio = "Cambio de aceite"
        costo = 450.00
        
        servicio = Servicio(
            cliente=cliente,
            vehiculo=vehiculo,
            tipo_servicio=tipo_servicio,
            costo=costo
        )
        
        assert servicio.cliente == cliente
        assert servicio.vehiculo == vehiculo
        assert servicio.tipo_servicio == tipo_servicio
        assert servicio.costo == costo
    
    def test_servicio_con_costo_negativo_lanza_error(self):
        costo_negativo = -100.00
        
        with pytest.raises(ValueError) as exc_info:
            Servicio(
                cliente="Test",
                vehiculo="Test",
                tipo_servicio="Test",
                costo=costo_negativo
            )
        
        assert "negativo" in str(exc_info.value).lower()
    
    def test_servicio_to_dict(self):
        servicio = Servicio(
            id_servicio=1,
            cliente="María López",
            vehiculo="Honda Civic",
            tipo_servicio="Frenos",
            costo=1200.00
        )
        
        resultado = servicio.to_dict()
        
        assert isinstance(resultado, dict)
        assert resultado['id_servicio'] == 1
        assert resultado['cliente'] == "María López"
        assert resultado['costo'] == 1200.00
    
    def test_servicio_str_representation(self):
        servicio = Servicio(
            id_servicio=5,
            cliente="Carlos Ruiz",
            vehiculo="Nissan Versa",
            tipo_servicio="Afinación",
            costo=850.00
        )
        
        resultado = str(servicio)
        
        assert "Servicio(5)" in resultado
        assert "Carlos Ruiz" in resultado
        assert "$850.0" in resultado