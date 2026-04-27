import limpiador as proc
import glob
import os

def generar_archivos_locales():
    print("--- PASO 1: Generando archivos Parquet ---")

    # 1. Procesar Padrón
    archivos_padron = glob.glob('*PADRON_ARTICULOS*.DAT')
    if archivos_padron:
        df_p = proc.limpiar_padron(archivos_padron[0])
        df_p.to_parquet('productos_master.parquet', index=False)
        print(f"✓ Padrón procesado: {len(df_p)} artículos listos.")

    # 2. Procesar Ventas
    archivos_vta = glob.glob('*larti*.dat')
    
    if not archivos_vta:
        print("OJO: No se encontraron archivos .dat de ventas.")
        return

    for archivo in archivos_vta:
        df_v = proc.limpiar_ventas(archivo)

        # --- SECCIÓN DE DEBUG ---
        print(f"\n--- DEBUG ARCHIVO: {archivo} ---")
        print(f"Filas procesadas por el limpiador: {len(df_v)}")
        
        if not df_v.empty:
            print("Primeras filas:")
            print(df_v.head())
        else:
            print("OJO: El DataFrame de este archivo está VACÍO.")
        # ------------------------

        nombre_suc = os.path.basename(archivo)[:4]
        salida = f'ventas_{nombre_suc}.parquet'
        
        if not df_v.empty:
            df_v.to_parquet(salida, index=False)
            print(f"✓ Generado: {salida}")
        else:
            print(f"X No se generó {salida} por falta de datos.")

if __name__ == "__main__":
    generar_archivos_locales()