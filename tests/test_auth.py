import requests

BASE_URL = "https://fakestoreapi.com"

# Usuario de ejemplo (puede ser creado previamente en test_users.py)
USERNAME = "mor_2314"
PASSWORD = "83r5^_"

def test_login_success():
    data = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(f"{BASE_URL}/auth/login", json=data)
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_failure():
    data = {"username": USERNAME, "password": "wrongpass"}
    response = requests.post(f"{BASE_URL}/auth/login", json=data)
    assert response.status_code == 401 