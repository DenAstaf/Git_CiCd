from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '"Hello, World!"'


def test_read_json():
    response = client.get("/json")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World in JSON!"}


def test_read_templated_html():
    response = client.get("/html")
    assert response.status_code == 200
    assert "Hello, Templated World!" in response.text
    assert "Hello, World in HTML with Templating!" in response.text


def test_read_fake_route():
    response = client.get("/fake")
    assert response.status_code == 404
