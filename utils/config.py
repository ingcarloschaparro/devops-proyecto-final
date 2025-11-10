import os


class Config:
    TOKEN = "f18dadb0-c911-46ac-854f-e552ef323cda"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres123456@" +
        "postgres.crgu42es8gyo.us-east-2.rds.amazonaws.com:5432/postgres"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = os.getenv('TEST_ENV', 'False') == 'True'
