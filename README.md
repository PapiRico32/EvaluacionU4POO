# Sistema CRUD - Taller Mecánico

Sistema de gestión de servicios para taller mecánico desarrollado con Python, Tkinter y MySQL.

## Requisitos

- Python 3.8+
- MySQL 8.0+
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar o descargar el proyecto

```bash
cd EvaluacionU4POO
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar base de datos

1. Asegúrate de que MySQL esté ejecutándose
2. Ejecuta el script SQL:

```bash
mysql -u root -p < CRUD/db_taller.sql
```

3. Ingresa tu contraseña de MySQL cuando se solicite

## Ejecución

Desde la carpeta `CRUD`:

```bash
cd CRUD
python main.py
```


## Ejecutar pruebas

```bash
cd tests
pytest -v
```

## Características

- ✅ CRUD completo (Crear, Leer, Actualizar, Eliminar)
- ✅ Interfaz gráfica con Tkinter
- ✅ Validaciones de datos
- ✅ Excepciones personalizadas
- ✅ Pruebas unitarias con pytest
- ✅ Principios SOLID y POO

## Tecnologías

- **Lenguaje**: Python 3.8+
- **GUI**: Tkinter
- **Base de datos**: MySQL
- **Pruebas**: pytest
- **Conector BD**: mysql-connector-python

## Autor

Desarrollado como proyecto educativo aplicando:
- Programación Orientada a Objetos (POO)
- Principios SOLID
- Pruebas unitarias (patrón AAA, principios F.I.R.S.T.)
- Manejo de excepciones
- Debugging con pdb