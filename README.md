# ADIF Scraper

Scraper para https://www.adif.es/viajeros/estado-de-la-red usando requests + BeautifulSoup.
Guarda resultados en `data/YYYY-MM-DD_HHMMSS.json`. Docker + docker-compose incluidos.

## Quickstart (local)
1. Crear entorno virtual e instalar:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
