import requests

BASE_URL = "https://fakestoreapi.com"

# Obtener carrito de usuario existente

def test_get_cart_user():
    response = requests.get(f"{BASE_URL}/carts/user/2")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Eliminar carrito existente (puede fallar si no existe, es solo ejemplo)
def test_delete_cart():
    # Primero crear un carrito para asegurar que existe
    cart_data = {"userId": 2, "date": "2020-03-02", "products": [{"productId": 1, "quantity": 1}]}
    create_resp = requests.post(f"{BASE_URL}/carts", json=cart_data)
    cart_id = create_resp.json().get("id")
    if cart_id:
        del_resp = requests.delete(f"{BASE_URL}/carts/{cart_id}")
        assert del_resp.status_code == 200
    else:
        assert False, "No se pudo crear carrito para eliminar"

# Actualizar producto (PUT)
def test_update_product():
    update_data = {"title": "Nuevo título", "price": 99.99}
    response = requests.put(f"{BASE_URL}/products/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Nuevo título" 