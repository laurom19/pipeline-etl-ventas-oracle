import pandas as pd
import config_db as db
import glob
import os

def cargar_datos():
    print("--- PASO 2: Iniciando carga a Oracle ---")
    
    try:
        engine = db.conectar_oracle()
        
        # 1. Cargar Productos
        if os.path.exists('productos_master.parquet'):
            df_p = pd.read_parquet('productos_master.parquet')
            print(f"DEBUG: Leídos {len(df_p)} productos del Parquet.")
            
            # Usamos el nombre de la tabla en MAYÚSCULAS
            df_p.to_sql('PRODUCTOS', engine, if_exists='append', index=False)
            print("✓ Tabla PRODUCTOS actualizada.")

        # 2. Cargar Ventas
        archivos_parquet = glob.glob('ventas_*.parquet')
        
        if not archivos_parquet:
            print("OJO: No se encontraron archivos .parquet para cargar.")
            return

        for archivo in archivos_parquet:
            df_v = pd.read_parquet(archivo)
            
            # --- PUNTO DE CONTROL ---
            print(f"\n--- DEBUG CARGA: {archivo} ---")
            print(f"Filas a insertar: {len(df_v)}")
            print("Columnas detectadas:", df_v.columns.tolist())
            
        if not df_v.empty:
            # Oracle prefiere nombres en minúscula a veces para evitar el Warning
            df_v.to_sql('ventas', engine, if_exists='append', index=False)
            print(f"✓ {archivo} cargado exitosamente.")
        else:
                print(f"X Saltando {archivo} porque está vacío.")

        
    except Exception as e:
        print(f"\n❌ ERROR EN LA CARGA: {e}")

if __name__ == "__main__":
    cargar_datos()