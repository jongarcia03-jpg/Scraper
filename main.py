import requests
import random
from bs4 import BeautifulSoup
from src.logger import get_logger
from src.utils import save_json

URL = "https://www.adif.es/viajeros/estado-de-la-red"

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/90.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/18.18363',
    'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
]

if __name__ == "__main__":
    logger = get_logger()
    logger.info("Iniciando scraper de ADIF...")
    try:
        response = None
        for ua in random.sample(user_agents, len(user_agents)):
            headers = {
                "User-Agent": ua,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Cache-Control": "max-age=0",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Referer": "https://www.google.com/"
            }
            try:
                logger.info(f"Probando User-Agent: {ua}")
                response = requests.get(URL, headers=headers)
                response.raise_for_status()
                break
            except Exception as e:
                logger.warning(f"User-Agent fallido: {ua} - {e}")
        if response is None or response.status_code != 200:
            raise Exception("No se pudo acceder a la web con ningún User-Agent")
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
