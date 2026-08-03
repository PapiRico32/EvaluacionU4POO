# Pruebas Unitarias - Taller Mecánico

## Ejecutar pruebas

```bash
cd tests
pytest -v
```

## Estructura de pruebas

- `test_servicio.py`: Pruebas para la entidad Servicio
- `test_repositorio.py`: Pruebas para el repositorio (mock)
- `test_controlador.py`: Pruebas para el controlador
- `conftest.py`: Configuración y fixtures

## Patrón AAA

Todas las pruebas siguen el patrón:
1. **Arrange**: Configurar datos de entrada
2. **Act**: Ejecutar la acción a probar
3. **Assert**: Verificar resultados

## Principios F.I.R.S.T.

- **Fast**: Las pruebas son rápidas
- **Isolated**: Cada prueba es independiente
- **Repeatable**: Resultados consistentes
- **Self-validating**: Resultado claro (pass/fail)
- **Timely**: Escritas antes o durante el desarrollo