from flask_sqlalchemy import SQLAlchemy

from utils.config import Config

print(f"Connecting to {Config.SQLALCHEMY_DATABASE_URI}")

db = SQLAlchemy()
