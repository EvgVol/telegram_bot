from pathlib import Path

from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')
VK_API_ACCESS_TOKEN = config('VK_API_ACCESS_TOKEN')
USER_ID = config('USER_ID')