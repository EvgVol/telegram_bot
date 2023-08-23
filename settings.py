from decouple import config


TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')

DB_NAME = config('DB_NAME')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
