-- ========================================================
-- SCRIPT DE CONFIGURACIÓN INICIAL - PROYECTO VENTAS LARCO
-- Ejecutar como: SYSTEM
-- ========================================================

-- 1. Limpieza: Borrar el usuario si ya existe para evitar conflictos
DROP USER DATA_SUCURSAL CASCADE;

-- 2. Creación del usuario
-- NOTA: Reemplazar 'TU_PASSWORD_AQUI' por una clave segura antes de ejecutar.
CREATE USER DATA_SUCURSAL IDENTIFIED BY "TU_PASSWORD_AQUI";

-- 3. Permisos de Acceso y Estructura (Roles)
GRANT CONNECT, RESOURCE TO DATA_SUCURSAL;

-- 4. Permisos de Sesión y Almacenamiento
GRANT CREATE SESSION TO DATA_SUCURSAL;
GRANT UNLIMITED TABLESPACE TO DATA_SUCURSAL;

-- 5. Permisos de Visibilidad y Metadatos (Clave para Power BI/Python)
GRANT SELECT ANY TABLE TO DATA_SUCURSAL;
GRANT SELECT ANY DICTIONARY TO DATA_SUCURSAL;

-- 6. Permisos para el catálogo (Mejora la compatibilidad con Power Query)
GRANT SELECT_CATALOG_ROLE TO DATA_SUCURSAL;

COMMIT;

PROMPT >>> Configuración completada. Usuario DATA_SUCURSAL listo para usar.
