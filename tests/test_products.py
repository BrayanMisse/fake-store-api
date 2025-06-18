import requests

BASE_URL = "https://fakestoreapi.com"

def test_list_products():
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]

def test_get_product_valid():
    response = requests.get(f"{BASE_URL}/products/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_product_invalid():
    response = requests.get(f"{BASE_URL}/products/99999")
    assert response.status_code == 404 