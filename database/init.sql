CREATE TABLE IF NOT EXISTS "members" (
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    legajo INT PRIMARY KEY,
    feature TEXT NOT NULL,
    servicio TEXT NOT NULL,
    estado TEXT NOT NULL
);

INSERT INTO "members" (nombre, apellido, legajo, feature, servicio, estado) VALUES
('Ignacio', 'Benitez', 33507, '4', 'database', 'en proceso'),
('Matias', 'Dieguez', 33080, '2', 'frontend', 'en proceso'),
('Naim', 'Guarino', 32683, '1,5', 'infra', 'en proceso'),
('Agustín', 'Manrique', 31976, '3', 'backend', 'en proceso');
