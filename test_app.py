import pytest

from app import create_app

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


def test_index(client):
    response = client.get("/")
    assert response.data == b'Hello, World!'

def test_username(client):
    response = client.get("/user/copia")
    assert response.data == b'User copia'



