from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"data": {"message": "Welcome to my Python powered API!"}}
    # assert body does not have errors key
    assert "errors" not in response.json()
    assert "Trackingid" in response.headers


def test_root_authenticated():
    response = client.get("/authenticated")
    assert response.status_code == 401
    assert response.json() == {"errors": ["Could not validate credentials"]}
    assert "data" not in response.json()
    assert "Trackingid" in response.headers

    # add access_token to request and try same again, should succeed
    response = client.get("/authenticated", headers={"access_token": "apikey123"})
    assert response.status_code == 200
    assert response.json() == {"data": {"message": "Welcome to my Python powered API, username1!"}}
    # assert body does not have errors key
    assert "errors" not in response.json()


def test_no_route():
    response = client.get("/no_route")
    assert response.status_code == 404
    assert response.json() == {"errors": ["Not Found"]}
    # assert body does not have errors key
    assert "data" not in response.json()
    assert "Trackingid" in response.headers


def test_hello_world():
    response = client.get("/example/hello_world")
    assert response.status_code == 200
    assert response.json() == {"data": "Hello World from my Python API!"}
    # assert body does not have errors key
    assert "errors" not in response.json()
    assert "Trackingid" in response.headers


def test_example_list():
    response = client.get("/example/list")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "paging" in data
    assert len(data["data"]) > 0  # Check if data list is not empty
    assert "Trackingid" in response.headers


def test_example_error():
    response = client.get("/example/error")
    assert response.status_code == 400
    assert "errors" in response.json()
    assert response.json()["errors"] == ["An error occurred"]
    assert "Trackingid" in response.headers
