from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from models.base import Base
from models.commandLogs import CommandLog  # Importez tous les modèles ici

# config.py
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '0.0.0.0')  # Par défaut, localhost
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')  # Par défaut, 5432

DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)