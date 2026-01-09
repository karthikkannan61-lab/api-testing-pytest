import requests

class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Accept": "application/json", "User-Agent": "Mozilla/5.0"}

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint,
                            headers = self.headers,timeout = 10)


