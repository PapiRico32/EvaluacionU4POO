from typing import List, Optional
from servicio import Servicio
from repositorio_servicios import RepositorioServicios

import sys
sys.path.append('..')
from exceptions.servicio_no_encontrado_error import ServicioNoEncontradoError
from exceptions.costo_invalido_error import CostoInvalidoError


class ControladorServicios:
    
    def __init__(self, repositorio: RepositorioServicios):
        self.repositorio = repositorio
    
    def _validar_servicio(self, servicio: Servicio) -> None:
        if not servicio.cliente or len(servicio.cliente.strip()) == 0:
            raise ValueError("El nombre del cliente es obligatorio")
        
        if not servicio.vehiculo or len(servicio.vehiculo.strip()) == 0:
            raise ValueError("El vehículo es obligatorio")
        
        if not servicio.tipo_servicio or len(servicio.tipo_servicio.strip()) == 0:
            raise ValueError("El tipo de servicio es obligatorio")
        
        if servicio.costo <= 0:
            raise CostoInvalidoError(servicio.costo)
    
    def registrar_servicio(self, servicio: Servicio) -> int:
        self._validar_servicio(servicio)
        
        try:
            id_generado = self.repositorio.crear(servicio)
            return id_generado
        except Exception as e:
            raise Exception(f"Error al registrar servicio: {str(e)}")
    
    def consultar_todos(self) -> List[Servicio]:
        try:
            return self.repositorio.leer_todos()
        except Exception as e:
            raise Exception(f"Error al consultar servicios: {str(e)}")
    
    def consultar_por_id(self, id_servicio: int) -> Servicio:
        try:
            servicio = self.repositorio.leer_por_id(id_servicio)
            
            if servicio is None:
                raise ServicioNoEncontradoError(id_servicio)
            
            return servicio
        except ServicioNoEncontradoError:
            raise
        except Exception as e:
            raise Exception(f"Error al consultar servicio: {str(e)}")
    
    def actualizar_servicio(self, servicio: Servicio) -> bool:
        if servicio.id_servicio is None:
            raise ValueError("El ID del servicio es obligatorio para actualizar")
        
        self._validar_servicio(servicio)
        
        try:
            existente = self.repositorio.leer_por_id(servicio.id_servicio)
            if existente is None:
                raise ServicioNoEncontradoError(servicio.id_servicio)
            
            return self.repositorio.actualizar(servicio)
        except ServicioNoEncontradoError:
            raise
        except Exception as e:
            raise Exception(f"Error al actualizar servicio: {str(e)}")
    
    def eliminar_servicio(self, id_servicio: int) -> bool:
        if id_servicio is None:
            raise ValueError("El ID es obligatorio para eliminar")
        
        try:
            existente = self.repositorio.leer_por_id(id_servicio)
            if existente is None:
                raise ServicioNoEncontradoError(id_servicio)
            
            return self.repositorio.eliminar(id_servicio)
        except ServicioNoEncontradoError:
            raise
        except Exception as e:
            raise Exception(f"Error al eliminar servicio: {str(e)}")