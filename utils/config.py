import os

class Config:
    TOKEN = "f18dadb0-c911-46ac-854f-e552ef323cda"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:users12345@localhost:5432/postgres"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False