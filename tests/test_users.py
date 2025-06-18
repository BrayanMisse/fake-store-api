import requests
import random
import string

BASE_URL = "https://fakestoreapi.com"

def random_email():
    return ''.join(random.choices(string.ascii_lowercase, k=8)) + "@test.com"

def test_register_user():
    user_data = {
        "email": random_email(),
        "username": "testuser",
        "password": "testpass123",
        "name": {"firstname": "Test", "lastname": "User"},
        "address": {"city": "TestCity", "street": "TestStreet", "number": 1, "zipcode": "12345", "geolocation": {"lat": "0", "long": "0"}},
        "phone": "1234567890"
    }
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_register_user_missing_fields():
    user_data = {"username": "testuser"}
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    assert response.status_code in [400, 500] 