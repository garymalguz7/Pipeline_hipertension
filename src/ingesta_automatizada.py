import os
import shutil
import logging
from datetime import datetime

# Configurar el registro de eventos
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def ingestar_datos(ruta_origen, ruta_destino):
    logging.info("Iniciando la ingesta de datos...")
    
    try:
        # Crear carpeta de destino si no existe
        if not os.path.exists(ruta_destino):
            os.makedirs(ruta_destino)
            
        # Verificar que el archivo origen exista
        if not os.path.exists(ruta_origen):
            raise FileNotFoundError("No se encontró el archivo de origen.")
            
        # Generar nombre con marca de tiempo
        nombre_archivo = os.path.basename(ruta_origen)
        nombre_sin_ext, ext = os.path.splitext(nombre_archivo)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nuevo_nombre = f"{nombre_sin_ext}_ingested_{timestamp}{ext}"
        ruta_final = os.path.join(ruta_destino, nuevo_nombre)
        
        # Copiar archivo
        shutil.copy2(ruta_origen, ruta_final)
        logging.info(f"Éxito: Archivo guardado en {ruta_final}")
        
    except Exception as e:
        logging.error(f"Error en la ingesta: {e}")

if __name__ == "__main__":
    ARCHIVO_ORIGEN = "../data/source/riesgo_hipertension_dataset.csv"
    CARPETA_DESTINO = "../data/raw/"
    ingestar_datos(ARCHIVO_ORIGEN, CARPETA_DESTINO)