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
                "Referer": "https://www.google.com/",
                import requests
                from bs4 import BeautifulSoup
                import random
                import time
                from src.logger import get_logger
                from src.utils import save_json
                from src.config import OUTPUT_DIR

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

                SCRAPING_URL = "https://www.adif.es/viajeros/estado-de-la-red"
                MAX_RETRIES = 10

                def fetch_data():
                    logger = get_logger()
                    logger.info("Iniciando la obtención de datos desde la URL.")
                    for attempt in range(MAX_RETRIES):
                        try:
                            headers = {'User-Agent': random.choice(user_agents)}
                            response = requests.get(SCRAPING_URL, headers=headers)
                            response.raise_for_status()
                            logger.info("Datos obtenidos con éxito.")
                            return response.content
                        except requests.exceptions.RequestException as e:
                            logger.error(f"Intento {attempt + 1} fallido. Error: {e}")
                            time.sleep(random.uniform(1, 3))
                    logger.error("No se pudieron obtener datos después de varios intentos.")
                    return None

                def parse_data(html_content):
                    logger = get_logger()
                    logger.info("Iniciando el análisis de datos HTML.")
                    soup = BeautifulSoup(html_content, 'html.parser')
                    titulo = soup.find('h2')
                    titulo_texto = titulo.get_text(strip=True) if titulo else 'Título no encontrado'
                    avisos = []
                    for elem in soup.find_all(text=True):
                        if elem.strip().startswith("▸"):
                            avisos.append(elem.strip("▸ ").strip())
                    logger.info(f"Título extraído: {titulo_texto}")
                    logger.info(f"Número de avisos extraídos: {len(avisos)}")
                    logger.info("Datos analizados correctamente.")
                    return titulo_texto, avisos

                if __name__ == "__main__":
                    logger = get_logger()
                    html_content = fetch_data()
                    if html_content:
                        titulo, avisos = parse_data(html_content)
                        datos = {
                            "fecha_hora": titulo,
                            "avisos": avisos
                        }
                        save_json(datos)
                        logger.info(f"Scraping completado. {len(avisos)} avisos guardados.")
                    else:
                        logger.error("No se pudo obtener ni analizar datos.")
