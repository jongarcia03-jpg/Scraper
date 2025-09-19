import os
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
