class CostoInvalidoError(Exception):
    
    def __init__(self, costo: float, mensaje_extra: str = ""):
        self.costo = costo
        self.mensaje = f"Costo inválido: ${costo}. El costo debe ser mayor a 0"
        
        if mensaje_extra:
            self.mensaje += f". {mensaje_extra}"
        
        super().__init__(self.mensaje)