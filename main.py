import requests
from bs4 import BeautifulSoup
from src.logger import get_logger
from src.utils import save_json

URL = "https://www.adif.es/viajeros/estado-de-la-red"

if __name__ == "__main__":
    logger = get_logger()
    logger.info("Iniciando scraper de ADIF...")
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        response = requests.get(URL, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Extraer fecha y hora
        fecha_hora = ""
        h2 = soup.find("h2")
        if h2 and "Estado de la Red" in h2.text:
            fecha_hora = h2.text.strip()
        # Extraer avisos (cada uno empieza por '▸')
        avisos = []
        for elem in soup.find_all(text=True):
            if elem.strip().startswith("▸"):
                avisos.append(elem.strip("▸ ").strip())
        datos = {
            "fecha_hora": fecha_hora,
            "avisos": avisos
        }
        save_json(datos)
        logger.info(f"Scraping completado. {len(avisos)} avisos guardados.")
    except Exception as e:
        logger.error(f"Error en el scraping: {e}")
