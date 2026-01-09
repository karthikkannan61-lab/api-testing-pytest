from clients.base_client import BaseClient
from config.config import Config

def test_users():
    client = BaseClient(Config.BASE_URL)
    response = client.get("/users")
    assert response.status_code == 200
