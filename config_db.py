import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carga las variables del archivo .env
load_dotenv()

def conectar_oracle():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    sid = os.getenv('DB_SID')
    
    # Construir la cadena de conexión
    conn_str = f"oracle+oracledb://{user}:{password}@{host}:{port}/{sid}"
    engine = create_engine(conn_str)
    return engine