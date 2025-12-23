import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    try:
        return mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'taskflow_db'),
            port=int(os.getenv('DB_PORT', 3306))
        )
    except mysql.connector.Error as err:
        print(f"Error de conexión a DB: {err}")
        return None  # O lanza el error si quieres