from dotenv import dotenv_values

config = dotenv_values('.env')
DB_HOST = config.get("DB_HOST")
DB_PORT = config.get("DB_PORT")
DB_NAME = config.get("DB_NAME")
DB_USER = config.get("DB_USER")
DB_PASS = config.get("DB_PASS")
DB_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
