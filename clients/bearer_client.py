import requests

class BearerClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.token = None

    def login(self, username, password):
        response = requests.post(
            f"{self.base_url}/auth/login",
            json={
                "username": username,
                "password": password
            },
            timeout=10
        )

        self.token = response.json().get("token")
        return response

    def get_products(self):
        return requests.get(
            f"{self.base_url}/products",
            headers={
                "Authorization": f"Bearer {self.token}"
            },
            timeout=10
        )
