import os

from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
