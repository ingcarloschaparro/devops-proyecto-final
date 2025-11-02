import json

from tests.conftest import EMAIL

MAIN_URL: str = "/api/blacklists"


def test_home(client, app):
    """Test para home"""
    response = client.get("/")

    # Assertions:
    # HTTP Code
    assert response.status_code == 400


def test_health(client, app):
    """Test para health"""
    response = client.get(f"{MAIN_URL}/health")

    # Assertions:
    # HTTP Code
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'OK'


def test_reset(client, app, headers):
    """Test para reset"""
    response = client.delete(f"{MAIN_URL}/reset", headers=headers)

    # Assertions:
    # HTTP Code
    assert response.status_code == 200
    data = json.loads(response.data)
    # Content
    assert data['status'] == 'success'
    assert data['data'] == 'Tabla borrada exitosamente'


def test_get_by_email_without_token(client, app):
    """Test para get_by_email sin enviar token bearer"""
    response = client.get(f"{MAIN_URL}/{EMAIL}")

    # Assertions:
    # HTTP Code
    assert response.status_code == 401


def test_get_by_email_invalid_token(client, app, invalid_headers):
    """Test para get_by_email enviando un token invalido"""
    response = client.get(f"{MAIN_URL}/{EMAIL}", headers=invalid_headers)

    # Assertions:
    # HTTP Code
    assert response.status_code == 401


def test_add_without_token(client, app, add_request):
    """Test para add sin enviar token bearer"""
    response_post = client.post(
        f"{MAIN_URL}/",
        data=json.dumps(add_request),
        content_type='application/json'
    )

    # Assertions:
    # HTTP Code
    assert response_post.status_code == 401


def test_add_invalid_token(client, app, add_request, invalid_headers):
    """Test para add enviando un token invalido"""
    response_post = client.post(
        f"{MAIN_URL}/",
        data=json.dumps(add_request),
        content_type='application/json',
        headers=invalid_headers
    )

    # Assertions:
    # HTTP Code
    assert response_post.status_code == 401


def test_add_bad_request(client, app, headers):
    """Test para add con un request invalido"""
    response_post = client.post(
        f"{MAIN_URL}/",
        data=json.dumps({}),
        content_type='application/json',
        headers=headers
    )

    # Assertions:
    # HTTP Code
    assert response_post.status_code == 400


def test_get_by_email_not_found(client, app, headers):
    """Test para get_by_email con un email no encontrado"""
    response = client.get(f"{MAIN_URL}/not_found@test.com", headers=headers)

    # Assertions:
    # HTTP Code
    assert response.status_code == 200
    data = json.loads(response.data)
    # Content
    assert data['status'] == 'success'
    response_data = data['data']
    assert response_data['exists'] is False


def test_add_new(client, app, add_request, headers):
    """Test para add un email nuevo"""
    response_post = client.post(
        f"{MAIN_URL}/",
        data=json.dumps(add_request),
        content_type='application/json',
        headers=headers
    )

    # Assertions:
    # HTTP Code
    assert response_post.status_code == 201
    data = json.loads(response_post.data)
    # Content
    assert data['status'] == 'success'
    response_data = data['data']
    assert 'id' in response_data


def test_add_already_exists(client, app, add_request, headers):
    """Test para add para un email ya existente"""
    response_post = client.post(
        f"{MAIN_URL}/",
        data=json.dumps(add_request),
        content_type='application/json',
        headers=headers
    )

    # Assertions:
    # HTTP Code
    assert response_post.status_code == 409
    data = json.loads(response_post.data)
    # Content
    assert data['status'] == 'error'
    assert data['message'] == 'Ya existe el email en listas negras'


def test_get_by_email_found(client, app, headers):
    """Test para get_by_email para un email encontrado"""
    response = client.get(f"{MAIN_URL}/{EMAIL}", headers=headers)

    # Assertions:
    # HTTP Code
    assert response.status_code == 200
    data = json.loads(response.data)
    # Content
    assert data['status'] == 'success'
    response_data = data['data']
    assert response_data['exists'] is True


def test_get_all(client, app, headers):
    """Test para get_all"""
    response = client.get(f"{MAIN_URL}/", headers=headers)

    # Assertions:
    # HTTP Code
    assert response.status_code == 200
    data = json.loads(response.data)
    # Content
    assert data['status'] == 'success'
    response_data = data['data']
    assert isinstance(response_data, list)
    assert len(response_data) == 1
