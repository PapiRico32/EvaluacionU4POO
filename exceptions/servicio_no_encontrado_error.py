class ServicioNoEncontradoError(Exception):

    def __init__(self, id_servicio: int, mensaje_extra: str = ""):
        self.id_servicio = id_servicio
        self.mensaje = f"Servicio con ID {id_servicio} no encontrado"
        
        if mensaje_extra:
            self.mensaje += f". {mensaje_extra}"
        
        super().__init__(self.mensaje)