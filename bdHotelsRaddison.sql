--
-- File generated with SQLiteStudio v3.3.3 on vie. oct. 22 17:01:56 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: superusu
CREATE TABLE superusu (
    id_Super integer primary key,
    nombre text,
    apellido text,
    correo text,
    contrasena  text
);
INSERT INTO superusu (id_Super, nombre, apellido, correo, contrasena) VALUES (1, 'Camilo', 'Duarte', 'wmateus@uninorte.edu.co', 'Comercio*1');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
