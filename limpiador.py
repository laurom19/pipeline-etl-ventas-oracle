import pandas as pd

def limpiar_padron(ruta):
    # Basado en tu formato: 1001|ARTICULO_TIPO_A_PROMO|150.00|245.50
    df = pd.read_csv(ruta, sep='|', header=None, 
                     names=['PLU', 'NOMBRE', 'COSTO', 'VENTA'], 
                     encoding='latin-1', dtype={'PLU': str})
    
    # Solo las columnas que pide el CREATE TABLE PRODUCTOS
    return df[['PLU', 'NOMBRE']].drop_duplicates(subset=['PLU'])

def limpiar_ventas(ruta):
    # Basado en tu larti anonimizado: 102|99|20260425|231015|1|1500.50|315.10|1815.60|0|0
    df = pd.read_csv(ruta, sep='|', header=None, encoding='latin-1')
    
    # Mapeo inicial (usando los índices correctos del archivo de 10 columnas)
    df_v = df[[0, 1, 2, 4, 7]].copy()
    df_v.columns = ['SUCURSAL', 'CAJA', 'FECHA_STR', 'TICKET', 'IMPORTE']
    
    # Transformación de datos
    df_v['FECHA'] = pd.to_datetime(df_v['FECHA_STR'], format='%Y%m%d', errors='coerce')
    df_v['PLU'] = '999' # Valor temporal de prueba
    
    # FILTRO FINAL: Solo columnas que existen en la tabla VENTAS de Oracle
    columnas_oracle = ['SUCURSAL', 'FECHA', 'CAJA', 'TICKET', 'PLU', 'IMPORTE']
    
    return df_v[columnas_oracle].dropna(subset=['FECHA'])