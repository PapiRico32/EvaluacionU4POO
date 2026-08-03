CREATE DATABASE IF NOT EXISTS taller_mecanico;
USE taller_mecanico;

CREATE TABLE IF NOT EXISTS servicios (
    id_servicio INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    vehiculo VARCHAR(100) NOT NULL,
    tipo_servicio VARCHAR(100) NOT NULL,
    costo DECIMAL(10, 2) NOT NULL CHECK (costo > 0),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Datos de prueba opcionales
INSERT INTO servicios (cliente, vehiculo, tipo_servicio, costo) VALUES
('Juan Pérez', 'Toyota Corolla 2020', 'Cambio de aceite', 450.00),
('María López', 'Honda Civic 2019', 'Frenos delanteros', 1200.00),
('Carlos Ruiz', 'Nissan Versa 2021', 'Afinación mayor', 850.00);