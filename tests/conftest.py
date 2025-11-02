import uuid

import pytest
from api.app import create_app
from persistent.db_utils import db
from tests.testing_config import TestingConfig

EMAIL : str = "ca.chaparros1@uniandes.edu.co"

@pytest.fixture(scope='session')
def app():
    """Fixture que crea y configura la instancia de la aplicación."""
    app = create_app(TestingConfig)

    with app.app_context():
        #db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(scope='function')
def client(app):
    """Fixture que proporciona un cliente de prueba de Flask."""
    return app.test_client()

@pytest.fixture(scope='session')
def headers():
    headers = {
        'Authorization': f'Bearer {TestingConfig.TOKEN}'
    }

    return headers

@pytest.fixture(scope='session')
def invalid_headers():
    headers = {
        'Authorization': f'Bearer INVALID_TOKEN'
    }

    return headers

@pytest.fixture(scope='function')
def add_request():
    request = {
        "email": EMAIL,
        "app_uuid": str(uuid.uuid4()),
        "blocked_reason": "Razón de bloqueo"
    }

    return request

@pytest.fixture(scope='function')
def init_database(app):
    """Fixture que garantiza que la BD esté vacía y lista para el tests."""
    with app.app_context():

        ##producto1 = Producto(nombre='Laptop', precio=1200.00)
        ##db.session.add(producto1)
        ##db.session.commit()

        yield db

        ##db.session.remove()
        ##db.session.rollback()