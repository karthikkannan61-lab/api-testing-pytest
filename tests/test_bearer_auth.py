from clients.bearer_client import BearerClient
from config.config import Config

def test_bearer_token_auth():
    client = BearerClient(Config.BASE_URL_3)

    # 1️⃣ LOGIN
    login_response = client.login(
        username="mor_2314",
        password="83r5^_"
    )

    print("\n--- LOGIN RESPONSE ---")
    print("Status code:", login_response.status_code)
    print("Response body:", login_response.json())

    assert login_response.status_code in(200,201)
    assert client.token is not None

    # 2️⃣ PROTECTED CALL (token required)
    products_response = client.get_products()

    print("\n--- PRODUCTS RESPONSE ---")
    print("Status code:", products_response.status_code)

    assert products_response.status_code in (200,201)
