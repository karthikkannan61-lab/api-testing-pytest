import requests

class APIkeyClient:
    def __init__(self,base_url,api_key):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.headers = {"Accept": "application/json",}

    def get(self, endpoint, params=None):
        if params == None:
            params = {}
        params["appid"] =  self.api_key

        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params,
            timeout=10
        )