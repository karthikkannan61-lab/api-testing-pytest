from clients.api_key_client import APIkeyClient
from config.config import Config

def test_level2():
    client = APIkeyClient(
        Config.BASE_URL_2,
        api_key="afe3bb50bafb6ff43aa4346f25e7000c"
    )
    r = client.get("/weather", params={"q": "London"})
    assert r.status_code == 200