import requests
from bs4 import BeautifulSoup
from src.logger import get_logger
from src.utils import save_json

URL = "https://www.adif.es/viajeros/estado-de-la-red"

if __name__ == "__main__":
    logger = get_logger()
    logger.info("Iniciando scraper de ADIF...")
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # TODO: Extraer la información relevante de la página
        # Ejemplo: datos = {...}
        datos = {"html_length": len(response.text)}  # Placeholder
        save_json(datos)
        logger.info("Scraping completado y datos guardados.")
    except Exception as e:
        logger.error(f"Error en el scraping: {e}")
