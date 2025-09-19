# main.py
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from src.logger import get_logger
from src.utils import save_json
from src.config import URL, USER_AGENTS

def extract_avisos(soup):
    # Buscar strings que empiecen por '▸' (robusto, evita deprecated .find_all(text=...))
    avisos = []
    for s in soup.find_all(string=lambda t: t and t.strip().startswith("▸")):
        avisos.append(s.strip("▸ ").strip())
    return avisos

def extract_fecha_hora(soup):
    # Intentar encontrar un h2 que contenga "Estado de la Red" y extraer texto cercano
    # Si no, devolver fecha actual como fallback
    h2 = None
    for tag in soup.find_all("h2"):
        if "Estado de la Red" in tag.get_text():
            h2 = tag
            break
    if h2:
        return h2.get_text(strip=True)
    return f"fallback: {datetime.utcnow().isoformat()}Z"

def fetch_page(logger):
    session = requests.Session()
    # probar user agents
    for ua in random.sample(USER_AGENTS, len(USER_AGENTS)):
        headers = {
            "User-Agent": ua,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-ES,es;q=0.9",
            "Referer": "https://www.google.com/"
        }
        try:
            logger.info(f"Probando User-Agent: {ua}")
            r = session.get(URL, headers=headers, timeout=15)
            r.raise_for_status()
            return r.text
        except Exception as e:
            logger.warning(f"User-Agent fallido: {ua} - {e}")
    raise RuntimeError("No se pudo obtener la página con ningún User-Agent")

if __name__ == "__main__":
    logger = get_logger()
    logger.info("Iniciando scraper de ADIF...")
    try:
        html = fetch_page(logger)
        soup = BeautifulSoup(html, "html.parser")

        fecha_hora = extract_fecha_hora(soup)
        avisos = extract_avisos(soup)

        datos = {
            "scrape_time_utc": datetime.utcnow().isoformat() + "Z",
            "pagina_fecha_hora": fecha_hora,
            "avisos": avisos
        }

        save_json(datos)
        logger.info(f"Scraping completado. {len(avisos)} avisos guardados.")
    except Exception as e:
        logger.exception(f"Error en el scraping: {e}")
        raise

