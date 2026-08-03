import mysql.connector
from mysql.connector import Error
from typing import List, Optional
from servicio import Servicio
from datetime import datetime


class RepositorioServicios:
    
    def __init__(self, host: str = "localhost", user: str = "root", 
                 password: str = "", database: str = "taller_mecanico"):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self.connection = None
    
    def conectar(self) -> bool:
        try:
            self.connection = mysql.connector.connect(**self.config)
            return self.connection.is_connected()
        except Error as e:
            print(f"Error de conexión: {e}")
            return False
    
    def desconectar(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def crear(self, servicio: Servicio) -> int:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO servicios (cliente, vehiculo, tipo_servicio, costo)
                VALUES (%s, %s, %s, %s)
            """
            valores = (servicio.cliente, servicio.vehiculo, 
                      servicio.tipo_servicio, servicio.costo)
            cursor.execute(query, valores)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            self.connection.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()
    
    def leer_todos(self) -> List[Servicio]:
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM servicios ORDER BY id_servicio DESC")
            resultados = cursor.fetchall()
            
            servicios = []
            for row in resultados:
                servicio = Servicio(
                    id_servicio=row['id_servicio'],
                    cliente=row['cliente'],
                    vehiculo=row['vehiculo'],
                    tipo_servicio=row['tipo_servicio'],
                    costo=float(row['costo']),
                    fecha_registro=row['fecha_registro']
                )
                servicios.append(servicio)
            return servicios
        except Error as e:
            raise e
        finally:
            if cursor:
                cursor.close()
    
    def leer_por_id(self, id_servicio: int) -> Optional[Servicio]:
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM servicios WHERE id_servicio = %s"
            cursor.execute(query, (id_servicio,))
            resultado = cursor.fetchone()
            
            if resultado:
                return Servicio(
                    id_servicio=resultado['id_servicio'],
                    cliente=resultado['cliente'],
                    vehiculo=resultado['vehiculo'],
                    tipo_servicio=resultado['tipo_servicio'],
                    costo=float(resultado['costo']),
                    fecha_registro=resultado['fecha_registro']
                )
            return None
        except Error as e:
            raise e
        finally:
            if cursor:
                cursor.close()
    
    def actualizar(self, servicio: Servicio) -> bool:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
                UPDATE servicios 
                SET cliente=%s, vehiculo=%s, tipo_servicio=%s, costo=%s
                WHERE id_servicio=%s
            """
            valores = (servicio.cliente, servicio.vehiculo, 
                      servicio.tipo_servicio, servicio.costo, 
                      servicio.id_servicio)
            cursor.execute(query, valores)
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            self.connection.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()
    
    def eliminar(self, id_servicio: int) -> bool:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM servicios WHERE id_servicio = %s"
            cursor.execute(query, (id_servicio,))
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            self.connection.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()